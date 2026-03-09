class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe_book(self):
        print(f"The book {self.title} is written by {self.author} and has {self.pages} pages.")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book1.describe_book()

print()

book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book2.describe_book()