import random
while True:
    try:
        prompt = int(input("Level: "))
        if prompt > 0:
            break
    except ValueError:
        pass

goal = random.randint(1,prompt)

while True:
    try:
        answer = int(input("Guess: "))
    except ValueError:
        continue
    if answer > goal:
        print("Too large!")
    elif answer < goal:
        print("Too small!")
    else:
        print("Just right!")
        break
