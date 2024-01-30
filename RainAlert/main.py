import requests

def perecentage(number1, number2):
    return (number1/number2)*10

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameter = {
    'STOCK': STOCK,
    'COMPANY_NAME': COMPANY_NAME
}
parameter1 = {
    'q': COMPANY_NAME,
    'apiKey': '0a1ffa394a5b4d9e82e2ba588385cb4b'
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=3T2HD9EYXIOAMGYE")
response.raise_for_status()
response2 = requests.get(NEWS_ENDPOINT, params=parameter1)
data = response.json()
news_data = response2.json()
percentage_value = perecentage(float(data["Time Series (60min)"]["2023-11-28 19:00:00"]["4. close"]), float(data["Time Series (60min)"]["2023-11-29 04:00:00"]["1. open"]))
if percentage_value >= 10:
    print(news_data["articles"][0:2])

