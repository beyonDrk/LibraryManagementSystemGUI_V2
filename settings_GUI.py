from PIL import Image
from customtkinter import *

class settings_GUI:
    def __init__(self, main_content_frame) -> None:
        self.main_content_frame = main_content_frame
       
    def settings_frame(self) -> None:
        # Calling from main_GUI using inheritance
        self.destroy_main_frame()

        image_path = ".\Icons\pattern.png" 
        loaded_image = Image.open(image_path)
        ctk_login_image = CTkImage(dark_image=loaded_image, size=(1333,777))

        label_image2 = CTkLabel(master=self.main_content_frame, image=ctk_login_image, text="")
        label_image2.place(relx=0.5, rely=0.5, anchor='center')

        about_us = (
            "About Us\n\n"
            "Welcome to the digital heart of our library, brought to life by Pratik.\n\n "
            "Our library management system stands as a testament to modern design and user-centric functionality, "
            "harnessing the power of the customtkinter Python UI library.\n"
            "Our goal is to enhance the library experience for both book lovers and librarians, "
            "offering a seamless interface for the organization and exploration of our extensive literary collection. "
            "Effortless navigation, efficient book tracking, and a simplified borrowing process are at the core of our system, "
            "ensuring that every reader finds their next great read.\n"
            "At the helm of this project is Pratik, a developer with a deep appreciation for literature and technology. "
            "This system is the fruit of a vision to create a space where knowledge thrives and managing a library is effortless.\n"
            "Embark with us on this transformative journey, as we redefine the way libraries engage with their communities "
            "and open up new chapters in the world of reading."
        )
        
        # label1
        self.label1 = CTkLabel(master=self.main_content_frame, text=about_us, corner_radius=9, justify="center", pady=7, bg_color=('#252525','#252525'), fg_color=("gray","black"), text_color="white", wraplength=611)
        self.label1.place(relx=0.5, rely=0.40, anchor='center')

        frame0 = CTkFrame(master=self.main_content_frame, width=222, height=99, corner_radius=22, bg_color=('#252525','#252525'), fg_color=('#afafaf','#141414'))
        frame0.place(relx=0.5, rely=0.8, anchor='center')

        text = "Change appearance here"
        label2 = CTkLabel(master=frame0, text=text, fg_color=('gray','black'), wraplength=191, padx=14, corner_radius=33)
        label2.place(relx=0.5, rely=0.4, anchor='center')

        # Combobox for appearance settings
        self.appearance_combobox = CTkComboBox(master=frame0, values=["System", "Light", "Dark"], command=self.set_appearance, width=99, corner_radius=1)
        self.appearance_combobox.place(relx=0.5, rely=0.7, anchor='center')
        
    def set_appearance(self, choice) -> None:
        set_appearance_mode(choice.lower())

