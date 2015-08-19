#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty
from std_srvs.srv import EmptyResponse

def handle_service(req): # req is defined in rospy
    rospy.loginfo('called!')
    return EmptyResponse() # Response for Request

def service_server():
    rospy.init_node('service_server')
    s = rospy.Service('call_me', Empty, handle_service)
    print "Ready to serve."
    rospy.spin()

if __name__ == '__main__': # main function
    service_server() # defined above
