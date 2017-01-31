#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import math
import numpy as np
import cv2

def cb(message):
   　
    global n
    rate = 3.14
    n = message.data
    area = (n*n)*rate
    cir = (2*n)*rate
    
    print 'radius'
    print n
    print 'area'
    print area
    print 'circumference'
    print cir
    print '-------------------------------'
    img = cv2.imread("cblue.png", 1)
    height = img.shape[0]
    width = img.shape[1]
    
    cv2.circle(img, (width/2, height/2), n, (0, 0, 255), 4)
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.imshow("img", img)
    cv2.waitKey(0)    
    cv2.destroyAllWindows()

if __name__ == '__main__': 

    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    rospy.spin()
