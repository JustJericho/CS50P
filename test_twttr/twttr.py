import sys

def main():
    prompt = input("Input: ")
    returned_prompt = shorten(prompt)
    print("Output: " + returned_prompt)


def shorten(word="dq"):
    try:
        word.split()
    except AttributeError:
        sys.exit("Incorrect query")

    if word == "dq":
        sys.exit("Incorrect query")

    word = word.replace("a", "")
    word = word.replace("e", "")
    #word = word.replace("i", "")
    #word = word.replace("o", "")
    #word = word.replace("u", "")
    #word = word.replace("A", "")
    #word = word.replace("E", "")
    #word = word.replace("I", "")
    word = word.replace("O", "")
    word = word.replace("U", "")
    word = word.replace("3", "")
    word = word.replace("C", "c")
    word = word.replace(".", "")

    return word


if __name__ == "__main__":
    main()
