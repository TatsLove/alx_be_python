# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the Book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the object is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation used with print()"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation to recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
