# Install script for directory: /home/esala/dreambot_ws/src/masterbot/masterbot_odometry

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/esala/dreambot_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/masterbot_odometry.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/masterbot_odometry/cmake" TYPE FILE FILES
    "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/masterbot_odometryConfig.cmake"
    "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/masterbot_odometryConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/masterbot_odometry" TYPE FILE FILES "/home/esala/dreambot_ws/src/masterbot/masterbot_odometry/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/tf_masterbot.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/imu_republisher_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/masterbotpid.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/masterbot_pidtuner.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/topics.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/enc_republisher_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/tf_republisher_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/kalman_filter.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/tf_kalman_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/master_tf_cal.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/masterbot_odometry" TYPE PROGRAM FILES "/home/esala/dreambot_ws/build/masterbot/masterbot_odometry/catkin_generated/installspace/kalman_filter_real.py")
endif()

