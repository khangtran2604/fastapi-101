class ProductNotFound(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)

class ProductAlreadyExists(Exception):
    def __init__(self, msg: str = "Product already exists!"):
        super().__init__(msg)
