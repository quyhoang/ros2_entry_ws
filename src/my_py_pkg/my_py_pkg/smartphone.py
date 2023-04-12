#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# use the same data type as that of publisher
from example_interfaces.msg import String


class MyNode(Node):
    def __init__(self):
        super().__init__("smartphone")
        # same data type and topic name as publisher
        self.subscriber_ = self.create_subscription(
            String, "robot_news", self.callback_robot_news, 10)
        self.get_logger().info("Smartphone on")

    def callback_robot_news(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
