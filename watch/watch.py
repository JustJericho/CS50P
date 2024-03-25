import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        iframefinder = re.search(r'^<iframe.+</iframe>',s)
        linkfinder = re.search(r'https*://w*w*w*.*youtube.com/embed/\w{11}',iframefinder.string[slice(*iframefinder.span())])
        codefinder = re.search(r'\w{11}', s[slice(*linkfinder.span())])
        return "https://youtu.be/" + codefinder.string[slice(*codefinder.span())]
    except AttributeError:
        return None
    
if __name__ == "__main__":
    main()
