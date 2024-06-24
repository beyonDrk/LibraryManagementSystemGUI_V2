from PIL import Image
from customtkinter import *
from threading import Thread

from allbooks_Data import allbooks_data
from librarian_Actions import librarian_actions

class librarian_GUI(librarian_actions, allbooks_data):
    def __init__(self, main_content_frame) -> None:
        self.main_content_frame = main_content_frame
        self.admin_menubar_visible = False

    def librarian_auth_frame(self) -> None:
        # Calling from main_GUI using inheritance
        self.destroy_main_frame()

        # Create a label
        label1 = CTkLabel(master=self.main_content_frame, text="You need to authenticate your self Sir!")
        label1.pack(pady=11)

        self.frame0 = CTkFrame(master=self.main_content_frame, fg_color=('White', '#555555'), border_color='black', border_width=0)
        self.frame0.place(relx=0.107, rely=0.111, relwidth=0.79, relheight=0.77)

        image_path0 = ".\Icons\loginframe_icon3.png" 
        loaded_image0 = Image.open(image_path0)
        ctk_login_image0 = CTkImage(light_image=loaded_image0, size=(771,567))
        label_image0 = CTkLabel(master=self.frame0, image=ctk_login_image0, text="")
        label_image0.place(relx=0.202, rely=0, relwidth=0.90, relheight=1)
        
        frame1 = CTkFrame(master=self.frame0, fg_color=('White', '#1d1d1d'), border_color='black', border_width=0)
        frame1.place(relx=0.5, rely=0.4, anchor='center')

        image_path1 = ".\Icons\loginframe_icon5.jpg" 
        loaded_image1 = Image.open(image_path1)
        ctk_login_image1 = CTkImage(light_image=loaded_image1, size=(203,149))
        label_image1 = CTkLabel(master=frame1, image=ctk_login_image1, text="")
        label_image1.pack(side='left', expand=True, fill='x', padx=0, pady=0)

        frame2 = CTkFrame(master=frame1, fg_color="transparent", corner_radius=0)
        frame2.pack(side='right', expand=False, fill='y', padx=0, pady=0)

        self.username_entry = CTkEntry(master=frame2, placeholder_text="username", fg_color="transparent", corner_radius=44, width=222)
        self.username_entry.pack(padx=10, pady=10, side='top')
        self.password_entry = CTkEntry(master=frame2, placeholder_text="password", fg_color="transparent", corner_radius=44, width=222)
        self.password_entry.pack(padx=10, pady=10, side='top')

        # TODO: Implementation is not done yet
        login_button = CTkButton(master=frame2, text="Login", command=self.auth_check, corner_radius=44)
        login_button.pack(padx=10, pady=10, side='top')

        self.forgot_password_frame()

    def forgot_password_frame(self) -> None:
        frame3 = CTkFrame(master=self.main_content_frame, fg_color=('White', '#1d1d1d'), border_color='black', border_width=1, corner_radius=1)
        frame3.place(relx=0.5, rely=0.8, anchor='center')

        image_path2 = ".\Icons\loginframe_icon2.png" 
        loaded_image2 = Image.open(image_path2)
        ctk_login_image2 = CTkImage(light_image=loaded_image2, size=(150,111))

        label_image2 = CTkLabel(master=frame3, image=ctk_login_image2, text="")
        label_image2.pack(side='left', expand=True, fill='x', padx=11, pady=20)

        # Create a label
        label2 = CTkLabel(master=frame3, text="Oops! Forgot your password!")
        label2.pack(side='top', padx=11, pady=26)
        
        # TODO: Implementation is not done yet
        forgotpass_button = CTkButton(master=frame3, text="Click Here!", command=self.forgotpass_action, corner_radius=44)
        forgotpass_button.pack(side='top', padx=11, pady=11)

    def admin_menubar_frame(self) -> None:
        self.admin_menubar = CTkFrame(master=self.top_frame, fg_color=('white', '#1a1a1a'), border_color='black', border_width=2)
        self.admin_menubar.pack(anchor='center', side='right', padx=8, pady=11)

        self.logout_button = CTkButton(master=self.admin_menubar, command=self.librarian_auth_frame, text="logout", corner_radius=4)
        self.logout_button.pack(anchor='center', padx=8, pady=8)

    def toggle_admin_menubar(self) -> None:
        if self.admin_menubar_visible:
            self.hide_admin_menubar()
        else:
            self.show_admin_menubar()

    def hide_admin_menubar(self) -> None:
        self.admin_menubar.pack_forget()
        self.admin_menubar_visible = False

    def show_admin_menubar(self) -> None:
        self.admin_menubar_frame()
        self.admin_menubar_visible = True

    # FIXED: Implementation of threads
    def librarian_frame(self) -> None:
        # Calling from main_GUI using inheritance
        thread0 = Thread(target=self.destroy_main_frame())
        thread0.start()
        thread0.join()

        def new_thread_for_topframe() -> None:
            self.top_frame = CTkFrame(master=self.main_content_frame, fg_color='transparent')
            self.top_frame.pack(side='top', fill='x', padx=11, pady=1)

            # Admin button with image for top_frame
            image_path = ".\Icons\\admin_icon1.png"
            loaded_image = Image.open(image_path)
            ctk_image = CTkImage(light_image=loaded_image, size=(27,29))
            admin_button = CTkButton(master=self.top_frame, text="", image=ctk_image, command=self.toggle_admin_menubar, corner_radius=8, width=44, height=44)
            admin_button.pack(side='right', padx=1, pady=11)

        thread1 = Thread(target=new_thread_for_topframe())
        
        def new_thread_for_tabview() -> None:
            self.tabview = CTkTabview(master=self.main_content_frame, border_color=('white', 'black'), border_width=3)
            self.tabview.pack(padx=11, pady=7, fill='both', expand=True)

            # created tabs
            self.add_book = self.tabview.add("Add Book")
            self.remove_book = self.tabview.add("Remove Book")
            self.reset_pass = self.tabview.add("Reset Password")

            image_path = ".\Icons\pattern.png" 
            loaded_image = Image.open(image_path)
            ctk_fg_image = CTkImage(light_image=loaded_image, size=(1441,777))
            label_image = CTkLabel(master=self.reset_pass, image=ctk_fg_image, text="")
            label_image.place(relx=0.5, rely=0.5, anchor='center', relwidth=1, relheight=1)

        thread2 = Thread(target=new_thread_for_tabview())
        
        # FIXME: Working Progress the implementation of threads
        thread3 = Thread(target=self.add_book_tab, args=(self.add_book,))
        thread4 = Thread(target=self.remove_book_tab, args=(self.remove_book,))
        thread5 = Thread(target=self.reset_pass_tab, args=(self.reset_pass,))

        # Starting threads
        thread3.start()
        thread4.start()
        thread5.start()

        thread1.start()
        thread2.start()

        # Join threads to main thread
        thread1.join()
        thread2.join()

    def add_book_tab(self, frame) -> None:
        # NOTE: Creating widgets for Add_book_tab 
        # Creating all frames
        self.frame2 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame2.place(relx=0.34, rely=0.5, anchor='center', relwidth=0.66, relheight=0.96)
        
        self.frame2_scrollable_1 = CTkScrollableFrame(master=self.frame2)
        self.frame2_scrollable_1.place(relx=0.5, rely=0.26, anchor='center', relwidth=0.96, relheight=0.47)
        self.frame2_scrollable_2 = CTkScrollableFrame(master=self.frame2)
        self.frame2_scrollable_2.place(relx=0.5, rely=0.74, anchor='center', relwidth=0.96, relheight=0.47)
    
        self.frame2_1 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame2_1.place(relx=0.833, rely=0.5, anchor='center', relwidth=0.313, relheight=0.96)

        self.frame2_1_1 = CTkFrame(master=self.frame2_1, fg_color=('White', '#1e1e1e'), border_color='black', border_width=3)
        self.frame2_1_1.place(relx=0.5, rely=0.259, anchor='center', relwidth=0.96, relheight=0.49)

        image_path0 = ".\Icons\\librarian_icon1.png"
        loaded_image0 = Image.open(image_path0)
        ctk_image0 = CTkImage(light_image=loaded_image0, size=(140,140))  
        label_image = CTkLabel(master=self.frame2_1_1, image=ctk_image0, text='')     
        label_image.pack(padx=1, pady=1 , anchor='center', expand=True)      
        
        # Adding CTkButton
        image_path1 = ".\Icons\\addbook_icon1.png"
        loaded_image1 = Image.open(image_path1)
        ctk_image1 = CTkImage(light_image=loaded_image1, size=(33,33))
        add_book_button = CTkButton(master=self.frame2_1, text="Add!", image=ctk_image1, corner_radius=11, command=self.add_book_action)
        add_book_button.place(anchor='center', relx=0.5, rely=0.9, relwidth=0.66, relheight=0.13)
        
        # Adding CTkEntry 
        self.bookauthorname_entry1 = CTkEntry(master=self.frame2_1, placeholder_text="Enter the author name", fg_color='transparent', corner_radius=11, width=222, border_color=('gray', 'black'))
        self.bookauthorname_entry1.place(anchor='center', relx=0.5, rely=0.74, relwidth=0.96, relheight=0.13)

        self.bookname_entry2 = CTkEntry(master=self.frame2_1, placeholder_text="Enter the book name", fg_color='transparent', corner_radius=11, width=222, border_color=('gray', 'black'))
        self.bookname_entry2.place(anchor='center', relx=0.5, rely=0.59, relwidth=0.96, relheight=0.13)

        # FIXME: I have to add 2 frames here 
        self.show_available_books_frame(self.frame2_scrollable_1)
        self.show_unavailable_books_frame(self.frame2_scrollable_2)
        
    def remove_book_tab(self, frame) -> None:
        # FIXME: WORK in progress
        # NOTE: Creating widgets for remove_book_tab 
        self.frame3 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame3.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.96, relheight=0.77)
        self.scrollable_frame = CTkScrollableFrame(master=self.frame3, width=444, height=222)
        self.scrollable_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.96, relheight=0.933)

        self.frame3_1 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), border_color='black', border_width=2)
        self.frame3_1.place(relx=0.5, rely=0.9, anchor='center', relwidth=0.96, relheight=0.191)

        image_path1 = ".\Icons\\removebook.png"
        loaded_image1 = Image.open(image_path1)
        ctk_image1 = CTkImage(light_image=loaded_image1, size=(26,36))
        remove_book_button = CTkButton(master=self.frame3_1, image=ctk_image1, text="Remove!", corner_radius=9, command=self.remove_book_action)
        remove_book_button.place(relx=0.86, rely=0.5, anchor='center', relwidth=0.19, relheight=0.66)
        
        self.frame3_1_0 = CTkFrame(master=self.frame3_1, fg_color=('White', '#1b1b1b'), border_color='black', border_width=2)
        self.frame3_1_0.place(relx=0.5, rely=0.5, relwidth=0.44, relheight=0.69, anchor='center')

        self.remove_book_searchbookname_entry1 = CTkEntry(master=self.frame3_1_0, placeholder_text="Search bar", fg_color='transparent', corner_radius=44, width=111, border_color=('gray', 'black'))
        self.remove_book_searchbookname_entry1.place(relx=0.42, rely=0.5, relwidth=0.77, relheight=0.59, anchor='center')

        image_path2 = ".\Icons\\search_icon.png"
        loaded_image2 = Image.open(image_path2)
        ctk_image2 = CTkImage(light_image=loaded_image2, size=(22,22))
        search_book_button = CTkButton(master=self.frame3_1_0, text='', command=lambda:self.show_available_books_frame2(self.scrollable_frame), image=ctk_image2, corner_radius=4, width=33)
        search_book_button.place(relx=0.89, rely=0.5, relwidth=0.11, relheight=0.6, anchor='center')

        self.show_available_books_frame2(self.scrollable_frame)

    def reset_pass_tab(self, frame) -> None:
        # NOTE: Creating widgets for reset_pass_tab 
        self.frame4 = CTkFrame(master=frame, fg_color=('White', '#1e1e1e'), bg_color=('#252525','#252525'), border_color='black', border_width=2)
        self.frame4.place(relx=0.5, rely=0.5, anchor='center')

        self.old_password_entry0 = CTkEntry(master=self.frame4, placeholder_text="Old Password", fg_color="transparent", corner_radius=44, width=222, border_color=('gray', 'black'))
        self.old_password_entry0.pack(padx=10, pady=10, side='top')

        self.new_password_entry1 = CTkEntry(master=self.frame4, placeholder_text="New Password", fg_color="transparent", corner_radius=44, width=222, border_color=('gray', 'black'))
        self.new_password_entry1.pack(padx=10, pady=10, side='top')

        self.new_password_entry2 = CTkEntry(master=self.frame4, placeholder_text="Re-enter new Password", fg_color="transparent", corner_radius=44, width=222, border_color=('gray', 'black'))
        self.new_password_entry2.pack(padx=10, pady=10, side='top')

        image_path1 = ".\Icons\\submitbutton.png"
        loaded_image1 = Image.open(image_path1)
        ctk_image1 = CTkImage(light_image=loaded_image1, size=(111,44))
        forgotpass_button = CTkButton(master=self.frame4, text="", image=ctk_image1, hover_color='black', bg_color='transparent', fg_color='transparent', command=self.update_pass, corner_radius=44)
        forgotpass_button.pack(side='top', padx=11, pady=11)

