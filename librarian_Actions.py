from CTkMessagebox import CTkMessagebox
from allbooks_Data import allbooks_data

class librarian_actions(allbooks_data):
    def __init__(self) -> None:
        # Librarian Credentials
        self.username = 'admin'
        self.password = 'admin123'
        
    # TODO: Work in progress
    def auth_check(self) -> None:
        if self.username_entry.get() == self.username and self.password_entry.get() == self.password:
            self.librarian_frame()

    def update_pass(self) -> None:
        if self.old_password_entry0.get() == self.password:
            if self.new_password_entry1.get() == self.new_password_entry2.get():
                if self.password != self.new_password_entry1.get():
                    self.password = self.new_password_entry1.get()
                    self.librarian_auth_frame()

    def forgotpass_action(self) -> None: 
        CTkMessagebox(message='Under Progress', title='Error')

    # TODO: Pick both entry from add_book then make a f string and add it in self.available_books then update/refresh all frames  
    def add_book_action(self) -> None:
        # Collecting the values from entry fields
        book_title = self.bookname_entry2.get()
        book_author = self.bookauthorname_entry1.get() 

        # Ensure both fields are filled 
        if not book_title or not book_author:
            return

        # Finding maximum id of items from availableBooksList dictionary
        max_id = max(self.availableBooksList.keys(), default=0)

        # Create a new dictionary entry
        new_book_entry = {'title': book_title, 'author': book_author}

        # Add the new entry to the availableBooksList dictionary
        self.availableBooksList[max_id + 1] = new_book_entry

        # Calling them from Librarian_GUI class to refresh the window
        self.add_book_tab(self.add_book) 
        self.remove_book_tab(self.remove_book)               

    def remove_book_action(self) -> None:
        checked_items = []

        # Collecting checked items
        for book_title_author, check_var in self.check_vars3.items():
            if check_var.get() == 'checked':
                checked_items.append(book_title_author)
        
        # Processing checked items
        for book_title_author in checked_items:
            for book_id, book_info in list(self.availableBooksList.items()):
                if f"{book_info['title']} by {book_info['author']}" == book_title_author:
                    del self.availableBooksList[book_id]
        
        # Calling them from Librarian_GUI class to refresh the window
        self.remove_book_tab(self.remove_book)
        self.add_book_tab(self.add_book)

    