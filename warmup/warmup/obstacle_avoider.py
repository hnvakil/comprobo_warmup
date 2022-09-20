import rclpy
import time
import numpy as np
import math
import tty
import select
import sys
import termios
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_subscription(LaserScan, 'stable_scan', self.process_scan, 10)
        self.scan = []
        self.processed_scan = []
        self.x_weight = 0
        self.y_weight = 0

    
    def run_loop(self):
        msg = Twist()
        # run scan
        self.processed_scan = []
        for reading in range(len(self.scan)):
            if 0.1 <= self.scan[reading] <= 4:
                self.processed_scan.append(self.scan[reading])
            else:
                self.processed_scan.append(200)
        
        self.x_weight = 0
        self.y_weight = 0
        #pos y means weight from front
        #pos x means weight from left
        for angle in range(len(self.processed_scan)):
            reading = 1/self.processed_scan[angle]
            x_comp = math.sin(math.radians(angle))
            y_comp = math.cos(math.radians(angle))
            self.x_weight = self.x_weight + reading * x_comp
            self.y_weight += reading * y_comp

        y_go_weight = math.floor(-1 * self.y_weight)
        x_go_weight = math.floor(-1 * self.x_weight)
        print(x_go_weight)
        print(y_go_weight)
        #print(y_go_weight/x_go_weight)

        try:
            tan_dir = math.degrees(math.atan(abs(y_go_weight) / x_go_weight))
            tan_dir = np.sign(tan_dir) * 90 - tan_dir
            if y_go_weight < 0:
                print('neg y go')
                go_heading = 180 * np.sign(tan_dir) - tan_dir
            else:
                print('pos y go')
                go_heading = tan_dir
            #go_heading = (abs(go_heading) - 90)* np.sign(go_heading)
        except:
            go_heading = 0
        print('go_heading: ' + str(go_heading))
        print('')

        if abs(go_heading) <= 5:
            msg.linear.x = 0.2
        msg.angular.z = 0.2 * np.sign(go_heading)
        self.vel_pub.publish(msg)
        
        #print(self.processed_scan)
        

    def process_scan(self, msg):
        self.scan = msg.ranges


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
