from user import User

class UserRepository:

    # initialise with a database connection
    def __init__(self, connection):
        self._connection = connection


    def create(self, user):
        print(f"user: {user}")
        self._connection.execute(
            'INSERT INTO users (username, password) VALUES (%s, %s)',
            [user.username, user.password]
        )
        return None
