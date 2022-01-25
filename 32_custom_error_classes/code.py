class TooManyPagesReadError(ValueError):  # you must inherit from an error in able to raise the exception
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read}"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
                raise TooManyPagesReadError(
                    f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
                )
        self.pages_read += pages
        print(f"You have now read {self.pages_read}")


python101 = Book("Python 101", 50)
try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)
#  use the except statement above to send the error to the user in the form of a print