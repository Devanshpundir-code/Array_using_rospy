#!/usr/bin/python3
import rospy
from std_msgs.msg import Float32MultiArray
def funtion():
    rospy.init_node('node23', anonymous=True)
    pub=rospy.Publisher('topic14', Float32MultiArray, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        arr = Float32MultiArray()
        arr.data=[30, 40, 50]
        pub.publish(arr)
        rate.sleep()

if __name__ == '__main__':
    funtion()
    
