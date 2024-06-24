from PIL import Image
from customtkinter import *
from threading import Thread

# Importing OtherClasses
from allbooks_Data import allbooks_data
from student_Actions import student_actions

class student_GUI(student_actions, allbooks_data):
    def __init__(self, main_content_frame) -> None:
        self.main_content_frame = main_content_frame

    def student_frame(self) -> None:
        # Calling from main_GUI using inheritance
        thread0 = Thread(target=self.destroy_main_frame())
        thread0.start()
        thread0.join()

        tabview = CTkTabview(master=self.main_content_frame, border_color=('white', 'black'), border_width=4)
        tabview.pack(padx=11, pady=11, fill='both', expand=True)

        # create tabs
        self.borrow_book = tabview.add("Borrow Book")
        self.return_book = tabview.add("Return Book")

        # Functions for tabs
        thread1 = Thread(target=self.borrow_book_tab(self.borrow_book))
        thread2 = Thread(target=self.return_book_tab(self.return_book))

        # # Start threads
        thread1.start()
        thread2.start()

    def borrow_book_tab(self, frame) -> None:
        self.frame0 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame0.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.96, relheight=0.77)
        
        self.scrollable_frame0 = CTkScrollableFrame(master=self.frame0, width=444, height=222)
        self.scrollable_frame0.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.96, relheight=0.933)
        
        self.frame0_0 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame0_0.place(relx=0.5, rely=0.9, anchor='center', relwidth=0.96, relheight=0.191)

        image_path1 = ".\Icons\\processicon1.png"
        loaded_image1 = Image.open(image_path1)
        ctk_image1 = CTkImage(light_image=loaded_image1, size=(44,44))
        borrow_book_button = CTkButton(master=self.frame0_0, text="Process! :)", image=ctk_image1, corner_radius=9, command=self.borrow_book_action)
        borrow_book_button.place(relx=0.86, rely=0.5, anchor='center', relwidth=0.22, relheight=0.66)

        self.frame0_0_0 = CTkFrame(master=self.frame0_0, fg_color=('White', '#1b1b1b'), border_color='black', border_width=2)
        self.frame0_0_0.place(relx=0.5, rely=0.5, relwidth=0.44, relheight=0.69, anchor='center')

        self.borrow_book_searchbookname_entry1 = CTkEntry(master=self.frame0_0_0, placeholder_text="Search", fg_color='transparent', corner_radius=44, width=111, border_color=('gray', 'black'))
        self.borrow_book_searchbookname_entry1.place(relx=0.42, rely=0.5, relwidth=0.77, relheight=0.59, anchor='center')

        image_path2 = ".\Icons\\search_icon.png"
        loaded_image2 = Image.open(image_path2)
        ctk_image2 = CTkImage(light_image=loaded_image2, size=(22,22))
        search_book_button = CTkButton(master=self.frame0_0_0, text='', command=lambda:self.show_available_books_frame1(self.scrollable_frame0), image=ctk_image2, corner_radius=4, width=33)
        search_book_button.place(relx=0.89, rely=0.5, relwidth=0.11, relheight=0.6, anchor='center')

        self.show_available_books_frame1(self.scrollable_frame0)

    def return_book_tab(self, frame) -> None:
        self.frame1 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame1.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.96, relheight=0.77)

        self.scrollable_frame1 = CTkScrollableFrame(master=self.frame1, width=444, height=222)
        self.scrollable_frame1.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.96, relheight=0.933)
        
        self.frame1_0 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame1_0.place(relx=0.5, rely=0.9, anchor='center', relwidth=0.96, relheight=0.191)

        image_path1 = ".\Icons\\processicon2.png"
        loaded_image1 = Image.open(image_path1)
        ctk_image1 = CTkImage(light_image=loaded_image1, size=(44,44))
        return_book_button = CTkButton(master=self.frame1_0, text="Process! :)", image=ctk_image1, corner_radius=9, command=self.return_book_action)
        return_book_button.place(relx=0.86, rely=0.5, anchor='center', relwidth=0.22, relheight=0.66)

        self.frame1_0_0 = CTkFrame(master=self.frame1_0, fg_color=('White', '#1b1b1b'), border_color='black', border_width=2)
        self.frame1_0_0.place(relx=0.5, rely=0.5, relwidth=0.44, relheight=0.69, anchor='center')

        self.return_book_searchbookname_entry1 = CTkEntry(master=self.frame1_0_0, placeholder_text="Search", fg_color='transparent', corner_radius=44, width=111, border_color=('gray', 'black'))
        self.return_book_searchbookname_entry1.place(relx=0.42, rely=0.5, relwidth=0.77, relheight=0.59, anchor='center')

        image_path2 = ".\Icons\\search_icon.png"
        loaded_image2 = Image.open(image_path2)
        ctk_image2 = CTkImage(light_image=loaded_image2, size=(22,22))
        search_book_button = CTkButton(master=self.frame1_0_0, text='', image=ctk_image2, corner_radius=4, width=33, command=lambda:self.show_unavailable_books_frame1(self.scrollable_frame1))
        search_book_button.place(relx=0.89, rely=0.5, relwidth=0.11, relheight=0.6, anchor='center')

        self.show_unavailable_books_frame1(self.scrollable_frame1)
        
