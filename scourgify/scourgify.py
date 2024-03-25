import csv
import sys

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    writer(sys.argv[2], reader(sys.argv[1]))

def reader(rfile):
    try:
        with open(rfile) as file:
            csvreader = csv.reader(file)

            students = []
            for row in csvreader:
                try:
                    row[0].strip()
                    row[1].strip()
                    student = {"first" : row[0].split(",")[1].replace(" ", ""), "last" : row[0].split(",")[0].replace(" ", ""), "house" : row[1]}
                    students.append(student)
                except IndexError:
                    continue
    except FileNotFoundError:
        sys.exit(f"Could not read {rfile}")

    return students



def writer(wfile, students):
    with open(wfile, 'w') as file:
        header = ['first', 'last', 'house']
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)

        for student in students:
            csvwriter.writerow([student['first'], student['last'], student['house']])


if __name__ == "__main__":
    main()