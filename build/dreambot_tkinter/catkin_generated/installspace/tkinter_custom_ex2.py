#!/usr/bin/env python3

from tkinter import *
import customtkinter
import rospy

class CustomTkinterApp:
     def __init__(self):
          rospy.init_node('tkinter_custom_ex2', anonymous=True)
          
          customtkinter.set_appearance_mode("dark")
          customtkinter.set_default_color_theme("blue")

          self.root = customtkinter.CTk()
          self.root.title('Tkinter.com - Custom Tkinter!')
          self.root.geometry('600x350')

          self.my_label = customtkinter.CTkLabel(self.root, text="", font=("Helvetica", 24))
          self.my_label.pack(pady=40)

          self.my_entry = customtkinter.CTkEntry(self.root, 
                                                  placeholder_text="Enter your name",
                                                  height=50,
                                                  width=200,
                                                  font=('Helvitica', 18),
                                                  corner_radius=50,
                                                  text_color='green',
                                                  placeholder_text_color='darkblue',
                                                  fg_color=('blue', 'lightblue'),
                                                  state='normal'
                                                  )
          self.my_entry.pack(pady=20)     

          self.my_button = customtkinter.CTkButton(self.root, text="Submit", command=self.submit)
          self.my_button.pack(pady=10)

          self.clear_button = customtkinter.CTkButton(self.root, text="Clear", command=self.clear)
          self.clear_button.pack(pady=10)

     def submit(self):
          self.my_label.configure(text=f'Hello {self.my_entry.get()}')
          self.my_entry.configure(state='disabled')

     def clear(self):
          self.my_entry.configure(state='normal')
          self.my_entry.delete(0, END)
          
          
     def run(self):
          self.root.mainloop()
          rospy.spin()

if __name__ == '__main__':
    app = CustomTkinterApp()
    app.run()
