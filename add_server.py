#!/usr/bin/env python

from lab.srv import AddTwooInts,AddTwoIntResponse
from random import random
import rospy

def handle_add_two_ints(random):
    print int(random()*10+1)
    print "Returning [%s,%s,%s,%s]"%(random)
    return AddTwoIntsResponse(random)

def add_two_ints_srver():
    rospy.init_node('add_server')
    s = rospy.Service('add_two_ints', AddTwooInts, handle_add_twoo_ints)
    print "Ready to add twoo inst."
    rospy.spin

if __name__ == "__main__":
    add_server()


