import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        divider = re.search(r'\bto\b',s)
        findA = re.search(r'\b([1-9]|1[0-2])\b',s[:divider.start()])
        typeA = re.search(r'\b(AM|PM)\b',s[:divider.start()])
        findB = re.search(r'\b([1-9]|1[0-2])\b',s[divider.start():])
        typeB = re.search(r'\b(AM|PM)\b',s[divider.start():])
        hour1,hour2 = (s[slice(*findA.span())] + s[slice(*typeA.span())], s[divider.start():][slice(*findB.span())] + s[divider.start():][slice(*typeB.span())])

        if hour1 == "12AM":
            hour1 = 0
        elif hour1 == "12PM":
            hour1 = 12
        elif hour1.endswith("AM"):
            hour1 = int(hour1.replace("AM", ""))
        else:
            hour1 = 12 + int(hour1.replace("PM", ""))

        if hour2 == "12AM":
            hour2 = 0
        elif hour2 == "12PM":
            hour2 = 12
        elif hour2.endswith("AM"):
            hour2 = int(hour2.replace("AM", ""))
        else:
            hour2 = 12 + int(hour2.replace("PM", ""))


        if hour1 > 24 or hour2 > 24:
            raise ValueError



        if hour1 < 10:
            hour1 = "0" + str(hour1)
        else:
            hour1 = str(hour1)


        if hour2 < 10:
            hour2 = "0" + str(hour2)
        else:
            hour2 = str(hour2)




        if s.find(":") == -1:

            return (hour1 + ":00" + " to " + hour2 + ":00")
        else:
            minfinder1 = re.search(r'\b(60|[0-5][0-9])\b', s[findA.end():divider.start()])
            minfinder2 = re.search(r'\b(60|[0-5][0-9])\b', s[divider.start():][findB.end():divider.start()]) # 9:30 AM to 7:50 PM

            min1 = "00"
            min2 = "00"

            if minfinder1 != None:
                min1 = s[minfinder1.start()+1:minfinder1.end()+1]

            if minfinder2 != None:
                min2 = s[divider.start():][minfinder2.start()+4:minfinder2.end()+4]


            print(min1, min2)

            if int(min1.replace(":", "")) >= 60 or int(min2.replace(":", "")) >= 60:
                raise ValueError

            return (hour1 + ":" + min1 + " to " + hour2 + ":" + min2)



    except AttributeError:
        raise ValueError
if __name__ == "__main__":
    main()
