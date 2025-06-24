from pymongo import MongoClient
import json

# Local/URI connection
client = MongoClient("mongodb://localhost:27017")

# Database and collection
db = client["library"]
collection = db["books"]



# Takes dict {title, author, isbn, year, tags}, 
def add_book(book_data): 
    # Validate data --> add book
    if book_data != {}:
        collection.insert_one(book_data)


# Returns a list of books (Note: ObjectId is not filtered out)
def get_all_books():
    return list(collection.find())



def delete_book(query):
    # Count the amount of books before and after removal 
    count_before = get_all_books()
    collection.delete_one({"title": query})
    count_after = get_all_books()

    # Comparison to see if the book is removed
    if len(count_before) > len(count_after):
        return "The book {title} was successfully removed".format(title=query)
    else: 
        return "The book could not be removed, did you spell it correctly?"
    


def delete_all_docs():
    collection.delete_many({})
    print("¤¤¤¤¤", collection, "¤¤¤¤¤")
    collection.find



'''
def search_books(query):
    1. Check if query is a str or int
    1. If str --> Use author to display all their books --> collection.find(query) --> return list
    2. If int --> Use ISBN number for unique search --> collection.find_one(query) --> return Author, Title, Year, Tag
'''


'''
def load_from_json():
    1. Read json-file
    2. Validate each book
    3. Add to database
'''


'''
def export_to_json():
    1. Get books from DB
    2. Remove or convert _id (ObjectId is not JSON compatible)
    3. Save list as JSON to file
'''