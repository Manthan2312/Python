# disct={
#     "Name":"Manthan",
#     "Age":20,
#     "Born Place":"Vadnagar"
# }
# print(disct)

# print(disct["Name"])
# print(disct["Age"])
# print(disct["Born Place"])



# print(disct.get("name")) # if you use the .get if key does not exstis in disctionary so it will return none other wise direct access will throw errors

# # key:value that is dictionary
# # key is unique and value can be any data type


# print(disct.keys())  #if you want the direct access of the keys

# print(disct.values()) #if you want the direct access of the value

# print(disct.items())  #if you want the key and value together that time you do this 


# for i in disct.keys():
#     print(disct[i])   #print the value of the disctionary


# disct1={"Name":"Manthan",
#         "Age":"20",
#         "Position":"Owner",
#         "Net Worth":"2434242"}


# disct2={"Name":"Khushbu",
#         "Age":"20",
#         "Position":"Owner Of Manthan"}

# disct1.update(disct2)   # update the value of the key if both had same key 
# print(disct1)



# disct3={12:1323,
#         44:4343,
#         54:445
#         }

# disct4={14:3422,
#         67:3332,
#         65:5454}


# disct3.update(disct4)
# print(disct3)        # if both are not the same key update the full in short term append the whole dictionary

# print(disct4)
# # disct4.clear()
# # print(disct4) #clear the dictionary

# print(disct4.pop(65))   #enter the key pop find or popped it's value 

# disct3={12:1323,
#         44:4343,
#         54:445
#         }

# print(disct3.popitem())   # popitems remove the  last key and value of the dictionary
# print(disct3)


# del disct3[44]
# print(disct3)    #if you are using the del keyword with key that time it delete that particular key and it's value  but del not finds key delete entire dictionary




for i in range(1,11):
    print(i)
    if i==5:
        break;
else:
    print("Loop is over")    # IF THE LOOP IS WORK BEGINNING TO END THAT TIME ELSE BLOCK EXCUTED OTHWERWISE 
    #ELSE LOOP BREAK THAT TIME IT IS DOES NOT WORK OR EXCUTED THE ELSE BLOCK


    