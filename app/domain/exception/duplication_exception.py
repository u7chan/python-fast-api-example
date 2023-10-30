class DuplicationException(Exception):
    message = "The account with the login id already exists."

    def __str__(self):
        return DuplicationException.message
