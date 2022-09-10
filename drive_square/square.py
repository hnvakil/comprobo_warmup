import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

#import rospy

class SquareNode(Node):
    def __init__(self):
        super().__init__('square')
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        #now = SquareNode.get_clock().now()

    def run_loop(self):
        msg = Twist()
        msg.linear.x = 0.5
        self.vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SquareNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()