import rclpy
import time
import math
import tty
import select
import sys
import termios
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WallFollowerNode(Node):
    def __init__(self):
        super().__init__('wall_follower')
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_subscription(LaserScan, 'stable_scan', self.process_scan, 10)
        self.scan = [0]


    def run_loop(self):
        msg = Twist()
        # run scan

        # find min dist and heading
        print(self.scan)
        min_dist = min(self.scan)
        min_dist_heading = self.scan.index(min_dist)
        print("Min dist: " + str(min_dist) + " of type: " + str(type(min_dist)))
        print("Min dist heading: " + str(min_dist_heading) + " of type: " + str(type(min_dist_heading)))

        #if heading less than 180, turn left else right
        dir = -1 
        if min_dist_heading > 90: #pos dir is ccw turn which turns left
            dir = 1
        
        msg.angular.z = abs(min_dist_heading - 90) * dir / 180
        


        #if heading within margin of error drive forward
        if abs(min_dist_heading - 90) <=1:
            print('going')
            msg.linear.x = 0.2
        self.vel_pub.publish(msg)
        time.sleep(0.1)
        

    def process_scan(self, msg):
        self.scan = msg.ranges






def main(args=None):
    rclpy.init(args=args)
    node = WallFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
