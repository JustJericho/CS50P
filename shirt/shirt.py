from PIL import Image
from PIL import ImageOps
import sys


if len(sys.argv) > 3:
    sys.exit("Too many command line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command line arguments")

try:
    match sys.argv[1].split(".")[1]:
        case "png":
            extinput = '.png'
        case "jpg":
            extinput = '.jpg'
        case "jpeg":
            extinput = '.jpeg'
except IndexError:
    sys.exit("Invalid input")


try:
    match sys.argv[2].split(".")[1]:
        case "png":
            extoutput = '.png'
        case "jpg":
            extoutput = '.jpg'
        case "jpeg":
            extoutput = '.jpeg'
except IndexError:
    sys.exit("Invalid output")

if extoutput != extinput:
    sys.exit("Input and output have different extensions")

inputfile = Image.open(sys.argv[1])
shirtfile = Image.open("shirt.png")

croppedfile = ImageOps.fit(inputfile, shirtfile.size)
croppedfile.paste(shirtfile, mask = shirtfile)
croppedfile.save(sys.argv[2])