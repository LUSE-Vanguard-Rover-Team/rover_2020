#!/usr/bin/python3
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
import rover_msgs.msg

class DriveTeleop(Node):

	def __init__(self):
		super().__init__('drive_teleoperation')
		self.subscription = self.create_subscription(Joy, "joy", self.recv_joy_data, 1)
		self.drive_pub = self.create_publisher(rover_msgs.msg.ODrive, "telop_drive_cmd", 1)
		self.speed_setting = 2

	def recv_joy_data(self, joystick):
		# Set speed setting using D-Pad
		if joystick.axes[6] == 1:
			self.speed_setting = 1
		if joystick.axes[6] == -1:
			self.speed_setting = 2
		if joystick.axes[7] == 1:
			self.speed_setting = 3
		if joystick.axes[7] == -1:
			self.speed_setting = 4

		msg = rover_msgs.msg.ODrive()
		msg.left = -joystick.axes[1] / self.speed_setting
		msg.right = - joystick.axes[4] / self.speed_setting

		msg.reset = joystick.buttons[7]
		msg.fullstop = joystick.buttons[6]

		self.drive_pub.publish(msg)
		
def main(args=None):
	rclpy.init(args=args)
	try:
		controller = DriveTeleop()
		rclpy.spin(controller)
	except:
		pass
	finally:
		controller.get_logger().info("drive_teleoperation node shutdown")
		# Destroy the node explicitly
		# (optional - otherwise it will be done automatically
		# when the garbage collector destroys the node object)
		controller.destroy_node()
		rclpy.shutdown()
	
if __name__ == '__main__':
	main()