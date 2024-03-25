def main():
    user_inp = input("What time is it? ")
    time = convert(user_inp)

    if 8 >= time >= 7:
        print("breakfast time")
    elif 13 >= time >= 12:
        print("lunch time")
    elif 19 >= time >= 18:
        print("dinner time")



def convert(time):
    time_converted = int(time.split(":")[0]) + (int(time.split(":")[1]))/60
    return time_converted

if __name__ == "__main__":
    main()
