# # number=(int)(input("Enter the Number to check"))
# # if number%2==0:
# #     print("even")
# # else:
# #     print("odd")




# # number=5
# # facto=1
# # for i in range(1,number+1):
# #     facto*=i

# # print(facto)


# # 1,1,2,3,5,8,13,21

# # str_e="Hello"

# # print(str_e[4])


# # str_r="My name is Manthan"
# # str_r=str_r.split()
# # print(str_r)


# listofnumber=[23,35,242,11,56]

# # print(max(listofnumber))
# # print(min(listofnumber))

# listofnumber_1=reversed(listofnumber)
# print(list(listofnumber_1))


from ast import Not
import requests
import os
# image = requests.get(url="https://images.pexels.com/photos/1183099/pexels-photo-1183099.jpeg", stream=True)

# if image.status_code == 200:
# 	with open("downloaded_image.jpg", "wb") as f:
# 		f.write(image.content)
		
# else:
# 	print(f"Failed to download image: {image.status_code}")

# print(image)


# def func():

#     for i in range(5):
#         image = requests.get(url="https://picsum.photos/2000/3000")
#         if image.status_code == 200:
#             with open(f"file{i}.jpg", "wb") as f:
#                 f.write(image.content)
#             print(f"Saved file{i}.jpg")
#         else:
#             print(f"Failed to download image for file{i}.jpg: {image.status_code}")

# func()


# def fundelete():
#     for i in range(5):
#         os.remove(f"file{i}.jpg")
#         print("done")

# fundelete()
        

# expr = input("Enter expression: ")
# print("Result:", eval(expr))


# pi*r*r

# 1/2*hight*base

#  side*side

# length*width

# (p*r*t)/100

# cricket_score = {}
# n = int(input("Enter number of Players: "))
# i = 1

# while i <= n:
#     name = input("Enter Player Name ")
#     score = int(input("Enter Player Score of " + name + ": "))
#     cricket_score[name] = score
#     i = i + 1

# print(cricket_score)

# search_name = input("Enter Player's Name to get the score: ")
# if search_name in cricket_score:
#     print(search_name, "scored", 
# cricket_score[search_name], "runs")
    
# else:
#     print(search_name, "not found")


# mylist=[22]
# mylist.insert(0,40)
# print("Insert a value",mylist)

# mylist.append(10)
# mylist.append(20)
# mylist.append(30)
# print("After append",mylist)

# mylist.remove(30)
# print("After remove",mylist)

# lengths=len(mylist)
# print("After len",lengths)

# mylist.pop()
# print("After pop",mylist)

# mylist.clear()
# print("After clear",mylist)


# student = {
#     "id": 101,
#     "name": "Divya",
#     "age": 35,
#     "course": "Python"
#  }
# print("Original Dictionary:", student)
# # a. Print the dictionary items
# print("Dictionary Items:", student.items())

# # b. Access items (using key)
# print("Student Name:", student["name"])
# print("Student Age:", student["age"])

# # c. Use get()
# print("Course (using get):", student.get("course"))
# print("City (using get with default):", student.get("city", "Not Found"))

# # d. Change values
# student["age"] = 36
# print("Updated Dictionary after changing age:", student)

# # e. Use len()
# print("Total number of items in dictionary:", len(student))



# from datetime import datetime, timedelta
# today = datetime.now()
# days_to_add = 10

# new_date = today + timedelta(days=days_to_add)

# print("Today's Date:", today.date())

# print("Date after", days_to_add, "days:", new_date.date())

# N = int(input("Enter the value of N: "))
# series_sum = 0
# for i in range(2, N + 1):
#    series_sum += 1 / i
# print("Sum of the series 1/2 + 1/3 + ... + 1/{} = {:.4f}".format(N, series_sum))

# string = input("Enter a string: ")
# ch = input("Enter a character to count: ")
# count = 0
# for c in string:
#     if c == ch:
#         count += 1
# print("The character", ch, "occurs", count, "times in the string.")


import sqlite3

# connect to database
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")
conn.commit()

# insert data
cur.execute("INSERT INTO student(name, age) VALUES (?, ?)", ("Rahul", 20))
cur.execute("INSERT INTO student(name, age) VALUES (?, ?)", ("Priya", 22))
conn.commit()

# fetch data
print("\nStudents List:")
cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for r in rows:
    print(r)

# update data
cur.execute("UPDATE student SET age = ? WHERE name = ?", (25, "Rahul"))
conn.commit()


print("\nStudents List:")
cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for r in rows:
    print(r)

# delete data
cur.execute("DELETE FROM student WHERE name = ?", ("Priya",))
conn.commit()

print("\nStudents List:")
cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for r in rows:
    print(r)

# close database
conn.close()
