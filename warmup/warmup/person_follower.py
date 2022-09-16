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

class PersonFollowerNode(Node):
    #states:
    # 0: looking for person
    # 1: approaching person
    # 2: 
    def __init__(self):
        super().__init__('person_follower')
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_subscription(LaserScan, 'stable_scan', self.process_scan, 10)
        self.scan = None
        self.goal_dist = 0.75
        self.state = 0
        self.person_imprinted = False


    def get_nearest_point_angle(self, center_angle, angle_range):
        '''
        angle range is to either side
        '''
        if self.scan is None:
            return 0, self.goal_dist
        for reading in range(len(self.scan)):
            if self.scan[reading] == 0.0:
                self.scan[reading] = math.inf
        #print(self.scan)
        doubled_scan = np.concatenate([self.scan, self.scan])
        start_index = center_angle + 360 - angle_range
        end_index = center_angle + 360 + angle_range
        scan_range = doubled_scan[start_index:end_index+1]
        try:
            nearest_dist = min(scan_range)
        except:
            return 0, self.goal_dist + 1

        nearest_point_angle = self.scan.index(nearest_dist)
        return nearest_point_angle, nearest_dist
    
    def get_nearest_point(self):
        return self.get_nearest_point_angle(0, 180)
    


    def run_loop(self):
        msg = Twist()
        # run scan

        # find min dist and heading
        
                
        min_dist_heading, min_dist = self.get_nearest_point()
        print("Min dist: " + str(min_dist) + " of type: " + str(type(min_dist)))
        print("Min dist heading: " + str(min_dist_heading) + " of type: " + str(type(min_dist_heading)))

        dir = -1 
        if min_dist_heading < 180: #pos dir is ccw turn which turns left
            dir = 1

        if min_dist_heading <180:
            msg.angular.z = abs(min_dist_heading) * dir / 180
        else:
            msg.angular.z = abs(min_dist_heading - 360) * dir / 180

        msg.angular.z = 0.2 * dir

        if (min_dist_heading <= 3 or min_dist_heading >=357):
            msg.angular.z = 0.0
            if min_dist > self.goal_dist:
                msg.linear.x = 0.2
            else:
                msg.linear.x = 0.0

            msg.angular.z = 0.0
        
        self.vel_pub.publish(msg)



        # check current state
        # check sensor data
        # change to next state
        
    

    def process_scan(self, msg):
        self.scan = msg.ranges
    
    





def main(args=None):
    rclpy.init(args=args)
    node = PersonFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
