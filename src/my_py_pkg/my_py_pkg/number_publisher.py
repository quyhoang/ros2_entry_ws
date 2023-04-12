#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

class MyNode(Node):
    def __init__(self):
            super().__init__("numberPublisher")
            self.publisher_ = self.create_publisher(Int64, "number", 10)
            self.number = 3
            self.timer_ = self.create_timer(0.5, self.publishNumber)
            self.get_logger().info("numberPuslisher started")
            
    def publishNumber(self):
         msg = Int64()
         msg.data = self.number
         self.publisher_.publish(msg)
         #self.get_logger().info(str(self.counter_) + " and counting")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
