import requests
import bs4


def get_bitcoin_price():
    result = requests.get("https://coinmarketcap.com/currencies/bitcoin/markets/")
    soup = bs4.BeautifulSoup(result.text, "lxml")
    bitcoin_price = soup.select(".priceValue > span")

    print(f"Current Bitcoin price: {bitcoin_price[0].text}")


if __name__ == "__main__":
    get_bitcoin_price()
