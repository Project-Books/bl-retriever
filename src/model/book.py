class Book:
    def __init__(self, title: str, languages: [str], publication_year: int, isbn13=None):
        self.title = title
        self.isbn13 = isbn13
        self.publication_year = publication_year
        self.languages = languages
