math = input("Expression: ").split(" ")
math[0] = int(math[0])
math[2] = int(math[2])


match math[1]:

    case  "+":
        print("%.1f" % float(math[0] + math[2]))
    case "-":
        print("%.1f" % float(math[0] - math[2]))
    case "/":
        if math[2] != "0":
            print("%.1f" % float(math[0] / math[2]))
    case "*":
        print("%.1f" % float(math[0] * math[2]))
