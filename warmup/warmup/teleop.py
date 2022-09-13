import rclpy
import tty
import select
import sys
import termios
from rclpy.node import Node
from geometry_msgs.msg import Twist

#import rospy

class TeleopNode(Node):
    settings = termios.tcgetattr(sys.stdin)
    key = "a"
    def __init__(self):
        super().__init__('teleop')
        self.create_timer(0.1, self.run_loop)
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        
    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def process_input(self, input):
        msg = Twist()
        directions = ""
        if input == "w":
            msg.linear.x = 0.5
            directions += " forward"
        elif input == "s":
            msg.linear.x = -0.5
            directions += " backward"
        if input == "a":
            msg.angular.z = 0.5
            directions += " left"
        elif input == "d":
            msg.angular.z = -0.5
            directions += " right"
        self.vel_pub.publish(msg)
        return directions
        


    def run_loop(self):        
        if self.key != '\x03':
            key = self.getKey()
        directions = self.process_input(key)
        print("Key pressed: " + key)
        print(directions)
        

    
    """
    while key != '\x03':
        key = getKey()
        printout = "key pressed: " + key
        print(printout)
        """

def main(args=None):
    rclpy.init(args=args)
    node = TeleopNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()