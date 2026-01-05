import requests

url = requests.get("https://openlibrary.org/subjects/science_fiction.json")

response = url.json()

# print(response)
# print("keys :",response.keys())

print("--1--")
# Print the total number of keys present in the processed book record.
count=0
for i in response:
    count += 1
print("total keys :",count)


print("--2--")
# Print the complete list of key names available inside the record.
for i in response:
    print(i)


print("--3--")
# Print the datatype of every key present in the processed record.
for i in response["works"]:
    print("==================START OF RECORD OUTPUT =======================")
    print("Book Name",i["title"])
    print("Authors",i["authors"])
    print("First_Publish_Year :",i["first_publish_year"])
    print("edition_count :",i["edition_count"])
    print("Unique Identifier :",i["lending_identifier"])
    print("==================END OF RECORD OUTPUT =======================")