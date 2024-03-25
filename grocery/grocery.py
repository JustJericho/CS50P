food = []

while True:
    try:
        prompt = input()
        food.append(prompt)
    except EOFError:
        break


food.sort()

food_types = list(set(food))
food_types.sort()
print()

for x in food_types:
    print(food.count(x), x.upper())

