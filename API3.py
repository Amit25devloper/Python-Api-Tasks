import requests

url = requests.get("https://api.coinlore.net/api/tickers/")

response = url.json()


print("--1--")
# Using a for-loop, print every record from the data list in the API response.
DATA = response.get("data"),response.get("info")
for i in DATA:
    print(i)


print("--2--")
# Using a for-loop, print only the names of all cryptocurrencies.
Data = response.get("data")
for i in Data:
    print("CRYPTO CURRENCY NAMES :",i["name"])


print("--3--")
# Using a loop, print the index number along with each coin name.
count=0
for i in Data:
    count+=1
    print("Index_No :",count,"CURRENCY_NAMES :",i["name"])


print("--4--")
# Using a loop, print the coin name and symbol together for every record.
for i in Data:
    print("CURRENCY_NAMES :",i["name"],"\n","SYMBOL :",i["symbol"])


print("--5--")
# Using a loop, print the coin name and its price in USD.
for i in Data:
    print("CURRENCY_NAME :",i["name"],"\n","PRICE IN USD :",i["price_usd"])


print("--6--")
# Using a loop and a counter, print only the first 5 coins.
for i in Data[0:5]:
    print("FIRST FIVE CURRENCY_NAME :",i["name"])


print("--7--")
# Using a loop, print only the last 5 coins from the data list.
for i in Data[-5:]:
    print("LAST FIVE CURRENCY NAME :",i["name"])


print("--8--")
# Using a loop, print the coin name along with its rank value.

print("--9--")
# Using a loop, print the index number, name, symbol, and price for every coin.
for i in Data:
    print("RANK :",i["rank"]," ","CURRENCY NAME :",i["name"]," ","Symbol :",i["symbol"]," ","Price_USD :",i["price_usd"])


print("--10--")
# Using a loop, print only those coins that are present at even index positions.
count=0
for i in Data[0:100:2]:
    count+=2
    print("Even Index No. :",count,"Coin :",i["name"])


print("--11--")
# Using a loop, print only those coins that are present at odd index positions.
count=1
for i in  Data[1:100:2]:
    count+=2
    print("Odd Index No. :",count,"Coin :",i["name"])


print("--12--")
# Using a loop, print only the first and last record from the data list (without direct indexing).




print("--13--")
# Using a loop, print the names of coins from index positions 5 to 10.
for i in Data[5:10]:
    print("index :",len(i)," ","Currency Name :",i["name"])



print("--14--")
#  Using a loop, print each coin record with a separator line before and after it.
for i in Data:
    print("------") # before seprator
    print("Coin :"," ",i["name"])
    print("------") # after seprator


print("--15--")
# Using a loop, print only the key names of each cryptocurrency record, not the values.
for i in Data:
    print(i.keys())
