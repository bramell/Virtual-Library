from flask import Flask, jsonify
import json
import os

app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():
    return "This is a book API, use /books to get the list"



@app.route("/books", methods=["GET"])
def get_json_books():
    try:
        # Path to books.json from this file
        json_path = os.path.join(os.path.dirname(__file__), "books.json")

        # Open file
        with open(json_path, "r", encoding="utf-8") as file:
            books = json.load(file)

        return jsonify(books)
    
    except FileNotFoundError:
        return jsonify({"error": "books.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "books.json is not valid JSON"}), 500



# In bash type: python routes.py to run server on http://localhost:5000
if __name__ == "__main__":
    app.run(debug=True)