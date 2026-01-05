import requests
url = requests.get("https://api.openbrewerydb.org/v1/breweries")
response = url.json()

# print(response)

print("--1--")
# Fetch one brewery record
for i in response:
    print("================ BREWERY INFORMATION REPORT =================")
    print("Brewery Name :",i["name"])
    print("Brewery Type :",i["brewery_type"])
    print("City :",i["city"])
    print("Country :",i["country"])
    print("Website URL :",i["website_url"])
    print("================ END OF RECORD ============================")
    break


print("--2--")
# Count total keys
count=0
for i in response:
    count+=1
print("Total No. of Keys :",count)


print("--3--")
# Print key names using loop
for i in response:
    print("Key Name =",i.keys())

