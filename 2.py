mydata= {
"maharashtra":{"mumbai":{"city":"metro city","metro":"yes"}, "population":"20 cr"},
"gujarat": ["AHMEDABAD","SURAT","RAJKOT"],
"rajasthan":["AJMER","JAISALMER",{"capital":"jaipur"},["MEWAD","RJ","INR"]]
}

# Question A : print all keys
print("all keys :",mydata.keys())
# Question B : print count (number of ) keys
print("TOTAL NO. OF KEYS :",len(mydata))
# Question 1 : print metro city
print("METRO CITY :",mydata["maharashtra"]["mumbai"]["city"])
# Question 2 : print jaipur
print("JAIPUR :",mydata["rajasthan"][2]["capital"])
# Question 3 : print Rajkot
print("RAJKOT :",mydata["gujarat"][2])
# Question 4 : print RJ
print("RJ :",mydata["rajasthan"][3][1])
