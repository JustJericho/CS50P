while True:
    try:
        prompt = input("Fraction: ")

        num_1 = int(prompt.split("/")[0])
        num_2 = int(prompt.split("/")[1])
        if num_1 < num_2 and num_1 >= 0 and num_2 > 0:
            if int((num_1 / num_2) * 100 ) <= 1:
                print("E")
            elif int((num_1 / num_2) * 100 ) >= 99:
                print("F")
            else:
                print( int((num_1 / num_2) * 100), "%", sep = '' )
        elif num_1 == num_2 and num_1 != 0:
            print("F")
        else:
            continue
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
