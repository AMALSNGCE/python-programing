class publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("the name of publisher is:",self.name)
class book(publisher):
    def __init__(self,name,title,author):
        publisher.__init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        print("Title of the book is =",self.title)
        print("author of the book is =",self.author)
class python(book):
    def __init__(self,name,title,author,prize,page_no):
        book.__init__(self,name,title,author)
        self.price=prize
        self.page_no=page_no
    def display(self):
        print("the name of publisher is:",self.name)
        print("Title of the book is =",self.title)
        print("author of the book is =",self.author)
        print("price of the book is =",self.price)
        print("no_of_page =",self.page_no)

p1=python("eric mathews","fluent python","luciano",879,700)
p1.display()