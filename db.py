from pymongo import MongoClient
import json
import os

# Local/URI connection
client = MongoClient("mongodb://localhost:27017")

# Database and collection
db = client["library"]
collection = db["books"]



''' Takes dict {title, author, isbn, year, tags} '''
def add_book(book_data): 
    # Validate data --> add book
    if book_data != {}:
        collection.insert_one(book_data)
        add_book_json(book_data)



''' Returns a list of books ''' 
# (Note: ObjectId is not filtered out)
def get_all_books():
    return list(collection.find())



''' Function for deleting all database entries '''
def delete_all_docs():
    collection.delete_many({})

    # Check if deletion was successful by retrieving and counting the collection from get_all_books()
    return "\n All entries deleted \n" if len(get_all_books()) <= 0 else "\n Could not remove any books \n" # Practicing ternary operators



''' Function for deleting one book '''
def delete_book(query):
    #Get the title of the book - only for confirmation message to user (instead of getting the ISBN nr)
    title = search_books(query)

    # Count the amount of books before and after removal
    count_before = get_all_books()
    collection.delete_one({"isbn": query})
    remove_book_from_json(query)
    count_after = get_all_books()

    # Comparison to see if the book is removed
    if len(count_before) > len(count_after):
        return "-- The book {title} was successfully removed --".format(title=title["title"]) # title["titel"] = the return value from search_books()
    else: 
        return "-- The book could not be removed, did you enter the correct ISBN-number (lower back of the book)? --" # Too long for ternary op, harder to read



''' Find several books by author or one by ISBN '''
def search_books(query):
    #If query == int (ISBN) --> display one book (ISBN = unique)
    if all(char.isdigit() or char == '-' for char in query):
        return collection.find_one({"isbn": query})

    # Search for all books by the author (case-sensitive)
    else:
        # $regex: f"^{query}$" searches for the exakt match
        return list(collection.find({"author": {"$regex": f"^{query}$", "$options": "i"}})) #   ^ = beginning of string, $ = end of string

        

''' Function to sync added book between database and json file '''
def add_book_json(new_book):
    json_path = os.path.join(os.path.dirname(__file__), "books.json")

    try:
        # Read existing books
        with open(json_path, "r", encoding="utf-8") as f:
            books = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

    # Remove MongoDBs ObjectId - Raises TypeError: Object of type ObjectId is not JSON serializable
    if "_id" in new_book:
        del new_book["_id"]

    # Add the new book
    books.append(new_book)

    # Write to file
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)



''' Function to sync deleted book between database and json file '''
def remove_book_from_json(deleted_book):
    json_path = os.path.join(os.path.dirname(__file__), "books.json")

    try:
        # Read existing books
        with open(json_path, "r", encoding="utf-8") as f:
            books = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

    # Removes the book with matching ISBN and adds the rest of the books to a new list
    updated_books = []
    for book in books:
        if book.get("isbn") != deleted_book.get("isbn"):
            updated_books.append()
    
    books = updated_books # Update the old list

    # Write to file
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)