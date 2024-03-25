terminal_input = input("Input: ")
terminal_output = ""
i = 0

for x in terminal_input:
    i = i + 1
    if x != "i" and x != "a" and x != "e" and x != "o" and x != "u" and x != "A" and x != "E" and x != "I" and x != "O" and x != "U":
        terminal_output = terminal_output + x
print("Output: " + terminal_output)