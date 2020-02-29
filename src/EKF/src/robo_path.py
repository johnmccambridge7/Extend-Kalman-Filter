import rospy
from geometry_msgs.msg import Twist
	
# global publisher for functions
publisher = rospy.Publisher("cmd_vel", Twist, queue_size=0)

def init():
	rospy.init_node("draw_d_node")
	
def rotate(angle, clockwise):
# rotate "angle" degrees counter-clockwise/clockwise (True for clockwise)
	vel_msg = Twist()
	ang_spd = 1.25
	rel_ang = angle*3.14159262/180
	
	if clockwise:
		vel_msg.angular.z = -ang_spd
		vel_msg.linear.x = 0.25
	else:
		vel_msg.angular.z = ang_spd
		vel_msg.linear.x = 0.25
	
	# get time to determine distance
	start = rospy.Time.now().to_sec()
	curr_ang = 0
	
	while (curr_ang < rel_ang):
		publisher.publish(vel_msg)
		t = rospy.Time.now().to_sec()
		curr_ang = ang_spd*(t-start)
	
	# stop rotation
	vel_msg.angular.z = 0
	publisher.publish(vel_msg)
	
def move_forward(distance):
	# move forward "distance"
	rate = rospy.Rate(1)
	vel_msg = Twist()
	vel_msg.linear.x = 0.3
	
	# get time to determine distance
	init_time = rospy.Time.now().to_sec()
	curr_dist = 0
	
	while (curr_dist < distance):
		publisher.publish(vel_msg)
		up_time = rospy.Time.now().to_sec()
		curr_dist = (up_time - init_time) * 0.3
		rate.sleep()
	
	# stop moving
	vel_msg.linear.x = 0
	publisher.publish(vel_msg)
	curr_dist = 0

def move_back(distance):
	# move forward "distance"
	rate = rospy.Rate(1)
	vel_msg = Twist()
	vel_msg.linear.x = -0.3
	
	# get time to determine distance
	init_time = rospy.Time.now().to_sec()
	curr_dist = 0
	
	while (curr_dist < distance):
		publisher.publish(vel_msg)
		up_time = rospy.Time.now().to_sec()
		curr_dist = (up_time - init_time) * 0.3
		rate.sleep()
	
	# stop moving
	vel_msg.linear.x = 0
	publisher.publish(vel_msg)
	curr_dist = 0

if __name__ == "__main__":
	init()
	
	rospy.sleep(3)
	move_forward(0.4)
	
	rospy.sleep(3)
	rotate(3, True)
	
	rospy.sleep(3)
	#move_forward(0.2)
	
	rospy.sleep(3)
	rotate(5, False)
	
	rospy.sleep(3)
	#move_forward(0.1)
	
	rospy.sleep(3)
	rotate(3, True)
	
	rospy.sleep(3)
	move_back(0.8)

	rospy.sleep(3)
