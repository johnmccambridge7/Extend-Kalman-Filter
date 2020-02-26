#!/usr/bin/env python
import rospy
import time

from geometry_msgs.msg import Twist


class Robot:
        def __init__(self):

                self.mvmt_msg = Twist()
                self.cmd_vel = rospy.Publisher("/cmd_vel", Twist, queue_size=0)
                rospy.sleep(2)

        def forward(self):
                self.mvmt_msg.linear.x = 1.0

        def backward(self):
                self.mvmt_msg.linear.x = -1.0

        def left(self):
                self.mvmt_msg.angular.z = 1.0

        def right(self):
                self.mvmt_msg.angular.z = -1.0

        def stop(self):
                self.mvmt_msg.angular.z = 0.0
                self.mvmt_msg.linear.x = 0.0

        def start(self):
                while not rospy.is_shutdown():
                        self.cmd_vel.publish(self.mvmt_msg)
                        rospy.sleep(2)


if __name__ == '__main__':
	rospy.init_node('CONTROLLER')
	r = Robot()
	r.start()
