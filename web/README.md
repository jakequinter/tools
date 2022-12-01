# Bitcoin price

Grab the the current price of Bitcoin by scraping [CoinMarketCap](https://coinmarketcap.com/) or by hitting the [Strike API](https://strike.me/developer/).

![A GIF showing the bitcoin command running in a terminal](https://user-images.githubusercontent.com/39658269/205134281-9b7476aa-a856-4a59-8c06-9d82bdf908d0.gif)

> ⚠️ The css class that's used to grab the CoinMarketCap data may suddenly change. Update the script accordingly.

### Setup

Rename the `.env.example` to `.env` and add your Strike API key.

### Installing dependencies

```
$ pip install requests
$ pip install bs4
$ pip install lxml
$ pip install python-dotenv
```

### Running locally

```
$ git clone git@github.com:jakequinter/tools.git
$ cd tools/web
$ python main.py
```

### Configuring terminal command

I created a command so I can just run `bitcoin` in my terminal and it will run this script. To do so, update your `.zshrc` file to include the following:

```
bitcoin() {
    python path/to/directory/main.py “$1”
}
```
