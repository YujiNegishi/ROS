#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32



def cb(message):
    global n
    #n = rospy.loginfo(message.data*2)
    n = message.data*2

if __name__ == '__main__': 
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    pub = rospy.Publisher('twice', Int32, queue_size=1) 
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
	n = int(raw_input())
        pub.publish(n)
        rate.sleep()
