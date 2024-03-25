user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
if user_answer == "42" or user_answer == "forty two" or user_answer == "forty-two":
    print("Yes")
else:
    print("No")