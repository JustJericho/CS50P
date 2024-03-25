def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numeric_list = []

    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha() : # Checks if the size is within limits
        for i in range(len(s)): # loop to check if there is a number within the plate
            if s[i].isnumeric(): # if a charactre is a number, save it's position
                numeric_list.append(i)
        if len(numeric_list) != 0:
            if int(s[numeric_list[0]]) != 0 and numeric_list == list(range(min(numeric_list), max(numeric_list)+1)) and numeric_list[len(numeric_list)-1] == len(s)-1:
                return True
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
