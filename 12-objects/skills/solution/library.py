class Book:
    def __init__(self, title, author, isbn, year):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = int(year)

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    """ OPTIONAL 

    @isbn.setter        # in constructor: call setter!
    def isbn(self,value):
        if len(value) != 13 or not value.isdigit():
            raise ValueError("Invalid ISBN")
        self.__isbn = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self,value):
        if len(value) != 4 or not value.isdigit():
            raise ValueError("Invalid year")
        self.__year = int(value)

    """

    def info(self):
        return f"'{self.__title}' by {self.__author} (ISBN: {self.__isbn}, Jaar: {self.__year})"


class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def add_book(self, book):
        if not isinstance(book,Book):
            raise ValueError("This is not a book")
        for b in self.__books:
            if b.isbn == book.isbn:
                raise ValueError("This book is already in the library")
        self.__books.append(book)

    def load_books_from_file(self, filename):
        with open(filename, 'r',encoding='utf-8') as file:
            lines = file.readlines()
        book_data = []
        for line in lines:
            line = line.strip() # remove \n and spaces at beginning & end
            if line != "":
                book_data.append(line)
            if len(book_data) == 4:  # We need 4 lines per book
                title, author, isbn, year = book_data
                self.add_book(Book(title, author, isbn, year))
                book_data = []

    def search_book(self,title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                print("this book is in the library:")
                return book.info()
        print(print("this book is not in library"))

    def info(self):
        output = f"Library: {self.__name}\n"
        for book in self.__books:
            output += f"- {book.info()}\n"
        return output

# Usage
library = Library("City Leuven")
library.load_books_from_file("books.txt")
# print(library.info())
print(library.search_book("1984"))
# print(library.search_book("1985"))
