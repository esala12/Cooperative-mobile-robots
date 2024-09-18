cmake_minimum_required(VERSION 3.0.2)
project(masterbot_fuzzy)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  nav_msgs
  geometry_msgs
)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS geometry_msgs nav_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/fuzzy_matlab.py
  src/fuzzy_wavepoints.py
  src/fuzzy_continous.py
  src/path_generator.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
