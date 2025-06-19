#Ebook 
# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def get_info(self):
        return f"{super().get_info()} [EBook, {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        return f"{super().get_info()} [PrintBook, {self.page_count} pages]"


class Library:
    def __init__(self):
        self.books = []  # List of Book, EBook, or PrintBook instances

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only books can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book.get_info()}")
