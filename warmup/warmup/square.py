import time,rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

#import rospy
float start_time, current_time

class SquareNode(Node):
    def __init__(self):
        super().__init__('square')
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        start_time = time.perf_counter
        

    def rotate_neato(self):
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0.5
        self.vel_pub.publish(msg)
        time.sleep(2)


    def run_loop(self):
        msg = Twist()

        if((start_time - current_time) < 1000):
            msg.linear.y = 0.5
            msg.angular.z = 0
        else:
            rotate_neato()
            start_time = time.perf_counter

        self.vel_pub.publish(msg)
        current_time = time.perf_counter

        

def main(args=None):
    rclpy.init(args=args)
    node = SquareNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()