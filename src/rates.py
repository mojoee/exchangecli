import requests
import argparse
from config import Config

argParser = argparse.ArgumentParser()
argParser.add_argument("-B", "--base", help="choose a certain base")
argParser.add_argument("-T", "--target", help="choose a certain target currency")

args = argParser.parse_args()

appID = Config.appID
selectedBase = args.base
targetCurrency = args.target
url = f"https://openexchangerates.org/api/latest.json?app_id={appID}&base={selectedBase}"

response = requests.get(url)
print(response)
print(f"Base {response.json()['base']}")
print(f"ExchangeRate {selectedBase}:{targetCurrency}|1:{response.json()['rates'][targetCurrency]}")