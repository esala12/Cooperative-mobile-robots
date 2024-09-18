cmake_minimum_required(VERSION 3.0.2)
project(masterbot_odometry)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  tf2_ros
  geometry_msgs
  sensor_msgs
  nav_msgs
  tf2_msgs
)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS tf2_ros geometry_msgs sensor_msgs nav_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/tf_masterbot.py
  src/imu_republisher_node.py
  src/masterbotpid.py
  src/masterbot_pidtuner.py
  src/topics.py
  src/enc_republisher_node.py
  src/tf_republisher_node.py
  src/kalman_filter.py
  src/tf_kalman_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
