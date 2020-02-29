#!/usr/bin/env python
import rospy
import time

from geometry_msgs.msg import Twist
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, LaserScan
from ar_track_alvar_msgs.msg import AlvarMarkers
import laser_geometry.laser_geometry as lg
import math

class Robot:
        def __init__(self):
                self.mvmt_msg = Twist()
		self.depthSub = rospy.Subscriber("ar_pose_marker", AlvarMarkers, self.updateDepth)
                self.cmd_vel = rospy.Publisher("cmd_vel", Twist, queue_size=0)
		self.l1 = 0 # Distance from robot to landmark 1. 
		self.l2 = 0 # Distance from robot to landmark 2. 
		rospy.sleep(2)
        
	def start(self):
                while not rospy.is_shutdown():
                        rospy.spin()
			# self.cmd_vel.publish(self.mvmt_msg)
			rospy.sleep(2)

	def updateDepth(self, msg):
		if len(msg.markers) != 0:
			for marker in msg.markers:
				if marker.id == 0: # AR tag 1
					self.l1 = marker.pose.pose.position.x
					print("l1: ", self.l1)
				if marker.id == 1: # AR tag 2
					self.l2 = marker.pose.pose.position.x
					print("l2: ", self.l2)

if __name__ == '__main__':
	rospy.init_node('CONTROLLER')
	r = Robot()
	print("robot node is successfully running")
	r.start()
