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

class WallFollowerNode(Node):
    def __init__(self):
        super().__init__('wall_follower')
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_subscription(LaserScan, 'stable_scan', self.process_scan, 10)
        self.scan = [0]


    def get_nearest_point_angle(self, center_angle, angle_range):
        '''
        angle range is to either side
        '''
        if self.scan is None:
            return 0, self.goal_dist
        #print(self.scan)
        doubled_scan = np.concatenate([self.scan, self.scan])
        for reading in range(len(doubled_scan)):
            if doubled_scan[reading] == 0.0:
                doubled_scan[reading] = 200
        start_index = center_angle + 360 - angle_range
        end_index = center_angle + 360 + angle_range
        scan_range = doubled_scan[start_index:end_index+1]
        try:
            nearest_dist = min(scan_range)
        except:
            return 0, 200 + 1

        nearest_point_angle = self.scan.index(nearest_dist)
        return nearest_point_angle, nearest_dist
    
    def get_nearest_point(self):
        return self.get_nearest_point_angle(0, 180)
    
    
    def run_loop(self):
        msg = Twist()
        # run scan

        # find min dist and heading
        min_dist, min_dist_heading = self.get_nearest_point()
        print("Min dist: " + str(min_dist) + " of type: " + str(type(min_dist)))
        print("Min dist heading: " + str(min_dist_heading) + " of type: " + str(type(min_dist_heading)))


        #if heading less than 180, turn left else right
        dir = -1 
        if min_dist_heading > 90: #pos dir is ccw turn which turns left
            dir = 1
        
        msg.angular.z = abs(min_dist_heading - 90) * dir / 180 /10
        


        #if heading within margin of error drive forward
        if abs(min_dist_heading - 90) <=5:
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
