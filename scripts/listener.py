#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(message): # message is found from the name 'chatte' by rospy
    rospy.loginfo("I heard %s", message.data)

rospy.init_node('listener')
sub = rospy.Subscriber('chatter', String, callback)
rospy.spin()
