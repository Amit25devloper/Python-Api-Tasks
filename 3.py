mydata= {"category":[{"A":"FIRST","package":{"data":"2lacs"}},
        {"B":"Second","data":{"new":[100]}},
        {"C":"Third","Tests":[45,75,25]}]};

# Question A : print all keys
# for i in range(len(mydata)):
#     for j in range(len(mydata["category"][0:3].keys()):
#         print(len(mydata["category"][0:3].keys()))
     #print("KEYS :",mydata[i].keys[i])
#print(len(mydata))
# Question B : print count (number of ) keys

# Question 1 : print 2lacs
print("2 lakhs :",mydata["category"][0]["package"]["data"])
# Question 2 : print 25
print("25 :",mydata["category"][2]["Tests"][2])
# Question 3 : print 100
print("100 :",mydata["category"][1]["data"]["new"])