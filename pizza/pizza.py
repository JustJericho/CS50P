from tabulate import tabulate
import csv
import sys

def read_file(file_name):
    with open(file_name, newline = '') as file:
        csv_reader = csv.reader(file)
        table = []
        file_headers = []
        for line in csv_reader:
            if csv_reader.line_num != 1:
                table.append(line)
            else:
                file_headers = line
        print(tabulate(table,headers = file_headers, tablefmt = "grid"))


def main():
    checker()
    read_file(sys.argv[1])




def checker():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].find(".csv") == -1:
        sys.exit("Not a csv file")

if __name__ == "__main__":
    main()