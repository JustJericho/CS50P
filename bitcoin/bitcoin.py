import requests
import sys

try:
    multiplier = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

try:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = (requests.get(url)).json()
except requests.RequestException:
    sys.exit("Request Exception")


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = (requests.get(url)).json()
value = float(response["bpi"]["USD"]["rate"].replace(",", ""))

value_adjusted = str(multiplier * value)
value_adjusted = (
    value_adjusted[: (value_adjusted.find(".") - 3)]
    + ","
    + value_adjusted[(value_adjusted.find(".") - 3) :]
)

print("$" + value_adjusted)
