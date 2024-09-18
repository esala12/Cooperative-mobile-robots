#!/usr/bin/env python3

from tkinter import *
import customtkinter
from PIL import Image
import rospy
from dreambot_tkinter.msg import BoolInt, BoolString  # Import BoolString message
import threading

class CustomTkinterApp:
    def __init__(self):
        rospy.init_node('tkinter_gui_test1', anonymous=True)

        # ROS publishers for /activate_base_station and /multi_path
        self.base_station_pub = rospy.Publisher('/activate_base_station', BoolInt, queue_size=10)
        self.multi_path_pub = rospy.Publisher('/multi_path', BoolString, queue_size=10)  # Publisher for BoolString messages

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Create the main application window
        self.root = customtkinter.CTk()
        self.root.title('Tkinter.com - Custom Tkinter!')
        # Removed the fullscreen attribute
        # self.root.attributes('-fullscreen', True)

        # Adjust frame layout to fill the screen
        self.top_frame = customtkinter.CTkFrame(self.root)
        self.top_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Split the top frame into two sub-frames for the image and the entry box
        self.image_frame = customtkinter.CTkFrame(self.top_frame)
        self.image_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        self.entry_frame = customtkinter.CTkFrame(self.top_frame)
        self.entry_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

        # Adjust the grid to ensure the frames fill the screen properly
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)

        # Display the image using CTkImage in the image_frame
        self.image = Image.open("/home/esala/dreambot_ws/src/dreambot_tkinter/images/map.jpg")
        self.image = self.image.resize((600, 300), Image.Resampling.LANCZOS)
        self.ctk_image = customtkinter.CTkImage(light_image=self.image, dark_image=self.image, size=(600, 300))
        self.image_label = customtkinter.CTkLabel(self.image_frame, image=self.ctk_image, text="")
        self.image_label.pack(fill='both', expand=True)

        # Frame to center the entry box and button
        self.center_frame = customtkinter.CTkFrame(self.entry_frame)
        self.center_frame.pack(expand=True)

        # Entry widget to enter numbers from 1 to 10 in the entry_frame, centered
        self.number_entry = customtkinter.CTkEntry(self.center_frame, 
                                                   placeholder_text="Enter distance of the object (1-10)",
                                                   height=80,
                                                   width=380,
                                                   font=('Helvetica', 20),
                                                   corner_radius=10,
                                                   text_color='green',
                                                   placeholder_text_color='darkblue',
                                                   fg_color=('blue', 'lightblue'),
                                                   state='normal')
        self.number_entry.pack(pady=20, anchor='center')

        # Enter button below the entry box
        self.enter_button = customtkinter.CTkButton(self.center_frame, 
                                                    text="Enter", 
                                                    height=50, 
                                                    width=150,
                                                    font=('Helvetica', 20))
        self.enter_button.pack(pady=10, anchor='center')
        
        # Bind button press and release events for the Enter button
        self.enter_button.bind('<ButtonPress-1>', self.enter_pressed)
        self.enter_button.bind('<ButtonRelease-1>', self.enter_released)

        # Frame for buttons A to F
        self.buttons_frame = customtkinter.CTkFrame(self.root)
        self.buttons_frame.pack(fill='both', expand=True, pady=20)

        # Create buttons A to F, filling the space
        button_names = ["A", "B", "C", "D", "E", "F"]
        for i, name in enumerate(button_names):
            if name == "A":
                # Bind press and release for button A and disable it permanently
                button = customtkinter.CTkButton(
                    self.buttons_frame, 
                    text=name, 
                    height=80, 
                    width=120, 
                    font=('Helvetica', 20),
                    state='disabled'  # Disable Button A permanently
                )
            else:
                # Bind press and release for buttons B-F
                button = customtkinter.CTkButton(
                    self.buttons_frame, 
                    text=name, 
                    height=80, 
                    width=120, 
                    font=('Helvetica', 20)
                )
                button.bind('<ButtonPress-1>', lambda event, n=name: self.multi_path_pressed(event, n))
                button.bind('<ButtonRelease-1>', lambda event, n=name: self.multi_path_released(event, n))
            button.grid(row=i//3, column=i%3, padx=20, pady=20, sticky='nsew')

        # Make sure the buttons fill the entire frame
        for i in range(2):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.buttons_frame.grid_columnconfigure(i, weight=1)

        # Bind Escape key to exit fullscreen mode
        self.root.bind("<Escape>", self.exit_fullscreen)

    def enter_pressed(self, event):
        entered_number = self.number_entry.get()
        if entered_number.isdigit() and 1 <= int(entered_number) <= 10:
            self.current_number = int(entered_number)
            msg = BoolInt()
            msg.flag = True
            msg.number = self.current_number
            self.base_station_pub.publish(msg)
            print(f'Entered number: {entered_number} with activate_base_station set to True')
        else:
            print("Please enter a valid number between 1 and 10")
            self.current_number = 0

    def enter_released(self, event):
        threading.Timer(3.0, self.publish_false_message).start()
        print("Enter button released: waiting 3 seconds to publish False")

    def publish_false_message(self):
        msg = BoolInt()
        msg.flag = False
        msg.number = self.current_number
        self.base_station_pub.publish(msg)
        print(f"activate_base_station set to False with number {self.current_number}")

    def multi_path_pressed(self, event, button_name):
        # Publish True and button name when buttons B-F are pressed
        msg = BoolString()
        msg.flag = True
        msg.data = button_name
        self.multi_path_pub.publish(msg)
        print(f"Button {button_name} pressed: /multi_path set to True {button_name}")

    def multi_path_released(self, event, button_name):
        # Start a timer to publish False message 3 seconds after release
        threading.Timer(3.0, lambda: self.publish_multi_path_false(button_name)).start()
        print(f"Button {button_name} released: /multi_path will turn False {button_name} after 3 seconds")

    def publish_multi_path_false(self, button_name):
        # Publish False and button name
        msg = BoolString()
        msg.flag = False
        msg.data = button_name
        self.multi_path_pub.publish(msg)
        print(f"/multi_path set to False {button_name} after 3 seconds")

    def button_a_pressed(self, event):
        msg = BoolInt()
        msg.flag = True
        msg.number = 0
        self.base_station_pub.publish(msg)
        print("Button A pressed: activate_base_station set to True")
        threading.Timer(3.0, self.set_activate_base_station_false).start()

    def button_a_released(self, event):
        print("Button A released: activate_base_station will turn False after 3 seconds")

    def set_activate_base_station_false(self):
        msg = BoolInt()
        msg.flag = False
        msg.number = 0
        self.base_station_pub.publish(msg)
        print("activate_base_station set to False after 3 seconds")

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)

    def run(self):
        self.root.mainloop()
        rospy.spin()

if __name__ == '__main__':
    app = CustomTkinterApp()
    app.run()
