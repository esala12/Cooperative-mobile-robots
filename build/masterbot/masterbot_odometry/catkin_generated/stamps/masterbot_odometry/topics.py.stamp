#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math

def publish_sine():
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        # Calculate sine value
        sin_value = math.sin(rospy.get_time())

        # Publish sine value
        sine.publish(Float64(sin_value))
        
        rate.sleep()

if __name__ == '__main__':
    
     rospy.init_node('topics_node')
     sine = rospy.Publisher("/sine", Float64, queue_size=1)
     
     publish_sine()
     
   
