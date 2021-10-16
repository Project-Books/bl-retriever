# This should match
# https://github.com/Project-Books/books-api/blob/main/src/main/resources/schema/publisher.graphqls
# without the ID
class Publisher:
    def __init__(self, name: str):
        self.name = name
        self.books = []
