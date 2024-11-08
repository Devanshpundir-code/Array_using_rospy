#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32MultiArray

def callback(val):
    rospy.loginfo('array data receveid %f %f %f' % (val.data[0], val.data[1], val.data[2]))

def funtion():
    rospy.init_node("node24", anonymous=True)
    rospy.Subscriber("topic14", Float32MultiArray,callback)
    rospy.spin()

if __name__ == '__main__':
    funtion()
