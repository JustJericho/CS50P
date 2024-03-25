import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        parts = ip.split(".")
        for i in range(0, len(parts)):
            if i == 0:
                if not re.search(r"^([2][5][0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[1-9][0-9]|[1-9])$", parts[i]):
                    return False
            else:
                if not re.search(r"^([2][5][0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[1-9][0-9]|[0-9])$", parts[i]):
                    return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
