from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["library"]
collection = db["books"]



def get_all_books():
    """ Returns all books as a list of dictionaries """
    return list(collection.find({}, {"_id": 0})) #Exclude MongoDB's _id



@app.route("/", methods=["GET"])
def home():
    return "This is a book API, use /books to get the list"



@app.route("/books", methods=["GET"])
def get_books():
    try:
        books = get_all_books()
        if not books:
            return jsonify({"message": "No books found"}), 404
        return jsonify(books)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# In bash type: python routes.py to run server on http://localhost:5000
if __name__ == "__main__":
    app.run(debug=True)