class Library:
    def __init__(self):
        self.books = []
        self.no_of_book = 0

    def addBook(self,book):
        self.books.append(book)
        self.no_of_book = len(self.books)

    def showInfo(self):
        print(f"The library has {self.no_of_book}")
        

l1 = Library()
l1.addBook("Pokemon")
l1.addBook("Perman")
l1.addBook("Pickachu")
l1.showInfo()
for index,list in enumerate(l1.books):
    print(f"Book No {index+1} is {list}")

