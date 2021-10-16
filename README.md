# British Library Retriever

All data is retrieved from the British Library. See their [collection metadata](https://www.bl.uk/collection-metadata). We have made small modifications to the data as part of our data cleaning process.

The Book Retriever reads the data as a CSV file and converts it into our JSON payload that will be used for adding new book-related data in our GraphQL [Books API](https://github.com/Project-Books/books-api). This can later be expanded to become a web app, rather than a console application, to remove the manual step of needing to call our mutations separately.
