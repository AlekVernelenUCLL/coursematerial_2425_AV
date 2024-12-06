class Book:
    def __init__(self, title, author, isbn, year):
        self.__title = title
        self.__author = author
        self.isbn = isbn #property
        self.year = year #property

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, string):
        if string.isdigit() and len(string) == 13:
            self.__isbn = str(string)
        else:
            raise ValueError("invalid isbn: needs to be 13 digits long")

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if value.isdigit() and len(value) == 4:
            self.__year = int(value)
        else:
            raise ValueError("invalid year: needs to be 4 digits long")

    def info(self):
        return f"book '{self.__title}' by {self.__author}, has isbn {self.__isbn}, was written in {self.__year}"
    

class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def add_book(self, book):
        for boek in self.__books:
            if book.isbn == boek.isbn:
                print("this book is already in library")
            else:
                self.__books.append(book)

    def load_books_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            list_lines = file.readlines()
        for i in range(0,len(list_lines),5):
            title = list_lines[i].strip()
            author = list_lines[i+1].strip()
            isbn = list_lines[i+2].strip()
            year = list_lines[i+3].strip()
            new_book = Book(title, author, isbn, year)
            self.add_book(new_book)

    def search_book(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                return book.info()
        print("this book is not in library")
            
    def info(self):
        result = f"Library {self.__name} has {len(self.__books)} books, namely:\n"
        for book in self.__books:
            result += f"- {book.info()}\n"
        return result
    
library = Library("City Leuven")
library.load_books_from_file("books.txt")
# print(library.info())
print(library.search_book("1984"))