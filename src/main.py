import csv


def read_csv():
    with open('../datasets/roald-dahl/records.csv', encoding='utf-8', newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=' ',quotechar='|')
        print('Row: ' + str(rows))
        for row in rows:
            print(', '.join(row))


if __name__ == '__main__':
    read_csv()

