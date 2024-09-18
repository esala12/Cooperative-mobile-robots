#!/usr/bin/env python3

from tkinter import *
import rospy

def Hello_widget():
     myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
     myLabel2 = Label(root, text="My Name is Esala").grid(row=1, column=5)
     
     # myLabel1.grid(row=0, column=0)
     # myLabel2.grid(row=1, column=5)

if __name__ == '__main__':
     rospy.init_node('tkinter_ex1', anonymous=True)
     root = Tk()
     Hello_widget()
     root.mainloop()
     rospy.spin()