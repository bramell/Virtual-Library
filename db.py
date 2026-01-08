from pymongo import MongoClient

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



''' Returns a list of books ''' 
# (Note: ObjectId is not filtered out)
def get_all_books():
    return list(collection.find())



''' Function for deleting all database entries '''
def delete_all_docs():
    collection.delete_many({})

    # Check if deletion was successful by retrieving and counting the collection from get_all_books()
    return "\n All entries deleted \n" if len(get_all_books()) == 0 else "\n Could not remove any books \n" # Practicing ternary operators



''' Function for deleting one book '''
def delete_book(query):
    #Get the title of the book - only for confirmation message to user (instead of getting the ISBN nr)
    title = search_books(query)
    if not title:
        return "-- The book could not be found. Check the ISBN number. --"

    # Count the amount of books before and after removal
    count_before = get_all_books()
    collection.delete_one({"isbn": query})
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
        # ^ = beginning of string, $ = end of string
        # options: i = case sensitive matching enabled, "Ape" matches with "APE" & "ape" too
        return list(collection.find({"author": {"$regex": f"^{query}$", "$options": "i"}})) 