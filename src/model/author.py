# This should match
# https://github.com/Project-Books/books-api/blob/main/src/main/resources/schema/author.graphqls
# (without the ID)
class Author:
    def __init__(self, name):
        self.full_name = name
        self.about = ''
        self.books = []

