class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title


    def __str__(self):
        return f'{self.author} {self.title}'     

book_one = Book('Rahma', 'Rahma and her success')
print(str(book_one))
