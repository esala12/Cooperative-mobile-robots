#!/usr/bin/env python3

import rospy
from dreambot.srv import PathRequest
from tkinter import Tk, Button
import threading

def send_path_request(path_name):
    # Function to handle the service call in a separate thread
    try:
        rospy.wait_for_service('path_selection_service', timeout=5)
        path_service = rospy.ServiceProxy('path_selection_service', PathRequest)
        response = path_service(path_name)
        rospy.loginfo(f"Response: {response.message}")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
    except rospy.ROSException as e:
        rospy.logerr(f"Timeout waiting for service: {e}")

def on_button_press(path_name):
    rospy.loginfo(f"Button pressed: {path_name}")
    # Run the service call in a separate thread
    threading.Thread(target=send_path_request, args=(path_name,)).start()

def main():
    rospy.init_node('path_client', anonymous=True)
    root = Tk()
    root.title("Path Selector")

    # Create buttons for selecting paths
    Button(root, text="Path 1", command=lambda: on_button_press("path1")).pack()
    Button(root, text="Path 2", command=lambda: on_button_press("path2")).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
