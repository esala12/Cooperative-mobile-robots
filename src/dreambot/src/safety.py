import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool

class LaserScanProcessor:
    def __init__(self):
        rospy.init_node('laser_scan_safety_monitor', anonymous=True)
        self.master_scan_sub = rospy.Subscriber('/filtered_scan_master', LaserScan, self.master_scan_callback)
        self.slave_scan_sub = rospy.Subscriber('/filtered_scan_slave', LaserScan, self.slave_scan_callback)
        self.safety_pub = rospy.Publisher('/safety', Bool, queue_size=10)
        self.master_ranges = []
        self.slave_ranges = []

    def master_scan_callback(self, msg):
        self.master_ranges = msg.ranges
        self.process_scans()

    def slave_scan_callback(self, msg):
        self.slave_ranges = msg.ranges
        self.process_scans()

    def process_scans(self):
        if self.master_ranges and self.slave_ranges:
            # Combine the ranges from both scans filtering out zero values
            combined_ranges = filter(lambda x: x > 0.0, self.master_ranges + self.slave_ranges)
            if combined_ranges:
                min_distance = min(combined_ranges)
                rospy.loginfo(f"Minimum distance: {min_distance} meters")
                
                # Publish safety status based on distance
                safety_status = Bool()
                safety_status.data = min_distance <= 0.60
                self.safety_pub.publish(safety_status)
            else:
                rospy.loginfo("No valid distances received.")
        else:
            rospy.loginfo("Waiting for data from both scans.")

if __name__ == '__main__':
    processor = LaserScanProcessor()
    rospy.spin()
