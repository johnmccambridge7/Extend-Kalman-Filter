#!/usr/bin/env python
import rospy
import time

from geometry_msgs.msg import Twist

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '100')
Config.set('graphics', 'height', '100')

class ControlScreen(GridLayout):
	def __init__(self, **kwargs):
		super(ControlScreen, self).__init__(**kwargs)
		self.cols = 2

		forwardBtn = Button(text='F')
		forwardBtn.bind(on_press=self.move)
		forwardBtn.bind(on_release=self.stop_movement)

		backwardBtn = Button(text='B')
		backwardBtn.bind(on_press=self.move)
                backwardBtn.bind(on_release=self.stop_movement)


		leftBtn = Button(text='L')
		leftBtn.bind(on_press=self.move)
                leftBtn.bind(on_release=self.stop_movement)

		rightBtn = Button(text='R')
		rightBtn.bind(on_press=self.move)
                rightBtn.bind(on_release=self.stop_movement)

		self.add_widget(forwardBtn)
		self.add_widget(backwardBtn)
		self.add_widget(leftBtn)
		self.add_widget(rightBtn)

		# code for controlling robot
		self.mvmt_msg = Twist()
		self.cmd_vel = rospy.Publisher("/cmd_vel", Twist, queue_size=0)
		rospy.sleep(2)

		# robot = Robot()
		# robot.start()

	def stop_movement(self, button):
		print("Sending null value to cmd_vel...")
		self.mvmt_msg.linear.x = 0
		self.mvmt_msg.angular.z = 0
		self.cmd_vel.publish(self.mvmt_msg)

	def move(self, button):
		direction = button.text

		VELOCITY = 0.25

		if direction == "F":
			self.mvmt_msg.linear.x = VELOCITY
			self.cmd_vel.publish(self.mvmt_msg)
			# self.robot.forward()
			print("Moving forward...")
		elif direction == "B":
			self.mvmt_msg.linear.x = -1 * VELOCITY
                        self.cmd_vel.publish(self.mvmt_msg)
			print("Moving backward...")
		elif direction == "L":
			self.mvmt_msg.linear.x = VELOCITY
			self.mvmt_msg.angular.z = 5 * VELOCITY
                        self.cmd_vel.publish(self.mvmt_msg)
			print("Moving left...")
		elif direction == "R":
			self.mvmt_msg.linear.x = VELOCITY
			self.mvmt_msg.angular.z = -5 * VELOCITY
                       	self.cmd_vel.publish(self.mvmt_msg)
			print("Moving right")


class MyApp(App):
	def build(self):
		self.title = 'ROS-bot controller - John McCambridge'
		return ControlScreen()

if __name__ == '__main__':
	rospy.init_node('ROBOT_CONTROLLER')
	MyApp().run()
