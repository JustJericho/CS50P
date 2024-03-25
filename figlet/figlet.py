from pyfiglet import Figlet
import sys
import random
from statistics import random

if len(sys.argv) == 3:
    if sys.argv[2] in Figlet().getFonts() and ( sys.argv[1] == "-f" or sys.argv[1] == "--font" ):
        prompt = input("Input: ")
        f = Figlet(font=sys.argv[2])
        print(f.renderText(prompt))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    prompt = input("Input: ")
    f = Figlet(font=Figlet().getFonts()[random.randint(0,424)])
    print(f.renderText(prompt))
else:
    sys.exit("Invalid usage")
