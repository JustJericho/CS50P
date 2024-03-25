def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction):
    num1 = int(fraction.split("/")[0])
    num2 = int(fraction.split("/")[1])
    if num1 > num2:
        raise ValueError
    
    return int((num1/num2) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()