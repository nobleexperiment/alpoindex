import urllib.request, urllib.parse, urllib.error
import json

# requirement:		Use an API Key from alphaadvantage.co
# url structure: 	"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=[myownapikey]"
# language: 			python3.5.7
# output:		      display the closing price & volume of a publicly traded company in the NYSE / NASDAQ / OTC

def TickerClose(symb):

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=demo".format(symb)

    stockdata = urllib.request.urlopen(url)
    data = stockdata.read().decode()

    js = json.loads(data)

    jstring = 'Time Series (Daily)'

    for entry in js:
        i = js[jstring].keys()

        for jkeys in i:
            return (jkeys,
                js[jstring][jkeys]['1. open'],
                js[jstring][jkeys]['2. high'],
                js[jstring][jkeys]['3. low'],
                js[jstring][jkeys]['4. close'],
                js[jstring][jkeys]['5. volume'])

# query multiple times, just to print one item?
print('open',TickerClose('GS')[1])
print('high',TickerClose('GS')[2])
print('low',TickerClose('GS')[3])
print('close',TickerClose('GS')[4])
print('volume',TickerClose('GS')[5])
