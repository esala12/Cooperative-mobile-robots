#!/usr/bin/env python3

from tkinter import *
import customtkinter
import rospy

class CustomTkinterApp:
     def __init__(self):
          rospy.init_node('tkinter_custom_ex3', anonymous=True)
          
          customtkinter.set_appearance_mode("dark")
          customtkinter.set_default_color_theme("blue")

          self.root = customtkinter.CTk()
          self.root.title('Tkinter.com - Custom Tkinter!')
          self.root.geometry('600x350')

          self.check_var = customtkinter.StringVar(value="off")
          self.my_check = customtkinter.CTkCheckBox(self.root, text="Would you like to play a game",
                                                variable=self.check_var,
                                                onvalue="on",
                                                offvalue="off")
          self.my_check.pack(pady = 40)
          


     def run(self):
          self.root.mainloop()
          rospy.spin()

if __name__ == '__main__':
    app = CustomTkinterApp()
    app.run()
