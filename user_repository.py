from user import User

class UserRepository:

    # initialise with a database connection
    def __init__(self, connection):
        self._connection = connection


    def create(self, user):
        # print(f"user: {user}")
        self._connection.execute(
            'INSERT INTO users (username, password) VALUES (%s, %s)',
            [user.username, user.password]
        )
        return None

    def find_by_username(self, username):
        user_details =self._connection.execute(
            'SELECT * FROM users WHERE username = %s',[username]
        )[0]

        return User(
            user_details["username"],
            user_details["password"],
            user_details["id"]
        )