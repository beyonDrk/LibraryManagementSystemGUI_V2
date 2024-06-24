from allbooks_Data import allbooks_data

class student_actions(allbooks_data):
    def __init__(self) -> None:
        pass

    # TODO: Remove book from available_books then add it in issued_books then refresh both frame 
    def borrow_book_action(self) -> None:
        checked_items = []

        # Collecting checked items 
        for book_title_author, check_var in self.check_vars2.items():
            if check_var.get() == 'checked':
                checked_items.append(book_title_author)

        # Processing checked items
        max_id = max(self.issuedBooksList.keys(), default=0)

        for book_title_author in checked_items:
            for book_id, book_info in list(self.availableBooksList.items()):
                if f"{book_info['title']} by {book_info['author']}" == book_title_author:
                    max_id += 1
                    
                    # Adding checked items in issuedBooksList
                    self.issuedBooksList[max_id] = book_info
                    
                    # Remove checked items from availableBooksList
                    del self.availableBooksList[book_id]
        
        # Calling them from student_GUI class to refresh the frame
        self.borrow_book_tab(self.borrow_book)
        self.return_book_tab(self.return_book)

    def return_book_action(self) -> None:
        checked_items = []

        # Collecting checked items
        for book_title_author, check_var in self.check_vars5.items():
            if check_var.get() == 'checked':
                checked_items.append(book_title_author)
        
        # Processing checked items
        max_id = max(self.availableBooksList.keys(), default=0)

        for book_title_author in checked_items:
            for book_id, book_info in list(self.issuedBooksList.items()):
                if f"{book_info['title']} by {book_info['author']}" == book_title_author:
                    max_id += 1
                    
                    # Adding checked items in availableBooksList
                    self.availableBooksList[max_id] = book_info
                    
                    # Remove checked items from issuedBooksList
                    del self.issuedBooksList[book_id]
        
        # Calling them from student_GUI class to refresh the frame
        self.borrow_book_tab(self.borrow_book)
        self.return_book_tab(self.return_book)
        
