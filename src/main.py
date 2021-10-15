import csv


def read_csv():
    with open('../datasets/roald-dahl/records.csv', encoding='utf-8', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        print('Row: ' + str(rows))
        for row in rows:
            print(
                row['Content type'],
                row['Material type'],
                row['ISBN'],
                row['Name'],
                row['Role'],
                row['All names'],
                row['Title'],
                row['Variant titles'],
                row['Series title'],
                row['Country of publication'],
                row['Publisher'],
                row['Year of publication'],
                row['Edition'],
                row['Topics'],
                row['Genres'],
                row['Languages'],
                row['Notes'],
            )


if __name__ == '__main__':
    read_csv()

