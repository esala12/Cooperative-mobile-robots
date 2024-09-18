cmake_minimum_required(VERSION 3.0.2)
project(masterbot_navigation)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  nav_msgs
  move_base_msgs
  actionlib_msgs
  std_srvs
)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS geometry_msgs nav_msgs actionlib_msgs move_base_msgs std_srvs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/path_generate.py
  src/pose_subscriber.py
  src/navigate_goal.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
