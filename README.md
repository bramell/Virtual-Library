## Virtual Library

A Python-project for managing a database for books using MongoDB and a JSON-based API through Flask. 
Add, remove and get books though the terminal or a REST API.
This is meant as a practice and was done in my spare time.

---

## Functionality

- Add books (title, author, ISBN, year, category)
- Remove books through ISBN
- Syncronisation betweeem MongoDB och `books.json`
- JSON-based export of the whole database.
- REST API with Flask:
  - `GET /books` – get all books.

---

## Project Structure

book_api/  
    --main.py           # Command-line-interface (CLI)  
    --db.py             # Database logic (MongoDB + JSON-synk)  
    --routes.py         # Flask-API  
    --books.json        # Synced JSON-file with all books  
    --requirements.txt  # Dependencies  
    --README.md         # Documentation  

---

## Instructions

1. Clone the project:
   Bash: git clone https://github.com/bramell/Virtual-Library.git

2. Install Dependencies:
   pip install -r requirements.txt

3. Run:
   Bash: python main.py
   Follow the instructions from the program to:
   - Add a book
   - Delete a book
   - List all added books
   - Search for an added book
   - Delete all entries
   - Quit the program

---

## API - Flask

- Bash: python routes.py
- http://localhost:5000/ - A welcome message
- http://localhost:5000/books - To access books.json/API


When you add a book via CLI:
It is saved to the database and added to books.json

When you remove a book:
It is removed from the database and removed from books.json

---

## Future Development

- GET /books/<isbn> to retrieve a book via API
- POST, PUT, DELETE endpoints
- Authentication and permissions
- Frontend (e.g. React or Svelte)