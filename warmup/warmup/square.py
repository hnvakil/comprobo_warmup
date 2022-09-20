import time,rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

#import rospy


class SquareNode(Node):    
    
    start_time = float(0)
    current_time = float(0)

    def __init__(self):
        super().__init__('square')
        self.start_time = int(time.perf_counter())
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        

    def rotate_neato(self, msg):
        msg.linear.x = 0.0
        msg.angular.z = 3.14159/4
        self.vel_pub.publish(msg)
        time.sleep(2)


    def run_loop(self):
        self.current_time = int(time.perf_counter())
        print("current time: " + str(self.current_time))
        print("start time: " + str(self.start_time))
        msg = Twist()

        if((self.current_time - self.start_time) < 2):
            msg.linear.x = 0.25
            msg.angular.z = 0.0
        else:
            self.rotate_neato(msg)
            self.start_time = int(time.perf_counter())

        self.vel_pub.publish(msg)
        

def main(args=None):
    global start_time 
    global current_time

    rclpy.init(args=args)
    node = SquareNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()