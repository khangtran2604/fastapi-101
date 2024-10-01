class UserNotFound(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)

class UserAlreadyExists(Exception):
    def __init__(self, msg: str = "User already exists!"):
        super().__init__(msg)
