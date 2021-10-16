import csv
import json

from src.model.author import Author
from src.model.book import Book


def read_csv():
    books_json = []
    # TODO: should the encoding be utf-8?
    with open('../datasets/roald-dahl/records.csv', encoding='ISO-8859-1', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        print('Row: ' + str(rows))
        for row in rows:
            title = row['Title']

            authors = [Author(row['Name'])]
            other_authors: str = row['All names']
            for name in other_authors.split(';'):
                authors.append(Author(name.strip()))

            languages = row['Languages']
            publishers = row['Publisher']
            publication_year = row['Year of publication']
            genres = row['Genres']
            isbn = row['ISBN']

            book = Book(title, authors, languages, publication_year, genres, publishers, isbn)
            books_json.append(book.to_json())
    return books_json


if __name__ == '__main__':
    books = read_csv()
    print()
    # pretty print for easier debugging
    print(json.dumps(books, indent=4))

