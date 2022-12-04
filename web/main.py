import requests
import os
import bs4
from dotenv import load_dotenv

load_dotenv()

STRIKE_API_KEY = os.getenv('STRIKE_API_KEY')


def get_coinmarkcap_price():
    result = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
    soup = bs4.BeautifulSoup(result.text, "lxml")
    bitcoin_price = soup.select(".priceValue > span")
    
    print(f'Current Bitcoin price: {bitcoin_price[0].text}')


def get_strike_price():
    url = 'https://api.strike.me/v1/rates/ticker'
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {STRIKE_API_KEY}',
    }

    response = requests.request('GET', url, headers=headers, data=payload)
    data = response.json()
    strike_price = data[0]['amount']

    print("Current Bitcoin price: $" + "{:,}".format(float(strike_price)))


if __name__ == '__main__':
    while True:
        try:
            print('1. CoinMarketCap\n2. Strike')
            user_input = int(input('Choose an option: '))

            if user_input == 1:
                get_coinmarkcap_price()
                break
            elif user_input == 2:
                get_strike_price()
                break
        except:
            print('Invalid option.')
