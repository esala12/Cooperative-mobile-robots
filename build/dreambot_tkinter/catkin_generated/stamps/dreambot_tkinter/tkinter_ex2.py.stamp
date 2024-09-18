#!/usr/bin/env python3

from tkinter import *
import rospy

def Button_widget():
     myButton = Button(root, text="Click Me!", padx=50, pady=50)
     myButton.pack()

if __name__ == '__main__':
     rospy.init_node('tkinter_ex2', anonymous=True)
     root = Tk()
     Button_widget()
     root.mainloop()
     rospy.spin()