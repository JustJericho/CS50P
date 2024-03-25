terminal_entry = input("Camel Case:")
snake_case = ""

for x in terminal_entry:
    if x.isupper():
        snake_case = snake_case + "_" + x.lower()
    else:
        snake_case = snake_case + x

print(snake_case)