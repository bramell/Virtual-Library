from flask import Flask, jsonify, Response
import json
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
            return Response(
                json.dumps({"message": "No books found"}, 
                            ensure_ascii=False),
                            mimetype="application/json",
                            status=404
            )
        
        # Return JSON with Swedish chars enabled
        return Response(
            json.dumps(books, ensure_ascii=False, indent=4),
            mimetype="application/json"
        )
    
    except Exception as e:
        return Response(
            json.dumps({"error": str(e)}, ensure_ascii=False),
            mimetype="application/json",
            status=500
        )



# In bash type: python routes.py to run server on http://localhost:5000
if __name__ == "__main__":
    app.run(debug=True)