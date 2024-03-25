user_greeting = input("Greeting: ").strip().lower()

if user_greeting.find("hello") == 0:
    print("$0", end = "")
elif user_greeting.find("h") == 0:
    print("$20", end = "")
else:
    print("$100", end = "")