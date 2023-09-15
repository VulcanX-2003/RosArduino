#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8


def control():

    pub = rospy.Publisher('chatter',Int8, queue_size=10)
    
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        senddata = 4
        rospy.loginfo("Sending 4")
        pub.publish(senddata)
        rospy.loginfo("Sent 4")
        rate.sleep()

if __name__ == "__main__" :
    rospy.init_node('talker', anonymous=True)
    control()
    




    