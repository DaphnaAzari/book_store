from flask import Flask, render_template, request,redirect,session
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from user import User
from user_repository import UserRepository
from authenticated import is_authenticated
from login_required import login_required

# instantiate a Flask app object
app = Flask(__name__)

# this is added because in Flask the data is stored in a cookie that is sent back
#and forth between server and client, therefore we need a secret key to prevent malicious
#tampering
app.secret_key = "some_really_secret_key"


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
@login_required
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

# @app.route('/books', methods=['POST'])
# def create_book():
#   book_details = request.json
#   print(book_details)
#   return "created", 201
@app.route('/books', methods=['POST'])
#call loging required on this:
@login_required
def create_book():

#the below is not needed anymore as we do this in the waped login_required func:
    # if not is_authenticated(session):
    #     return redirect("/sessions/new")
    
    # make a new database connection
    connection = DatabaseConnection()
    connection.connect()

    # make a new instance of BookRepository
    book_repository = BookRepository(connection)

    # get the request body
    # book_details = request.json
    # updated to:
    book_details = request.form


    # my BookRepository expects an instance of Book, so make one here
    book = Book(title=book_details["title"], author=book_details["author"], release_date=book_details["release_date"])

    # save the book
    book_repository.create(book)

    # return a 201, which means "created"
    # return "created", 201
    # updated to a redirect after creation:
    return redirect("/books")



@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")


@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    print(f"user details: {user_details}")
    print(f"user details of use: {user_details["username"]}")
    user = User(username=user_details["username"], password=user_details["password"])
    print(f"user : {user}")
    user_repository.create(user)
    return redirect("/books")

@app.route('/sessions/new', methods=['GET'])
def get_login_form():
    return render_template("login_form.html")



@app.route('/sessions', methods=['POST'])
def create_session():
    #initializing a db connection
    connection = DatabaseConnection()
    #using the connect method on it to connect to db
    connection.connect()
    #initializing a connection with Userrepo
    user_repository = UserRepository(connection)
    #accessing the body of the request from the form and specifically
    #looking for these values
    username = request.form["username"]
    password = request.form["password"]
#calling the method that we made in user repo to find the user by their username
    user = user_repository.find_by_username(username)
#if the user exsists, and the password equals what we expect the store
#user.id and user.username in the sessions respectivly
    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
    #if all goes well, redirect user to /books, else redirect to try a new session again
        return redirect("/books")
    else:
        return redirect("/sessions/new")
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

