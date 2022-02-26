# create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book
# dictionary like library card(key : book , value : name of the person )
# craete a main function and run an infinite loop asking users for their input
import sqlite3
import random
conn_db = sqlite3.connect("librarydb.db")
class Library:
    def __init__(self, booklist, libraryname):
        self.booklist = booklist
        self.libraryname = libraryname
        self.dict = {}

    def display(self):
        print("We have following books in our library")
        books = conn_db.execute( '''
            select * from library 
        ''')
        for book in books:
            print(book)


    def lend_book(self, user, bookname):
       if bookname not in self.dict.keys():
        self.dict.update({bookname : user})
        print("lender-book database has been updated , you can take the book now")
       else:
            print("book is already being used by ",{self.dict[bookname]})


    def add_book(self,book ,author,price):
        #self.booklist.append(booktobeadded)
        conn_db.execute("insert into library  values (? , ? ,?)",(book , author , price) )

        conn_db.commit()


    def return_book(self, bookname):
        self.dict.pop(bookname)

if __name__ == '__main__' :
    list = ["harrypotter1", "beauty&thebeast", "darksoldier"]
    sublib = Library(list, "subhamlib")
    while(True):
        print("welcome , enter your choices")
        print("1.display book")
        print("2.Lend a book")
        print("3.Add a book")
        print("4.Return a book")
        user_choice = int(input())
        if user_choice ==1:
            sublib.display()
        elif user_choice == 2:
            book = input("enter the name of the book you want to lend")
            user = input("enter your name")
            sublib.lend_book(user , book )
        elif user_choice == 3:
            book = input("enter the name of the book you want to add")
            author = input("enter the name of the author")
            price = int(input("enter the price of the book"))
            sublib.add_book(book, author, price)
        elif user_choice == 4:
            book = input("enter the name of the book you want to return")
            sublib.return_book(book)
        else:
            print("wrong choice")
        print("enter w to exit and c to continue")
        inp2 = input()
        if inp2 == 'w':
            exit()
        elif inp2 == 'c':
            continue

