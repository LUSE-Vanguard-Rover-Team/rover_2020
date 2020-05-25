#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import rover_msgs.msg
import time

class ControlMaster(Node):

    def __init__(self):
        super().__init__("control_master")
        self.drive_pub = self.create_publisher(rover_msgs.msg.ODrive, "drive_cmd", 1)
        # self.arm_pub = self.create_publisher(String, "arm_cmd", 10)
        self.telop_drive_sub = self.create_subscription(rover_msgs.msg.ODrive, "telop_drive_cmd", self.telop_drive_cmd, 1)
        # self.telop_arm_sub = self.create_subscription(Joy, "arm_controller_val", self.telop_arm_cmd, 10)
        self.auto_drive_sub = self.create_subscription(rover_msgs.msg.ODrive, "auto_drive_cmd", self.auto_drive_cmd, 1)
        # self.auto_arm_sub = self.create_subscription(String, "auto_arm_cmd", self.auto_arm_cmd, 10)
        self.block_time = 0
        self.telop_time = time.time()

    def telop_drive_cmd(self, msg):
        self.telop_time = time.time()
        self.block_time = 5
        self.get_logger().info("drive_cmd received: " + str(msg))
        self.drive_pub.publish(msg)

    def telop_arm_cmd(self, msg):
        self.telop_time = time.time()
        self.block_time = 5
        self.get_logger().info("telop_arm_cmd received: " + str(msg))

    def auto_drive_cmd(self, msg):
        self.get_logger().info("auto_drive_cmd received: " + str(msg))
        if (time.time() - self.telop_time) >= self.block_time:
            self.block_time = 0
            self.drive_pub.publish(msg)

    def auto_arm_cmd(self, msg):
        self.get_logger().info("auto_arm_cmd received: " + str(msg))
        if (time.time() - self.telop_time) >= self.block_time:
            self.block_time = 0
            # self.arm_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    try:
        control_master = ControlMaster()
        rclpy.spin(control_master)
    except:
        pass
    finally:
        control_master.get_logger().info("control_master node shutdown")
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        control_master.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
