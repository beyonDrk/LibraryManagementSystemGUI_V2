from PIL import Image
from customtkinter import *
from threading import Thread

from allbooks_Data import allbooks_data
from librarian_Actions import librarian_actions
from student_GUI import student_GUI 
from librarian_GUI import librarian_GUI
from settings_GUI import settings_GUI

class main_GUI(student_GUI, librarian_GUI, settings_GUI):
    def __init__(self) -> None:
        # Initialize the main application window
        self.app = CTk()
        self.app.geometry("696x444")
        self.app.title("Library Management System")

        # Calling frames method to create the GUI ctk widgets
        self.foreground_frame()
        self.main_frame()
        self.side_frame()
        
        # Calling the constructor of the mentioned class 
        allbooks_data.__init__(self)
        librarian_actions.__init__(self)
        librarian_GUI.__init__(self, self.main_content_frame)

        # Constructor Variable
        self.sidebar_visible = False

    def all_thread_manager(self) -> None:
        # Create threads
        thread1 = Thread(target=self.main_frame())
        thread2 = Thread(target=self.side_frame())

        # Start threads
        thread1.start()
        thread2.start()

    def foreground_frame(self) -> None:
        # Main content frame
        self.foreground_content_frame = CTkFrame(master=self.app, fg_color='black')
        self.foreground_content_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def main_frame(self) -> None:
        # Main content frame
        self.main_content_frame = CTkFrame(master=self.app, border_color="black", border_width=1)
        self.main_content_frame.place(relx=0.059, rely=0, relwidth=0.94, relheight=1)

        image_path2 = ".\Icons\landingimg.png" 
        loaded_image2 = Image.open(image_path2)
        ctk_login_image2 = CTkImage(dark_image=loaded_image2, size=(909,505))
        label_image2 = CTkLabel(master=self.main_content_frame, image=ctk_login_image2, text_color='#000000', text="")
        label_image2.place(relx=0.5, rely=0.5, anchor='center', relwidth=1, relheight=1)

        # Create a label
        self.label = CTkLabel(master=self.main_content_frame, padx=11, text="Welcome to the Library Management System!")
        self.label.place(anchor='center', relx=0.5, rely=0.77)

    # TODO: I need to work on this to create more frame destroyer
    def destroy_main_frame(self) -> None:
        # Destroy all children widgets in main_content_frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()
                
    def side_frame(self) -> None:
        # Side content frame 
        self.sidebar_frame = CTkFrame(master=self.app, width=111, border_width=1, border_color=("gray", "#4a4a4a"), fg_color=("white", "#1f1f1f"))
        self.sidebar_frame.place(x=0, y=0, relwidth=0.059, relheight=1, relx=0, rely=0)

        # Menu button
        self.menu_button = CTkButton(master=self.sidebar_frame, text="☰", command=self.toggle_menu)
        self.menu_button.place(anchor="nw", relx=0.080, rely=0.01, relwidth=0.827, relheight=0.040)

        # Student image and button
        image_path1 = ".\Icons\student_icon.png"  # Replace with the path to your image
        loaded_image1 = Image.open(image_path1)
        ctk_student_image = CTkImage(light_image=loaded_image1, size=(30,30))
        self.student_frame_button1 = CTkButton(master=self.sidebar_frame, text="Student", image=ctk_student_image, command=self.student_frame, fg_color="black", hover_color="gray")
        self.student_frame_button2 = CTkButton(master=self.sidebar_frame, text="", image=ctk_student_image, command=self.student_frame, fg_color="black", hover_color="gray")
        self.student_frame_button2.place(anchor="nw", relx=0.033, rely=0.07, relwidth=0.92, relheight=0.066)

        # Librarian image and button
        image_path2 = ".\Icons\librarian_icon.png"  # Replace with the path to your image
        loaded_image2 = Image.open(image_path2)
        ctk_librarian_image = CTkImage(light_image=loaded_image2, size=(30,30))
        self.librarian_frame_button1 = CTkButton(master=self.sidebar_frame, text="Librarian", image=ctk_librarian_image, command=self.librarian_auth_frame, fg_color="black", hover_color="gray")
        self.librarian_frame_button2 = CTkButton(master=self.sidebar_frame, text="", image=ctk_librarian_image, command=self.librarian_auth_frame, fg_color="black", hover_color="gray")
        self.librarian_frame_button2.place(anchor="nw", relx=0.033, rely=0.15, relwidth=0.92, relheight=0.066)

        # Settings image and button
        image_path3 = ".\Icons\settings_icon.png"  # Replace with the path to your image
        loaded_image3 = Image.open(image_path3)
        ctk_settings_image = CTkImage(light_image=loaded_image3, size=(30,30))
        self.settings_frame_button1 = CTkButton(master=self.sidebar_frame, text="Settings", image=ctk_settings_image, command=self.settings_frame, fg_color="black", hover_color="gray")
        self.settings_frame_button2 = CTkButton(master=self.sidebar_frame, text="", image=ctk_settings_image, command=self.settings_frame, fg_color="black", hover_color="gray")
        self.settings_frame_button2.place(anchor="nw", relx=0.033, rely=0.928, relwidth=0.92, relheight=0.066)

    def toggle_menu(self) -> None:
        if self.sidebar_visible:
            self.hide_sidebar()
        else:
            self.show_sidebar()

    def show_sidebar(self) -> None:
        # FIXED: This is not solved how to implement threads here 
        def new_thread_for_frame() -> None:
            # All frames
            self.sidebar_frame.place(relwidth=0.2)

        thread1 = Thread(target=new_thread_for_frame())
        
        def new_thread_for_button() -> None:
            # All buttons
            self.menu_button.place_configure(anchor="nw", relx=0.021, rely=0.01, relwidth=0.245, relheight=0.040)

            self.student_frame_button1.place(anchor="nw", relx=0.020, rely=0.07, relwidth=0.96, relheight=0.066)
            self.librarian_frame_button1.place(anchor="nw", relx=0.020, rely=0.15, relwidth=0.96, relheight=0.066)
            self.settings_frame_button1.place(anchor="nw", relx=0.020, rely=0.928, relwidth=0.96, relheight=0.066)

            self.student_frame_button2.place_forget()
            self.librarian_frame_button2.place_forget()
            self.settings_frame_button2.place_forget()

        thread2 = Thread(target=new_thread_for_button())

        # Starting all threads here
        thread1.start()
        thread2.start()

        # Joining all threads after task done
        thread1.join()
        thread2.join()

        self.sidebar_visible = True

    def hide_sidebar(self) -> None:
        # FIXED: This is not solved how to implement threads here 
        def new_thread_for_frame() -> None:
            # All frames
            self.sidebar_frame.place_configure(relwidth=0.059)
        
        thread2 = Thread(target=new_thread_for_frame())

        def new_thread_for_button() -> None:
            # All buttons
            self.menu_button.place_configure(anchor="nw", relx=0.080, rely=0.01, relwidth=0.827, relheight=0.040)

            self.student_frame_button1.place_forget()
            self.librarian_frame_button1.place_forget()
            self.settings_frame_button1.place_forget()

            self.student_frame_button2.place(anchor="nw", relx=0.033, rely=0.07, relwidth=0.92, relheight=0.066)
            self.librarian_frame_button2.place(anchor="nw", relx=0.033, rely=0.15, relwidth=0.92, relheight=0.066)
            self.settings_frame_button2.place(anchor="nw", relx=0.033, rely=0.928, relwidth=0.92, relheight=0.066)

        thread1 = Thread(target=new_thread_for_button())

        # Starting all threads here
        thread1.start()
        thread2.start()

        # Joining all threads after task done
        thread1.join()
        thread2.join()
        
        # Set sidebar visiblity False
        self.sidebar_visible = False

    def run(self) -> None:
        # Start the application
        self.app.mainloop()

if __name__ == "__main__":
    app = main_GUI()
    app.run()

