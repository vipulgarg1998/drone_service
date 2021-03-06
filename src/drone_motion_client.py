#!/usr/bin/env python

import sys
import rospy
from drone_service.srv import *
from std_msgs.msg import Empty

def moveDrone():
    rospy.wait_for_service('my_service')
    try:
        print("callback")
        rosClient = rospy.ServiceProxy('my_service', MyService)
        response = rosClient()
        return True
    except rospy.ServiceException as e:
        print("exception")
        return False

if __name__ == "__main__":
    rospy.init_node("drone_motion_client")
    moveDrone()
    # if(moveDrone()):
    #     print("Objected Accomplished")
    # else:
    #     print("Objective Failed")