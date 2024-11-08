cmake_minimum_required(VERSION 3.0.2)
project(dreambot_data)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  nav_msgs
)

## Generate messages in the 'msg' folder
generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs 
  nav_msgs
)

catkin_package(
  # Add any necessary include directories or libraries here
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/cmd_csv.py
  src/distance.py
  src/master_path.py
  src/slave_path.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
