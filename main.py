import requests

def main(params):
    currency = params.get("currency", "RUB")
    response = requests.get("https://belarusbank.by/api/kursExchange").json()
    value = response[0][f"{currency}_out"]
    return {f"{currency}": value}