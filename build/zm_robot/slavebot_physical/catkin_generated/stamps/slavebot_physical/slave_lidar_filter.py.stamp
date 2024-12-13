import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

class LaserScanFilter:
    def __init__(self):
        rospy.init_node('laser_scan_filter', anonymous=True)
        
        # Subscribe to the /scan topic
        self.scan_subscriber = rospy.Subscriber(
            '/lidar_slave/scan',
            LaserScan,
            self.scan_callback
        )

        # Publisher for the filtered scan data
        self.filtered_scan_publisher = rospy.Publisher(
            '/filtered_scan_slave',
            LaserScan,
            queue_size=10
        )

        # Define the angle ranges to filter out (in radians) for each of the four corners
        self.filter_ranges = [
            (np.deg2rad(38), np.deg2rad(48)),      
            (np.deg2rad(129), np.deg2rad(141)),
            (np.deg2rad(-141), np.deg2rad(-131)),
            (np.deg2rad(-50), np.deg2rad(-37))
            # (np.deg2rad(-55), np.deg2rad(-35)),   
            # (np.deg2rad(35), np.deg2rad(55)),
            # (np.deg2rad(130), np.deg2rad(140)),
            # (np.deg2rad(-140), np.deg2rad(-130))
        ]

    def scan_callback(self, msg):
        # Filter out specific angle ranges
        filtered_ranges = list(msg.ranges)  # Start with the original ranges

        angle_increment = msg.angle_increment
        current_angle = msg.angle_min

        for i in range(len(msg.ranges)):
            # Check if the current angle falls within any of the specified ranges
            if any(
                start <= current_angle <= end if start < end else start <= current_angle or current_angle <= end
                for start, end in self.filter_ranges
            ):
                # Set the distance to infinity for angles we want to filter out
                filtered_ranges[i] = float('inf')
            current_angle += angle_increment

        # Create a new LaserScan message for the filtered data
        filtered_scan = LaserScan()
        filtered_scan.header = msg.header
        filtered_scan.angle_min = msg.angle_min
        filtered_scan.angle_max = msg.angle_max
        filtered_scan.angle_increment = msg.angle_increment
        filtered_scan.time_increment = msg.time_increment
        filtered_scan.scan_time = msg.scan_time
        filtered_scan.range_min = msg.range_min
        filtered_scan.range_max = msg.range_max
        filtered_scan.ranges = filtered_ranges

        # Publish the filtered scan data
        self.filtered_scan_publisher.publish(filtered_scan)
        

def main():
    laser_scan_filter = LaserScanFilter()
    rospy.spin()

if __name__ == '__main__':
    main()
