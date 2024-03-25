names = []
import inflect

p = inflect.engine()

while True:
    try:
        prompt = input().strip()
    except EOFError:
        break

    names.append(prompt)
printable_names = p.join(names)
print("Adieu, adieu, to", printable_names)
