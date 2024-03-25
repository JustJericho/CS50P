menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0

while True:
    try:
        prompt = input("Item: ").lower()
        total = total + menu[prompt]
        print("Total: $",total,"0", sep = '')
    except KeyError:
        pass
    except EOFError:
        print()
        break