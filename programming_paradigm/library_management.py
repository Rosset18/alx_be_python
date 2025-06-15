class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out if not already."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available to check out."""
        return not self._is_checked_out

    def __str__(self):
        """Readable string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Tries to check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Returns a book back to the library by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Lists all books that are currently not checked out."""
        for book in self._books:
            if book.is_available():
                print(book)

