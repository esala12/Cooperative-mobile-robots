# src/path_publisher.py
#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

def publish_path():
    rospy.init_node('path_publisher', anonymous=True)
    path_pub = rospy.Publisher('custom_path', Path, queue_size=10)

    path = Path()
    path.header.frame_id = "map"

    # Create a custom path with some example poses
    for i in range(15):
        pose = PoseStamped()
        pose.header.frame_id = "map"
        pose.header.stamp = rospy.Time.now()
        if i<=10:
            pose.pose.position.x = i * 0.5
            pose.pose.position.y = 0.0
            #pose.pose.orientation.w = 1.0
        if i>10:
            pose.pose.position.x = 10*0.5
            pose.pose.position.y = i*0.5
        path.poses.append(pose)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        path.header.stamp = rospy.Time.now()
        path_pub.publish(path)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_path()
    except rospy.ROSInterruptException:
        pass
