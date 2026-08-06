from flask import Flask, render_template
from database_connection import DatabaseConnection
from book_repository import BookRepository

# instantiate a Flask app object
app = Flask(__name__)

# NEW PART START

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

@app.route('/books', methods = ['GET'])
def get_all_books():
    # make a connection instanse/ instantiating:
    connection = DatabaseConnection()
    #open it: (calling on .connect that is in the database_connection.py file)
    connection.connect()
    # give the connection to the repository:
    book_repository = BookRepository(connection)
    #repository uses the connection internally to run SQL, 
    # #by calling the all() method from the repo file
    books = book_repository.all()
    # print(books)
    return render_template("books.html", books=books)

# @app.route("/books", methods=["GET"])
# def books():
#     return render_template("books.html")


# @app.route('/books-json', methods=['GET'])
# def getBooks():
#     return [
#     {
#         "title": "The Gruffalo",
#         "author": "Julia Donaldson"
#     },
#     {
#         "title": "Ada Twist, Scientist",
#         "author": "Andrea Beaty"
#     },
#     {
#         "title": "The Girl Who Drank the Moon",
#         "author": "Kelly Barnhill"
#     },
#     {
#         "title": "Dragons in a Bag",
#         "author": "Zetta Elliott"
#     }
#     ]

@app.route("/authors", methods=["GET"])
def authors():
    return render_template("authors.html")

@app.route('/authors-json', methods=['GET'])
def getAuthors():
    return [
    {
        "name": "Julia Donaldson",
        "dob": "1948-09-16"
    },
    {
        "name": "Andrea Beaty",
        "dob": "1961-10-08"
    },
    {
        "name": "Kelly Barnhill",
        "dob": "1973-01-01"
    },
    {
        "name": "Zetta Elliott",
        "dob": "1979-11-11"
    }
    ]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    # app.run(port=5001, debug=True)
     app.run(host="0.0.0.0", port=5001, debug=True)

