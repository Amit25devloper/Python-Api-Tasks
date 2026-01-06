mydata = [{"states":["GUJARAT","RAJASTHAN",
                     {"PORTION":"WEST INDIA"},
                     {"LANGUAGES":["GUJARATI","MARWADI",["HINDI","ENGLISH"]]}]},
            {"CODES":{"GUJARAT":"GJ","RAJASTHAN":"RJ"}},["7.07 CR","8.5 CR"]]
# PRINT TOTAL NUMBER OF MAIN KEYS
total =0
for i in range(0,len(mydata)):
    total += i
    if i==2:
        break;
print("total no. of keys :",total)
# PRINT NAME OF ALL MAIN KEYS
for i in range(0,len(mydata)):
    if i==2:
        break;
    print("total no. of keys :",mydata[i].keys())

# print gj
print(mydata[1]["CODES"]["GUJARAT"])

# PRINT GUJRAT
print("GUJRAT :",mydata[0]["states"][0])

#PRINT GUJRAT
print("GUJRAT :",mydata[1]["CODES"])

# PRINT MARWADI
print("MARWADI :",mydata[0]["states"][3]["LANGUAGES"][1])
# PRINT ENGLISH
print("ENGLISH :",mydata[0]["states"][3]["LANGUAGES"][2][1])
# PRINT WEST INDIA
print("WEST INDIA :",mydata[0]["states"][2]["PORTION"])
# PRINT 7.07 CR
print(mydata[2][0])
