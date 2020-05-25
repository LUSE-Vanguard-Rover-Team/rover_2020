#!/usr/bin/python3
import rclpy
from rclpy.node import Node

import odrive
from odrive.enums import *

import rover_msgs.msg

class Odrive(Node):

    def __init__(self, front, rear):
    # def __init__(self, rear):
        super().__init__('odrive_driver')
        self.subscription = self.create_subscription(rover_msgs.msg.ODrive, 'drive_cmd', self.listener_callback, 1)
        self.drive_telemetry_pub = self.create_publisher(rover_msgs.msg.ODriveTelem, "drive_telemetry", 10)
        self.subscription  # prevent unused variable warning
        self.front = front
        self.rear = rear
        self.fullStop()
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = rover_msgs.msg.ODriveTelem()
        msg.front_vol = self.front.vbus_voltage
        msg.back_vol = self.rear.vbus_voltage
        self.drive_telemetry_pub.publish(msg)

    def listener_callback(self, msg):
        self.get_logger().info("Received: " + str(msg))
        if msg.reset == 1:
            self.reset()
        if msg.fullStop == 1:
            self.fullStop()
        self.updateMotorValues(msg)

    def reset(self):
        self.front.axis0.error = 0
        self.front.axis1.error = 0
        self.rear.axis0.error = 0
        self.rear.axis1.error = 0
        self.front.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.front.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.rear.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.rear.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

    def fullStop(self):
        self.front.axis0.controller.vel_setpoint = 0
        self.front.axis1.controller.vel_setpoint = 0
        self.rear.axis0.controller.vel_setpoint = 0
        self.rear.axis1.controller.vel_setpoint = 0

    def updateMotorValues(self, msg):
        self.get_logger().info("left: " + str(msg.left) + ", right: " + str(msg.right))
        self.front.axis0.controller.vel_setpoint = -msg.left
        self.rear.axis0.controller.vel_setpoint = msg.right
        # self.reset()
        self.rear.axis1.controller.vel_setpoint = -msg.left
        self.front.axis1.controller.vel_setpoint = msg.right

def main(args=None):
    try:
        print("Connecting to odrive front...")
        front = odrive.find_any(serial_number="20703882304E")
        print("Connecting to odrive rear...")
        rear = odrive.find_any(serial_number="205F3599524B")
        print("All drives connected")
        rclpy.init(args=args)
        odrive_node = Odrive(front, rear)
        # odrive_node = Odrive(rear)
        rclpy.spin(odrive_node)
    except:
        pass
    finally:
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        odrive_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
