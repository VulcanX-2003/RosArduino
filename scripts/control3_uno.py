def control():

    pub = rospy.Publisher('chatter',Int8, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) 
    
    while not rospy.is_shutdown():
        senddata = key_input()
        if(senddata==1):
            rospy.loginfo("Forward")
        if(senddata==2):
            rospy.loginfo("Backward")
        if(senddata==3):
            rospy.loginfo("left")
        if(senddata==4):
            rospy.loginfo("Right")
        rospy.loginfo(senddata)
        pub.publish(senddata)
        rate.sleep()

if __name__ == "__main__" :
    control()
