class UserNotFoundException(Exception):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f"User with ID {self.user_id} not found in the database"