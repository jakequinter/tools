# Web scraper

A simple web scraper that fetches the current price of Bitcoin from [CoinMarketCap](https://coinmarketcap.com/).

> ⚠️ The css class that's used to grab this information may suddenly change. Update the script accordingly.

![A GIF showing the bitcoin command running in a terminal](https://user-images.githubusercontent.com/39658269/204101479-0ec2250f-e2c4-4b76-b7ec-3aa4085d6362.gif)

### Installing dependencies

```
$ pip install requests
$ pip install bs4
$ pip install lxml
```

### Running locally

```
$ git clone git@github.com:jakequinter/tools.git
$ cd tools/web
$ python scraper.py
```

### Configuring terminal command

I created a command so I can just run `bitcoin` in my terminal and it will run this script. To do so, update your `.zshrc` file to include the following:

```
bitcoin() {
    python path/to/directory/scraper.py “$1”
}
```
