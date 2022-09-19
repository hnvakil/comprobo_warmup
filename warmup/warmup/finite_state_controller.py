import rclpy
import tty
import select
import sys
import termios
import TeleopNode, SquareNode
from rclpy.node import Node
from geometry_msgs.msg import Twist

#import rospy

class FiniteStateController(Node):
    settings = termios.tcgetattr(sys.stdin)
    key = "a"
    def __init__(self):
        super().__init__('finite_state_controller')
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
        if input == "0":
            msg.linear.x = 0.0
            directions += " stop"
        elif input == "1":
            TeleopNode()
            directions += " tele"
        elif input == "2":
            SquareNode()
            directions += "squre"
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
    node = FiniteStateController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()