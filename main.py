from db import *

def menu():
    while True:
        print("\n", "---------- MENU ----------")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. View Collection")
        print("9. Delete All Books")
        print("0. Quit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            add_book_prompt()
        elif choice == 2:
            delete_book_prompt()
        elif choice == 3:
            view_collection()
        elif choice == 9:
            delete_all_docs_prompt()
        else:
            break



def add_book_prompt():
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN number: ")
    year = input("Year: ")
    tags = input("Tag/Category: ")

    book_data = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "tags" : tags
    }
    
    if book_data != {}:
        add_book(book_data)



def view_collection():
    print("\n", "---------- VIEW COLLECTION ----------", "\n")
    books = get_all_books()
    for book in books:
        print("Title: ", book["title"], "  ||  ", "Author: ", book["author"])
        print("-"*37)



def delete_book_prompt():
    title = str(input("\n", "Title of the book you want to delete: "))
    print("\n", delete_book(title))



def delete_all_docs_prompt():
    confirmation = input("Are you sure (y/n)? ")
    if confirmation == "y":
        delete_all_docs()
    else:
        pass

menu()