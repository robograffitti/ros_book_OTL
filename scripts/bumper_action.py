#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
import actionlib
from ros_book_OTL.msg import GoUntilBumperAction
from ros_book_OTL.msg import GoUntilBumperResult
from ros_book_OTL.msg import GoUntilBumperFeedback

class BumperAction(object):
    def __init__(self):
        self._pub = rospy.Publisher('/mobile_base/commands/velocity', Twist)
        self._sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent,
                                     self.bumper_callback, queue_size=1)
        self._max_vel = 
