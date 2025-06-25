import re
from db import *


''' Interface menu to navigate the program. '''
def menu():
    while True:
        print("\n", "---------- MENU ----------")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. View Collection")
        print("4. Search books")
        print("9. Delete All Books")
        print("0. Quit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            add_book_prompt()
        elif choice == 2:
            delete_book_prompt()
        elif choice == 3:
            view_collection()
        elif choice == 4:
            search_books_prompt()
        elif choice == 9:
            delete_all_docs_prompt()
        else:
            break

        print("")



''' Ask the user for inputs, validate and send to database. '''
def add_book_prompt():
    print("\n", "---------- ADD A BOOK ----------", "\n")
    validated = False

    while not validated:
        # Titles can be any characters or numbers so no validation here.
        title = input("Title: ")

        # Using re to allow special characters but prevent empty strings or @123 characters
        author = input("Author: ")
        if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\- ]+", author): # Syntax: re.fullmatch(pattern, string)
            print("Author name can only contain letters, hyphens, and spaces.")
        
        # Using whitelist to check for illegal characters, can't use isdigit due to '-' char
        # ¤¤¤   Add format checking     ¤¤¤
        whitelisted_chars = "0123456789-"
        isbn = input("ISBN number: ")
        if any(char not in whitelisted_chars for char in isbn):
            print("ISBN must be numbers and in format: xxx-xx-x-xxxxxx-x (- is allowed)")
            continue
        
        # Using isdigit to check that input is an integer
        year = input("Year: ")
        if year.isdigit() == False:
            print("Year needs to be a number")
            continue
        
        # Tags could technically be anything, but only categories in string format are preferred.
        tags = input("Tag/Category: ")
        if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\- ]+", author):
            print("A tag has to be text, not numbers or special characters")
        
        # If all data is ok, set validate to True
        validated = True
        if validated:
            book_data = {
            "title" : title,
            "author" : author,
            "isbn" : isbn,
            "year" : year,
            "tags" : tags
        }
        
        # Ensure that book_data isn't an empty dict --> send dict to db.py
        if book_data != {}:
            add_book(book_data)
    


''' Function for printing the collection '''
def view_collection():
    print("\n", "---------- VIEW COLLECTION ----------", "\n")
    books = get_all_books()
    for book in books:
        print("Title: ", book["title"], "  ||  ", "Author: ", book["author"], "  ||  ", "ISBN: ", book["isbn"])
        print("-"*100)



''' Function that takes an input to send to db.py for deletion '''
def delete_book_prompt():
    print("")
    print("\n", "---------- DELETE A BOOK ----------", "\n")
    # Does not have to be ISBN, but since it's unique it's good for removing the right book if duplicates with different ISBN numbers have been entered
    # If any other more common variable like "year" is used, the first found entry/document will be deleted from the db
    
    isbn = input("ISBN number of the book you want to delete: ") 

    # Using whitelist to check for illegal characters, can't use isdigit due to '-' char
    whitelisted_chars = "0123456789-"
    if any(char not in whitelisted_chars for char in isbn):
        print("ISBN must be numbers and in format: xxx-xx-x-xxxxxx-x (- is allowed)")

    # Execute the function and print the return statement
    else:
        print("\n", delete_book(isbn))



''' Function to delete all entries to the database '''
def delete_all_docs_prompt():
    print("\n", "---------- DELETE ALL BOOKS ----------", "\n")
    confirmation = input("NOTE: This action can't be undone. Are you sure (y/n)? ")
    if confirmation == "y":
        # Execute the function and print the return statement
        print(delete_all_docs()) 
    else:
        pass



''' Function to search for all books by author or one by ISBN '''
def search_books_prompt():
    print("\n", "---------- SEARCH BOOKS ----------", "\n")
    query = input("Enter the name of an author for all their books or an ISBN number for one book (with format: xxx-xx-x-xxxxxx-x): ")
    
    print(search_books(query))


menu()