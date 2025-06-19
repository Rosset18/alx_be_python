# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the Book object with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (used for debugging and development)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (optional test):
if __name__ == "__main__":
    my_book = Book("1984", "George Orwell", 1949)
    print(str(my_book))      # Output: 1984 by George Orwell, published in 1949
    print(repr(my_book))     # Output: Book('1984', 'George Orwell', 1949)
    del my_book              # Output: Deleting 1984
