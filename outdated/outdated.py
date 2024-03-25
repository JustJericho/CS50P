months = {
    "January" : "01",
    "February": "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

while True:
    try:
        prompt = input("Date: ").strip()

        if prompt.find("/") != -1:
            month = prompt.split("/")[0]
            day = prompt.split("/")[1]
            year = prompt.split("/")[2]

            if 0 > int(month) or int(month) > 12 or 0 > int(day) or int(day) > 31:
                continue

            if int(month) < 10:
                month = "0" + month
            if int(day) < 10:
                day = "0" + day

            print(year, month, day, sep = "-")
            break


        month = prompt.split(",")[0].split(" ")[0]
        day = prompt.split(",")[0].split(" ")[1]
        year = prompt.split(",")[1].strip()

        if int(months[month]) > 12 or int(day) > 31:
            continue

        if int(day) < 10:
                day = "0" + day


        print(year, months[month], day, sep = "-")
        break

    except IndexError:
        pass

    except KeyError:
        pass

    except ValueError:
        pass

