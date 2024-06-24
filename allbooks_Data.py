from customtkinter import *
from threading import Thread

class allbooks_data:
    def __init__(self) -> None:
        self.availableBooksList = {
            1: {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson'},
            2: {'title': 'Structure and Interpretation of Computer Programs', 'author': 'Harold Abelson'},
            3: {'title': 'The C Programming Language', 'author': 'Brian W. Kernighan'},
            4: {'title': 'The Art of Computer Programming, Volumes 1-3 Boxed Set', 'author': 'Donald Ervin Knuth'},
            5: {'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'author': 'Erich Gamma'},
            6: {'title': 'The Pragmatic Programmer: From Journeyman to Master', 'author': 'Andy Hunt'},
            7: {'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser'},
            8: {'title': 'Windows 11: 2021 Complete New OS User Guide. 33 Best Tips and Tricks to Master your PC', 'author': 'Allan Farington'},
            9: {'title': 'Code: The Hidden Language of Computer Hardware and Software', 'author': 'Charles Petzold'},
            10: {'title': 'The Mythical Man-Month: Essays on Software Engineering', 'author': 'Frederick P. Brooks Jr.'},
            11: {'title': 'Clean Code: A Handbook of Agile Software Craftsmanship', 'author': 'Robert C. Martin'},
            12: {'title': 'Algorithms', 'author': 'Robert Sedgewick & Kevin Wayne'},
            13: {'title': 'Types and Programming Languages', 'author': 'Benjamin C. Pierce'},
            14: {'title': 'Code Complete: A Practical Handbook of Software Construction', 'author': 'Steve McConnell'},
            15: {'title': 'Introduction to Computer Science Using Python', 'author': 'Charles Dierbach'},
            16: {'title': 'JavaScript: The Good Parts', 'author': 'Douglas Crockford'},
            17: {'title': 'The Elements of Computing Systems: Building a Modern Computer from First Principles', 'author': 'Noam Nisan; Shimon Schocken'},
            18: {'title': 'Modern Operating Systems', 'author': 'Andrew S. Tanenbaum'},
            19: {'title': 'Computer Networks', 'author': 'Andrew S. Tanenbaum; David J. Wetherall'},
            20: {'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell & Peter Norvig'},
            21: {'title': 'Database System Concepts', 'author': 'Abraham Silberschatz, Henry F. Korth, S. Sudarshan'},
            22: {'title': 'Computer Organization and Design MIPS Edition: The Hardware/Software Interface', 'author': 'David A. Patterson & John L. Hennessy'}
        }

        self.issuedBooksList = {
            1: {'title': 'Computer Systems: A Programmer\'s Perspective', 'author': 'Randal E. Bryant & David R. O\'Hallaron'},
            2: {'title': 'Digital Design and Computer Architecture', 'author': 'David Harris & Sarah Harris'},
            3: {'title': 'Operating System Concepts', 'author': 'Abraham Silberschatz, Peter B. Galvin & Greg Gagne'},
            4: {'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho, Monica S. Lam, Ravi Sethi & Jeffrey D. Ullman'},
            5: {'title': 'Computer Networking: A Top-Down Approach', 'author': 'James F. Kurose & Keith W. Ross'},
            6: {'title': 'Discrete Mathematics and Its Applications', 'author': 'Kenneth H. Rosen'},
            7: {'title': 'Artificial Intelligence: Structures and Strategies for Complex Problem Solving', 'author': 'George F. Luger'},
            8: {'title': 'Data Structures and Algorithm Analysis in C++', 'author': 'Mark A. Weiss'},
            9: {'title': 'Introduction to the Design and Analysis of Algorithms', 'author': 'Anany Levitin'},
            10: {'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes, Andries van Dam, Morgan McGuire, David F. Sklar, James D. Foley, Steven K. Feiner & Kurt Akeley'},
            11: {'title': 'Cryptography and Network Security: Principles and Practice', 'author': 'William Stallings'}
        }

    # NOTE: This is only for Add book function from Librarian GUI class 
    def show_available_books_frame(self, frame) -> None:  
        def thread_manager() -> None:
            # Insert available books into the Text widget with checkboxes
            self.check_vars1 = {}
            for book_id, book_info in self.availableBooksList.items():
                book_title_author = f"{book_info['title']} by {book_info['author']}"
                check_var = StringVar() # Stores the state of the checkbox
                checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                self.check_vars1[book_title_author] = check_var

        thread = Thread(target=thread_manager)
        thread.start()

    def show_available_books_frame1(self, frame) -> None:
        """
        Displays available books in the given frame with checkboxes. 
        If a search query is provided, it filters the books based on the query.
        
        Args:
            frame: The frame where the available books going to display.
        """
        def thread_manager() -> None:
            # Clear the frame before populating it
            """
             NOTE: Thread Safety: 
             Tkinter is not thread-safe, meaning we should only update the UI from the main thread. 
             If we are using threads to perform background tasks, make sure to use thread-safe methods to update the UI, 
             such as `after()` method in Tkinter.
            """
            frame.after(0, lambda: [widget.destroy() for widget in frame.winfo_children()])

            # Retrieve the search query
            search_query = self.borrow_book_searchbookname_entry1.get().strip().lower()

            # Insert available books into the Text widget with checkboxes
            self.check_vars2 = {}
            for book_id, book_info in self.availableBooksList.items():
                book_title_author = f"{book_info['title']} by {book_info['author']}"

                if search_query:
                    # Check if the search query matches the book title or author
                    if search_query in book_info['title'].lower() or search_query in book_info['author'].lower():
                        check_var = StringVar()  # Stores the state of the checkbox
                        checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                        checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                        self.check_vars2[book_title_author] = check_var

                else:
                    # If no search query, display all books
                    check_var = StringVar()  # Stores the state of the checkbox
                    checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                    checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                    self.check_vars2[book_title_author] = check_var

        thread = Thread(target=thread_manager)
        thread.start()

    # NOTE: This is only for Remove book function from Librarian GUI class 
    def show_available_books_frame2(self, frame) -> None:
        """
        Displays available books in the given frame with checkboxes. 
        If a search query is provided, it filters the books based on the query.
        
        Args:
            frame: The frame where the available books going to display.
        """
        def thread_manager() -> None:
            # Clear the frame before populating it
            """
             NOTE: Thread Safety: 
             Tkinter is not thread-safe, meaning we should only update the UI from the main thread. 
             If we are using threads to perform background tasks, make sure to use thread-safe methods to update the UI, 
             such as `after()` method in Tkinter.
            """
            frame.after(0, lambda: [widget.destroy() for widget in frame.winfo_children()])

            # Retrieve the search query
            search_query = self.remove_book_searchbookname_entry1.get().strip().lower()

            # Insert available books into the Text widget with checkboxes
            self.check_vars3 = {}
            for book_id, book_info in self.availableBooksList.items():
                book_title_author = f"{book_info['title']} by {book_info['author']}"

                if search_query:
                    # Check if the search query matches the book title or author
                    if search_query in book_info['title'].lower() or search_query in book_info['author'].lower():
                        check_var = StringVar()  # Stores the state of the checkbox
                        checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                        checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                        self.check_vars3[book_title_author] = check_var

                else:
                    # If no search query, display all books
                    check_var = StringVar()  # Stores the state of the checkbox
                    checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                    checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                    self.check_vars3[book_title_author] = check_var

        thread = Thread(target=thread_manager)
        thread.start()

    # NOTE: Implemented 
    def show_unavailable_books_frame(self, frame) -> None:
        def thread_manager() -> None:
            # Insert issued books into the Text widget with checkboxes
            self.check_vars4 = {}
            for book_id, book_info in self.issuedBooksList.items():
                book_title_author = f"{book_info['title']} by {book_info['author']}"
                check_var = StringVar() # Stores the state of the checkbox
                checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                self.check_vars4[book_title_author] = check_var
        
        thread = Thread(target=thread_manager)
        thread.start()

    def show_unavailable_books_frame1(self, frame) -> None:
        """
        Displays available books in the given frame with checkboxes. 
        If a search query is provided, it filters the books based on the query.
        
        Args:
            frame: The frame where the available books going to display.
        """
        def thread_manager() -> None:
            # Clear the frame before populating it
            """
             NOTE: Thread Safety: 
             Tkinter is not thread-safe, meaning we should only update the UI from the main thread. 
             If we are using threads to perform background tasks, make sure to use thread-safe methods to update the UI, 
             such as `after()` method in Tkinter.
            """
            frame.after(0, lambda: [widget.destroy() for widget in frame.winfo_children()])

            # Retrieve the search query
            search_query = self.return_book_searchbookname_entry1.get().strip().lower()

            # Insert available books into the Text widget with checkboxes
            self.check_vars5 = {}
            for book_id, book_info in self.issuedBooksList.items():
                book_title_author = f"{book_info['title']} by {book_info['author']}"

                if search_query:
                    # Check if the search query matches the book title or author
                    if search_query in book_info['title'].lower() or search_query in book_info['author'].lower():
                        check_var = StringVar()  # Stores the state of the checkbox
                        checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                        checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                        self.check_vars5[book_title_author] = check_var

                else:
                    # If no search query, display all books
                    check_var = StringVar()  # Stores the state of the checkbox
                    checkbox = CTkCheckBox(master=frame, text=book_title_author, variable=check_var, onvalue='checked', offvalue='unchecked')
                    checkbox.pack(anchor='center', expand=True, fill='x', side='top', ipady=4)
                    self.check_vars5[book_title_author] = check_var

        thread = Thread(target=thread_manager)
        thread.start()
        
