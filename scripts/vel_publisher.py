#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('vel_publisher')
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
# rate = rospy.Rate(30) # 30Hz
while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_input('f: forward, b: backward, l: left, r: right > ') # wait until pressing Enter
    if 'f' in direction:
        vel.linear.x = 0.5
    if 'b' in direction:
        vel.linear.x = -0.5
    if 'l' in direction:
        vel.angular.z = 1.0
    if 'r' in direction:
        vel.angular.z = -1.0
    if 'q' in direction:
        break
    print vel
    pub.publish(vel)
    # rate.sleep()
