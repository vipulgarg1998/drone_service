#!/usr/bin/env python

from __future__ import print_function

from drone_service.srv import *
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import rospy

def moveDrone(req):
    takeOffPub = rospy.Publisher('/drone/takeoff', Empty, queue_size=10)
    movePub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    landPub = rospy.Publisher('/drone/land', Empty, queue_size=10)
    move_cmd = Twist()
    move_cmd.linear.x = 1.0
    takeOffPub.publish()
    rospy.sleep(2)
    movePub.publish(move_cmd)
    rospy.sleep(5)
    move_cmd.linear.x = 0.0
    movePub.publish(move_cmd)
    landPub.publish()
    rospy.sleep(2)
    return Empty()

def moveDroneServer():
    rospy.init_node('drone_service')
    s = rospy.Service('/my_service', MyService, moveDrone)
    print("Moving Drone")
    rospy.spin()

if __name__ == "__main__":
    moveDroneServer()