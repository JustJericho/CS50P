import random


def main():
    score = 0
    level = get_level()
    for i in range(0,10):
        intagers = generate_integer(level)
        x = intagers[0]
        y = intagers[1]
        for j in range(0,3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                if j != 2:
                    print("EEE")
                    continue
                else:
                    print("EEE")
                    print(f"{x} + {y} = {x+y}")
                    break
            if answer == x + y:
                score = score + 1
                break
            if j == 2 and answer != x + y:
                print("EEE")
                print(f"{x} + {y} = {x+y}")
                break
            elif j != 2 and answer != x + y:
                print("EEE")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            prompt = int(input("Level: "))
            if prompt == 1 or prompt == 2 or prompt == 3:
                return prompt
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        x = random.randint(0,10)
        y = random.randint(0,10)
    elif level == 2:
        x = random.randint(10,100)
        y = random.randint(10,100)
    else:
        x = random.randint(100,1000)
        y = random.randint(100,1000)
    return x,y


if __name__ == "__main__":
    main()
