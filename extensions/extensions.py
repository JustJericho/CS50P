user_input = input("File name: ").strip().lower()
user_ext = user_input[user_input.rfind("."):len(user_input)]

match user_ext:

    case ".jpg":
        print("image/jpeg")

    case ".jpeg":
        print("image/jpeg")

    case ".gif": # pronounced with a G as in Google BTW
        print("image/gif")

    case ".png":
        print("image/png")

    case ".pdf":
        print("application/pdf")

    case ".txt":
        print("text/plain")

    case ".zip":
        print("application/zip")

    case _:
        print("application/octet-stream")