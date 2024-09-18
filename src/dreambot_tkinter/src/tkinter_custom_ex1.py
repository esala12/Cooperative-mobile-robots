#!/usr/bin/env python3

from tkinter import *
import customtkinter
import rospy

class CustomTkinterApp:
    def __init__(self):
        rospy.init_node('tkinter_custom_ex1', anonymous=True)
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.root = customtkinter.CTk()
        self.root.title('Tkinter.com - Custom Tkinter!')
        self.root.geometry('600x350')

        self.my_button = customtkinter.CTkButton(self.root,
                                                  text="Hello World!!", 
                                                  height=100,
                                                  width=200,
                                                  text_color="black",
                                                  font=("Helvetica", 24),
                                                  fg_color='red',
                                                  hover_color='green',
                                                  corner_radius=50,
                                                  bg_color='white',
                                                  border_width=10,
                                                  command=self.hello)
        self.my_button.pack(pady=80)

        self.my_label = customtkinter.CTkLabel(self.root, text="")
        self.my_label.pack(pady=20)

    def hello(self):
        self.my_label.configure(text=self.my_button.cget("text"))

    def run(self):
        self.root.mainloop()
        rospy.spin()

if __name__ == '__main__':
    app = CustomTkinterApp()
    app.run()
