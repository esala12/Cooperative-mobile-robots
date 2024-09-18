cmake_minimum_required(VERSION 3.0.2)
project(slavebot_navigation)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  nav_msgs
  move_base_msgs
  actionlib_msgs
)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS geometry_msgs nav_msgs actionlib_msgs move_base_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/navigate_goal.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)