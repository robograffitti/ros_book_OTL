#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
import actionlib
from ros_book_OTL.msg import GoUntilBumperAction # Spec
from ros_book_OTL.msg import GoUntilBumperResult # Resultp
from ros_book_OTL.msg import GoUntilBumperFeedback # Progress check

class BumperAction(object): # inherit class object
    def __init__(self): # initializer / constructor
        self._pub = rospy.Publisher('/mobile_base/commands/velocity', Twist)
        self._sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent,
                                     self.bumper_callback, queue_size=1)
        self._max_vel = rospy.get_param('~max_vel', 2.5) # parameter
        self._action_server = actionlib.SimpleActionServer('bumper_action', GoUntilBumperAction,
                                                           execute_cb=self.go_until_bumper,
                                                           auto_start=False)
        self._hit_bumper = False # set default value for parameter
        self._action_server.start()

    def bumper_callback(self, bumper): # bumper is defined in BumperEvent
        self._hit_bumper = True

    def go_until_bumper(self, goal): # goal is object to access the Spec value of GoUntilBumper.action
        print(goal.target_vel)
        r = rospy.Rate(10.0)
        zero_vel = Twist()
        for i in range(10 * goal.timeout_sec): # Rate * timeout_sec
            if self._action_server.is_preempt_requested(): # check preemption request
                self._action_server.set_preempted()
                break
            if self._hit_bumper:
                self._pub.publish(zero_vel)
                break
            else:
                if goal.target_vel.linear.x > self._max_vel:
                    goal.target_vel.linear.x = self._max_vel
                self._pub.publish(goal.target_vel)
                feedback = GoUntilBumperFeedback(current_vel=goal.target_vel) # set feedback value
                self._action_server.publish_feedback(feedback)
            r.sleep()
        result = GoUntilBumperResult(bumper_hit=self._hit_bumper)
        self._action_server.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('bumper_action')
    bumper_action = BumperAction()
    rospy.spin()
