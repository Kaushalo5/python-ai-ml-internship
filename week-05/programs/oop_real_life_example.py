# Real-life OOP example: Library System

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title)

lib = Library()
lib.add_book(Book("Python Basics"))
lib.add_book(Book("Machine Learning"))

lib.show_books()
