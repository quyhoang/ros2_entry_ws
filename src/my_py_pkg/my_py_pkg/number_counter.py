#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# use the same data type as that of publisher
from example_interfaces.msg import Int64



class MyNode(Node):
    def __init__(self):
        super().__init__("numberCounter")
        self.counter = 0
        # same data type and topic name as publisher
        self.subscriber_ = self.create_subscription(
            Int64, "number", self.callback, 10)
        
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)

        self.get_logger().info("numberCounter on")

    def callback(self, msg):
        msgPub = Int64()
        self.counter += msg.data
        msgPub.data = self.counter
        self.publisher_.publish(msgPub) 
        #print(msgPub.data)
        self.get_logger().info(str(msgPub.data))


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()


# #!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node

# from example_interfaces.msg import Int64


# class counterNumber(Node):
#     def __init__(self):
#         super().__init__("numberCounter")
#         # same data type and topic name as publisher
#         self.subscriber_ = self.create_subscription(
#             Int64, "number", self.callback, 10)
#         self.get_logger().info("numberCounter on")

#         #self.publisher_ = self.create_publisher(Int64, "number_count", 10)

#     def callback(self, msg):
#         self.get_logger().info(msg.data)
#         #msgPub = Int64()
#         #msgPub.data += msg.data
#         #msgPub.data += 3
#         #self.publisher_.publish(msgPub) 



# def main(args=None):
#     rclpy.init(args=args)
#     node = counterNumber()
#     rclpy.spin(node)
#     rclpy.shutdown()


if __name__ == "__main__":
    main()
