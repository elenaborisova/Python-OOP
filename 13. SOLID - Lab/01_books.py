class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        try:
            found_book = [book for book in self.books if book.title == title][0]
            return found_book
        except IndexError:
            return "No such book found in the library"

    def add_book(self, book):
        self.books.append(book)


class Person:
    def __init__(self, name):
        self.name = name


class Reader(Person):
    def __init__(self, name, curr_book):
        super().__init__(name)
        self.curr_book = curr_book
        self.curr_page = None

    def turn_page(self):
        if not self.curr_page:
            self.curr_page = 1
            return

        self.curr_page += 1
