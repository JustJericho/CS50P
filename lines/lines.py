import sys

def main():
    print(file_size())



def file_size(filename=sys.argv[1]):
    size = 0
    if len(sys.argv) != 2:
        sys.exit("Too many command-line arguments")
    elif filename.find(".py") == -1:
        sys.exit("Not a Python file")
    try:
        with open(filename) as file:
            for line in file:
                line.strip()
                if not(line[0] == "#"):
                    size = size + 1
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
    return size



if __name__ == "__main__":
    main()