from src.model.author import Author
from src.model.publisher import Publisher


class Book:
    def __init__(self, title: str, authors: [Author], languages: [str], publication_year: int,
                 genres: [str], publishers: [Publisher], isbn13=None):
        self.title = title
        self.isbn13 = isbn13
        self.genres = genres
        self.year_of_publication = publication_year
        self.authors = authors
        self.languages = languages
        self.publishers = publishers
