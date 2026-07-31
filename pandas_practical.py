
import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
#

#2
# marks=pd.Series([70,80,90])
# print(marks)
# print(marks.shape)
# print(marks.size)
# print(marks.dtype)

#3
# Custom_Series=pd.Series(
#     ([75,82,91]),
#     index=(["Math","Science","English"])
# )
# print(Custom_Series)

#4
# Custom_Series=pd.Series(
#     ([75,82,91]),
#     index=(["Math","Science","English"])
# )
# print(Custom_Series["Math"])
# print(Custom_Series["English"])

#5

# sales=pd.Series([1200,1500,1800,1600])
# print(sales.sum())
# print(sales.mean())
# print(sales.max())
# print(sales.min())

#6
# age = pd.Series(
#     [21,24,19,30]
# )
# print(age)
# print(age.values)
# print(age.index)
#7
# import numpy as np
# np.random.seed(2)
# marks=np.random.randint(35,100,10)
# print(marks)
# marks=pd.Series(marks)
# print(marks)

#8
# import numpy as np
# np.random.seed(2)
# salary=np.random.randint(35000,100000,15)
# print(salary)
# salary=pd.Series(salary)
# print(salary)
# print(salary.mean())
# print(salary.max())
# print(salary.min())

#9
# import numpy as np
# np.random.seed(2)
# sales=np.random.randint(1000,5000,5)
# print(sales)
# print(pd.Series([sales]))
# sales_s=pd.Series(
#     sales,
#     index=["Mon","Tue","Wed","Thu","Fri"]
# )
# print(sales_s["Wed"])

#10
# cities=pd.Series(["Ahmedabad","Surat","Baroda","Jamnagar","Rajkot"])
# print(cities[0])
# print(cities[4])

#Bonus
# import numpy as np
# np.random.seed(42)
# temperatures=np.random.randint(-40,50,10)
# print(temperatures)
# print(temperatures.mean())
# print(temperatures.max())
# print(temperatures[temperatures>temperatures.mean()])

#Bonus
# fruits=pd.Series(
#     [120,40,80,150],
#     index=["Apple","Banana","Orange","Mango"]
# )
# print(fruits)
# print(fruits[fruits>100])
# print(fruits.mean())


# marks = pd.Series([70,80,90])
# print(marks.shape)
# print(marks.size)
# print(marks.dtype)
# print(marks.index)
# print(marks.values)


#1
# student_data={
#     "Name":["Rahul","Manthan","Neha"],
#     "Age":[24,21,26]
# }
# print(pd.DataFrame(student_data))

#2
# student_data={
#     "Name":["Rahul","Manthan","Neha"],
#     "Age":[24,21,26]
# }
# df=pd.DataFrame(student_data)
# print(df)
# print(df.shape)
# print(df.size)
# print(df.columns)
# print(df.index)

#3

# student_data={
#     "Name":["Rahul","Manthan","Neha"],
#     "Age":[24,21,26]
# }
# df=pd.DataFrame(student_data)
# print(df)
# print(df.values)
# print(df.dtypes)

#4

# student_data={
#     "Name":["Rahul","Manthan","Neha"],
#     "Age":[24,21,26]
# }
# df=pd.DataFrame(student_data)
# print(df)
# print(df["Age"])

#5
# student_data={
#     "Name":["Rahul","Manthan","Neha"],
#     "Age":[24,21,26]
# }
# df=pd.DataFrame(student_data)
# print(df["Name"])
# print(df["Age"])

#6

# data_products={
#     "Product":["Apple","Mango","Banana"],
#     "Quantity":[12,8,25],
#     "Price":[15,70,5]
# }
# df=pd.DataFrame(data_products)
# print(df)
# print(df[["Product","Price"]])

#7

# import numpy as np

# np.random.seed(1)
# ages=np.random.randint(18,100,10)
# salarys=np.random.randint(20000,100000,10)

# employee_data={
#     "age":pd.Series(ages),
#     "salary":pd.Series(salarys)
# }
# df=pd.DataFrame(employee_data)
# print(df)

#8
# import numpy as np

# np.random.seed(1)
# ages=np.random.randint(18,100,10)
# salarys=np.random.randint(20000,100000,10)

# employee_data={
#     "age":pd.Series(ages),
#     "salary":pd.Series(salarys)
# }
# df=pd.DataFrame(employee_data)
# print(df)
# print(df.shape)
# print(df.dtypes)

#9

# stduent_data={
#     "Student":["Amit","Rahul","Neha","Manthan"],
#     "Marks":[75,82,91,88]
# }
# df=pd.DataFrame(stduent_data)
# print(df["Marks"])

#10
# employee_data={
#     "Employee":["Rahul","Manthan","Neha"],
#     "Department":["HR","IT","Sales"],
#     "Salary":[45000,52000,61000]
# }

# df=pd.DataFrame(employee_data)
# print(df[["Department","Salary"]])

#Bonus
# import numpy as np

# np.random.seed(41)
# ID_s=np.random.randint(101,120,20)
# salaries=np.random.randint(20000,100000,20)
# ages=np.random.randint(20,60,20)

# employees_data={
#     "ID":pd.Series(ID_s),
#     "Salary":pd.Series(salaries),
#     "Age":pd.Series(ages)
# }
# df=pd.DataFrame(employees_data)
# print(df)
# print(df["Salary"])
# print(df[["Age","Salary"]])
# print(df.shape)
# print(df.dtypes)

#Bonus

# import numpy as np

# np.random.seed(41)
# Quantity=np.random.randint(1,20,5)
# Price=np.random.randint(20000,100000,5)

# product_data={
#     "Product":["Computer","Mobile Phone","AC","Microwave","Refrigerator"],
#     "Quantity":pd.Series(Quantity),
#     "Price":pd.Series(Price),
#     "Total":Quantity*Price
# }
# df=pd.DataFrame(product_data)
# print(df)

# head and tails
# import numpy as np

# np.random.seed(41)
# Quantity=np.random.randint(1,20,5)
# Price=np.random.randint(20000,100000,5)

# product_data={
#     "Product":["Computer","Mobile Phone","AC","Microwave","Refrigerator"],
#     "Quantity":pd.Series(Quantity),
#     "Price":pd.Series(Price),
#     "Total":Quantity*Price
# }
# df=pd.DataFrame(product_data)
# print(df.head(2))
# print(df.tail(3))

#1
# df = pd.DataFrame({
#     "Name":["Rahul","Neha","Manthan"],
#     "Age":[24,26,21]
# })
# print(df.to_csv("students.csv",index=False))

#2
# df=pd.read_csv("students.csv")
# print(df)

#3
# df=pd.read_csv("students.csv")
# print(df.head())
# print(df.head(2))

#4
# df=pd.read_csv("students.csv")
# print(df.tail())
# print(df.tail(1))

#5

# df=pd.read_csv("students.csv")
# print(df.info())
# #6
# print(df.describe())

#7
# product_data={
#     "Product":["Apple","Mango","Banana","Orange"],
#     "Qty":[12,8,25,15],
#     "Price":[15,70,5,20]
# }
# df=pd.DataFrame(product_data)
# print(df)
# try:
#     df.to_csv("sales.csv", index=False)
#     print("done")
# except Exception as e:
#     print(f"error: {e}")

#8

# df=pd.read_csv("sales.csv")
# print(df.head())
# print(df.info())
# print(df.describe())

#9
# import numpy as np

# np.random.seed(42)
# ages=np.random.randint(20,60,20)
# salaries=np.random.randint(20000,100000,20)

# employee_data={
#     "Age":ages,
#     "Salary":salaries
# }

# df=pd.DataFrame(employee_data)
# print(df)

# try:
#     df.to_csv("employees.csv",index=False)
#     print("done")
# except Exception as e:
#     print(e)

#10
# df=pd.read_csv("employees.csv")
# print(df.shape)
# print(df.info())
# print(df.describe())

#Bonus

# import numpy as np

# np.random.seed(1)
# marks=np.random.randint(35,100,100)
# print(marks)

# marks_data={
#     "Mark":marks
# }
# df=pd.DataFrame(marks_data)
# try:
#     df.to_csv("marks.csv",index=False)
#     print("done")
# except Exception as e:
#     print(e)

# df=pd.read_csv("marks.csv")
# print(df.head())
# print(df.tail())
# print(df.describe())

#Bonus
# import numpy as np

# np.random.seed(4)
# Quantity=np.random.randint(1,20,5)
# Price=np.random.randint(20000,100000,5)

# product_data={
#     "Product":["Computer","Mobile Phone","AC","Microwave","Refrigerator"],
#     "Quantity":pd.Series(Quantity),
#     "Price":pd.Series(Price),
#     "Total":Quantity*Price
# }

# df=pd.DataFrame(product_data)
# print(df)
# try:
#     df.to_csv("products_data.csv",index=False)
#     print("done")
# except Exception as e:
#     print(e)

# df=pd.read_csv("products_data.csv")
# print(df.info())
# print(df.describe())
# print(df.head(2))
# print(df.tail(2))
# print(df.columns)


# import pandas as pd

# df = pd.DataFrame({
#     "Name":["A","B","C","D","E"],
#     "Marks":[60,75,90,55,80]
# })

# print(df.shape)

# print(df.size)

# print(df.columns)

# print(df.head(3))

# print(df.tail(2))

# print(pd.__version__)

#1
# import pandas as pd

# df = pd.DataFrame({
#     "Name":["Rahul","Manthan","Neha","Amit"],
#     "Age":[24,21,26,22],
#     "Salary":[45000,52000,61000,48000]
# })
# print(df)
# print(df.iloc[0])
#2
# print(df.iloc[2])
#3
# print(df.iloc[0:2])
#4
# print(df.iloc[:,[0,2]])
#5
# print(df.iloc[2,2])
#6
# df.index = ["E101", "E102", "E103", "E104"]
# print(df.loc["E102"])
#7
# print(df.loc["E101":"E103"])
#8
# print(df.loc[:,["Name","Salary"]])
#9
# print(df.loc["E103","Salary"])
#10
# import numpy as np
# import names

# # First, install the library in your terminal or command prompt:
# # pip install names

# names_list = []

# # Generate 10 random names and append to list
# for _ in range(10):
#     full_name = f"{names.get_first_name()} {names.get_last_name()}"
#     names_list.append(full_name)

# # Print the list of names
# # print(names_list)

# np.random.seed(42)
# ages=np.random.randint(20,60,10)
# salaries=np.random.randint(20000,100000,10)

# employee_data={
#     "Name":names_list,
#     "Age":ages,
#     "Salary":salaries
# }
# df=pd.DataFrame(employee_data)
# print(df)
# print(df.iloc[0]) #first row
# print(df.iloc[3:6]) #third, fourth,fifth row
# df.index=["E101","E102","E103","E104","E105","E106","E107","E108","E109","E110"]
# print(df)


#bonus

# import numpy as np
# import names

# name_lists=[]
# names.random.seed(1)
# np.random.seed(1)
# for _ in range(20):
    
#     full_name = names.get_full_name()
#     name_lists.append(full_name)



# marks=np.random.randint(36,100,20)

# student_data={
#     "Name":name_lists,
#     "Marks":marks
# }
# df=pd.DataFrame(student_data)
# # print(df)
# df.index = [f"S{i}" for i in range(101, 121)]
# print(df)
# print(df.loc["S110"])
# print(df.loc["S105":"S115"])
# print(df.loc[:,["Name","Marks"]])

#Bonus

# product_data={
#     "Product_name":["AC","LAPTOP","MOBILEPHONE"],
#     "PRICE":[37000,48000,14000],
#     "QUN":[10,5,12]
# }
# df=pd.DataFrame(product_data)
# print(df)

# df.index=["P101","P102","P103"]
# print(df)
# print(df.loc["P102","Product_name"])
# print(df.loc["P103","PRICE"])
# print(df.loc[:,["Product_name","PRICE"]])

# import pandas as pd

# df = pd.DataFrame({
#     "Name":["Rahul","Neha","Amit"],
#     "Marks":[80,90,75]
# })

# df.index=["S101","S102","S103"]

# print(df.loc["S102"])

# print(df.iloc[2])

# print(df.at["S103","Marks"])

# print(df.iat[0,1])


# import pandas as pd

# df = pd.DataFrame({
#     "Name":["Rahul","Manthan","Neha","Amit","Priya"],
#     "Age":[24,21,26,22,25],
#     "Salary":[45000,52000,61000,48000,55000]
# })

# #1
# print(df[df["Salary"]>50000])

# #2
# print(df[df["Age"]<24])

# #3
# print(df[df["Name"]=="Rahul"])

# #4
# print(df[df["Name"]!="Rahul"])

# #5
# print(
#     df[
#     (df["Salary"]>45000)
#     &
#     (df["Age"]<25)
# ])

# #6
# print(
#     df[
#     (df["Age"]<22)
#     |
#     (df["Salary"]<55000)
# ])

# #7
# print(
#     df[
#         df["Name"].isin(
#             ["Rahul","Priya"]
#         )
#     ]
# )

# #8
# print(
#     df[
#         df["Salary"].between(
#             45000 ,
#             55000
#         )
#     ]
# )

# #9
# print(
#     df.loc[
#       df["Salary"]>50000,
#       ["Name","Salary"]
#      ] )

#10
# import numpy as np
# import names 

# np.random.seed(42)
# name_lists=[]
# for _ in range(20):
#         name_lists.append(names.get_full_name())

# salaries=np.random.randint(20000,100000,20)
# ages=np.random.randint(20,60,20)

# employee_data={
#         "Name":name_lists,
#         "Salary":salaries,
#         "Age":ages
# }
# df=pd.DataFrame(employee_data)

# print(df)
# print(df[df["Salary"]>50000])
# print(df[df["Age"]<24])
# print(
#         df[
#             (df["Salary"]>45000)
#             &
#             (df["Age"]<25)
#         ]
# )
# print(
#         df[
#                 (df["Age"]>22)
#                 |
#                 (df["Salary"]<55000)
#         ]
# )
# print(
#         df[
#                 (df["Salary"].between(
#                         45000,50000
#                 ))
#         ]
#       )

# print(
#         df.loc[
#         df["Salary"]>50000,
#         ["Name","Salary"]
# ])
#notice: i does not done with name realted == and != question because of my names are not seed 

#bonus
# student_data={
#     "Name":["Manthan","Khushbu","Neha","Aastha","Rahul"],
#     "Marks":[55,87,67,82,45]
# }
# df=pd.DataFrame(student_data)
# print(df[df["Marks"]>80])
# print(
#     df[
#         (df["Marks"].between(
#         60,90))
#     ]
# )

#bonus

# super_market={
#     "Product_name":["Tea","Salt","Jegrry","WashingPowder","PowerSell"],
#     "Price":[230,10,1500,350,150],
#     "Qty":[2,1,12,3,10]
# }
# df=pd.DataFrame(super_market)
# print(df[df["Price"]>1000])
# print(df[df["Qty"]<5])
# print(
#     df[
#         (df["Product_name"].isin(
#             ["WashingPowder","Tea"]
#         ))
#     ]
# )

# import pandas as pd

# df = pd.DataFrame({
#     "Name":["Rahul","Manthan","Neha","Amit","Priya"],
#     "Age":[24,21,26,22,25],
#     "Salary":[45000,52000,61000,48000,55000]
# })

#1
# print(df.sort_values("Salary"))
# #2
# print(df.sort_values("Salary",ascending=False))
# #3
# print(df.sort_values("Name"))
# #4
# print(df.sort_values("Age"))
# print(df.sort_values("Age",ascending=False))
# #5
# sorted_df=df.sort_values("Salary")
# print(sorted_df)
# sorted_dfd=df.sort_values("Salary",ascending=False)
# print(sorted_dfd)
#6
# df.index=["E105","E101","E104","E103","E102"]
# print(df.sort_index())
# #7

# print(df.sort_index(ascending=False))

#8
# department_data={
#     "Department":["IT","HR","IT","HR"],
#     "Salary":[45000,52000,61000,48000]
# }
# df=pd.DataFrame(department_data)
# print(df.sort_values(
#     ["Department","Salary"]
# ))
# print(df.sort_values(
#     ["Department","Salary"]
# ,ascending=False))

#9
# import numpy as np
# import names 

# np.random.seed(2)

# fullname_list=[]
# for _ in range(20):
#     fullname_list.append(names.get_full_name())

# salaries=np.random.randint(20000,100000,20)
# ages=np.random.randint(20,60,20)

# employee_data={
#     "Name":fullname_list,
#     "Salary":salaries,
#     "Age":ages
# }
# df=pd.DataFrame(employee_data)
# print(df)
# print(df.sort_values("Salary",ascending=False))
# print(df.sort_values("Age"))

#10

# df_boolen_salary=df["Salary"]>50000
# print(df[df_boolen_salary])
# print(df[df_boolen_salary].sort_values("Salary",ascending=False))

#bonus

# import numpy as np
# import names 

# np.random.seed(2)

# fullname_list=[]
# for _ in range(15):
#     fullname_list.append(names.get_full_name())


# marks=np.random.randint(35,100,15)

# stduent_data={
#     "Name":fullname_list,
#     "Mark":marks
# }
# df=pd.DataFrame(stduent_data)
# print(df)
# print(df.sort_values("Mark",ascending=False))
# print(df.sort_values("Name"))

#bonus
# super_market={
#     "Product_name":["Tea","Salt","Jegrry","WashingPowder","PowerSell"],
#     "Price":[230,10,1500,350,150],
#     "Qty":[2,1,12,3,10]
# }
# df=pd.DataFrame(super_market)
# print(df)
# print(df.sort_values("Price",ascending=False))
# print(df.sort_values("Qty"))

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Age":[24,np.nan,29,31,np.nan],
#     "Salary":[45000,52000,np.nan,61000,55000],
#     "City":["Ahmedabad","Surat",np.nan,"Rajkot","Ahmedabad"]
# })
#1
# print(df)
# #2
# print(df.isna())
# #3
# print(df.isna().sum())
# #4
# print(df.notna())
# print(df[df["Age"].notna()])

#5
# print(df.fillna(0))

#6
# df["Age"]=df["Age"].fillna(df["Age"].mean())
# print(df)

#7
# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)

#8
# print(df.dropna())

#9
# print(df.dropna(axis=1))

#10
# import pandas as pd
# import numpy as np
# import names
# from faker import Faker

# fake = Faker("en_IN")

# np.random.seed(42)

# employees_name = []
# city_list = []

# for _ in range(20):
#     employees_name.append(names.get_full_name())
#     city_list.append(fake.city())

# ages = np.random.randint(20, 60, 20).astype(float)
# salaries = np.random.randint(20000, 100000, 20).astype(float)

# # Introduce missing values
# ages[[2, 7, 15]] = np.nan
# salaries[[4, 10, 18]] = np.nan
# city_list[5] = np.nan
# city_list[12] = np.nan

# employees_data = {
#     "Name": employees_name,
#     "Age": ages,
#     "City": city_list,
#     "Salary": salaries
# }

# df = pd.DataFrame(employees_data)

# print(df)


# print(df.isna().sum())

# df["Age"]=df["Age"].fillna(df["Age"].mean())
# print(df)

# print(df["Salary"].dropna())

# df_sort_salary=df["Salary"].sort_values(ascending=False)
# print(df_sort_salary)


#bonus
# import numpy as np
# student_data={
#     "Name":["Manthan Patel","Khushubu Shah","Aastha Patel","Tirth Dabhi","Shukan Soni"],
#     "Marks":[38,93,72,np.nan,np.nan],
#     "Attendance":[np.nan,90,88,67,np.nan]
# }    
# df=pd.DataFrame(student_data)
# # print(df)

# print(df.isna().sum())
# df["Marks"]=df["Marks"].fillna(df["Marks"].mean())

# df["Attendance"]=df["Attendance"].fillna(df["Attendance"].median())
# print(df)

# print(
#     df[
#         df["Marks"]>70
#     ]
# )

# print(df["Marks"].sort_values(ascending=False))

#bonus
# import numpy as np
# super_market={
#     "Product_name":["Tea","Salt","Jegrry","WashingPowder","PowerSell"],
#     "Price":[230,np.nan,1500,350,np.nan],
#     "Qty":[2,1,12,np.nan,10]
# }
# df=pd.DataFrame(super_market)
# # print(df)


# df["Qty"] = df["Qty"].fillna(0)

# print(df)

# df["Price"]=df["Price"].fillna(df["Price"].median())

# print(df)

# print(df["Price"].sort_values(ascending=False))

# Mixed 1

# import numpy as np

# df = pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Age":[24,np.nan,29,31,np.nan],
#     "Salary":[45000,52000,44000,61000,55000]
# })

# df["Age"]=df["Age"].fillna(df["Age"].mean())
# print(df)

# print(
#     df[
#         (df["Salary"]>50000)
#     ]
# )

# print(df["Salary"].sort_values(ascending=False))

# print(df.loc[:,["Name","Salary"]])

# Mixed 2
# try:
#     files=pd.read_csv("students_scores.csv")

# except Exception as e:
#     print(e)

# print(files.info())
# print(files.isna().sum())

# files["Math"]=files["Math"].fillna(files["Math"].mean())
# # print(files)

# files["Science"]=files["Science"].fillna(files["Science"].mean())
# # print(files)


# files["English"]=files["English"].fillna(files["English"].mean())
# # print(files)


# files["Attendance"]=files["Attendance"].fillna(files["Attendance"].median())
# print(files)

# print(
#     files[
#         (files["Math"]>85)
#             &
#         (files["Attendance"]>90)
#     ]
# )

# print(
#     files[
#         files["Science"].between(
#             65,90
#         )
#     ]
# )

# print(files["Attendance"].sort_values().nsmallest(5))

# Mixed 3

# import numpy as np
# import pandas as pd


# np.random.seed(42)

# names = [
#     "Liam",
#     "Noah",
#     "Oliver",
#     "Elijah",
#     "William",
#     "James",
#     "Benjamin",
#     "Lucas",
# ]
# marks = np.random.randint(55, 100, size=len(names)).astype(float)


# df = pd.DataFrame({"Name": names, "Marks": marks})


# df.at[2, "Marks"] = np.nan
# df.at[5, "Marks"] = np.nan

# print(df)
# print(df.isna().sum())
# df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
# print(df)
# print(df[df["Marks"]>=80])

# print(df["Name"].sort_values(ascending=False))
# print(df["Marks"].sort_values().nlargest(3))


#new metor 
# import pandas as pd
# import numpy as np

# data = {
#     "EmployeeID": [101,102,103,104,105,106,107,108,109,110,
#                    111,112,113,114,115,116,117,118,119,120,
#                    121,122,123,124,125,126,127,128,129,130],

#     "Name": ["Aarav","Diya","Vivaan","Anaya","Aditya","Kiara","Ishaan","Meera","Kabir","Sara",
#              "Rohan","Priya","Arjun","Sneha","Yash","Neha","Dev","Riya","Kunal","Aisha",
#              "Rahul","Pooja","Manav","Nisha","Aryan","Tanvi","Harsh","Simran","Nitin","Kriti"],

#     "Age": [25,30,np.nan,28,35,26,31,np.nan,29,40,
#             27,33,24,36,np.nan,32,38,29,41,26,
#             34,30,27,np.nan,39,28,31,37,25,29],

#     "Salary": [50000,62000,58000,70000,np.nan,45000,67000,52000,61000,75000,
#                49000,np.nan,56000,68000,72000,54000,80000,59000,63000,47000,
#                66000,51000,73000,np.nan,64000,55000,69000,76000,53000,60000],

#     "City": ["Mumbai","Delhi","Pune","Chennai","Bengaluru","Hyderabad","Ahmedabad",None,"Jaipur","Lucknow",
#              "Mumbai","Delhi","Pune","Chennai","Bengaluru","Hyderabad","Ahmedabad","Surat","Jaipur","Lucknow",
#              "Mumbai","Delhi","Pune","Chennai","Bengaluru",None,"Ahmedabad","Surat","Jaipur","Lucknow"]
# }

# df = pd.DataFrame(data)

# print(df)

# # max_missing=df.isna().sum()
# # print(max_missing.max())

# # df["Age"]=df["Age"].fillna(df["Age"].mean())
# # print(df)

# # df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# # print(df)

# # df["City"]=df["City"].fillna("Unknown")
# # print(df)

# # print(df[df["Salary"]>60000])
# # print(df["Salary"].sort_values(ascending=False))


# import pandas as pd

# df = pd.DataFrame({
#     "Name":["Rahul","Neha","Rahul","Amit","Neha","Priya"],
#     "Age":[24,26,24,28,26,30],
#     "Salary":[45000,52000,45000,61000,52000,70000]
# })

# #1

# print(df)

# #2
# # print(df.duplicated())

# # #3
# # print(df.duplicated().sum())

# # #4
# # print(df[df.duplicated()])

# # #5
# # print(df.drop_duplicates())

# #6
# print(df.drop_duplicates(keep="last"))

# #7
# print(df.drop_duplicates(keep=False))

# #8
# print(df[df.duplicated(subset="Name")])

# #9
# print(df.drop_duplicates(subset="Name"))

#10
# try:
#     df=pd.read_csv("employees_data.csv")
#     print(df)
# except Exception as e:
#     print("ERROR:",e)

# print(df.duplicated("Name").sum())
# print(df.duplicated("Email").sum())

# print(df.drop_duplicates("Email"))

# print(df["Salary"].sort_values(ascending=False)) #Sort Salary descending.
# print(df.sort_values("Salary",ascending=False))  #sort by salary descending whole table 

# print(df.sort_values("Salary",ascending=False).head(5)) #sort by salary descending whole table 5 top
# print(df["Salary"].sort_values(ascending=False).nlargest(5)) #Sort Salary descending. 5 top 

#bonus

# df_manual = {
#     "StudentID": ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20"],
#     "Name": ["Liam Carter", "Olivia Olivia", "Noah Brooks", "Emma Watson", "Oliver Bennett", "Ava Adams", "Elijah Gray", "Charlotte Rice", "James Smith", "Benjamin Foster", "Liam Carter", "Mia Long", "Lucas Ward", "Amelia Cruz", "Henry Mason", "Emma Watson", "Alexander Boyd", "Harper Vance", "Jack Reynolds", "Evelyn Porter"],
#     "Subject": ["Maths", "Science", "History", "Maths", "Science", "History", "Maths", "Science", "History", "Maths", "Science", "History", "Maths", "Science", "History", "Science", "Maths", "Science", "History", "Maths"],
#     "Marks": [88, 92, 79, 95, 84, 91, 73, 89, 65, 98, 85, 77, 93, 81, 70, 96, 62, 87, 74, 90]
# }

# df=pd.DataFrame(df_manual)
# print(df)

# print(df.duplicated("Name").sum())

# print(df.drop_duplicates("Name"))

# sort_m=df.sort_values("Marks",ascending=False)
# print(sort_m)

# print(sort_m.head(3))

#bonus

# supermarket_df = {
#     "ProductID": ["P01", "P02", "P03", "P04", "P01", "P06", "P07", "P08", "P02", "P10", "P11", "P04", "P13", "P14", "P15"],
#     "Product": ["Wireless Mouse", "LED Monitor", "Mechanical Keyboard", "USB-C Cable", "Wireless Mouse", "Gaming Headset", "HDMI Cable", "External SSD", "LED Monitor", "Bluetooth Speaker", "Desk Mat", "USB-C Cable", "Webcam", "Office Chair", "Power Bank"],
#     "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics", "Audio", "Accessories", "Storage", "Electronics", "Audio", "Furniture", "Accessories", "Electronics", "Furniture", "Accessories"],
#     "Price": [250, 1200, 850, 150, 250, 650, 120, 1100, 1200, 450, 180, 150, 550, 2400, 350]
# }

# df=pd.DataFrame(supermarket_df)
# # print(df.duplicated())
# # print(df[df.duplicated()])
# # print(df.drop_duplicates())

# print(df[df["Price"]>500])
# print(df["Price"].sort_values(ascending=False)) #Sort Price descending.

#mixed 1

# employee_df = {
#     "EmployeeID": ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15"],
#     "Name": ["Alice Smith", "Bob Jones", "Charlie Brown", "Alice Smith", "David Miller", "Eva Green", "Bob Jones", "Frank Wilson", "Grace Davis", "Henry Clark", "James Taylor", "Linda White", "Henry Clark", "Nancy Adams", "Oscar Ward"],
#     "Age": [28, None, 42, 28, 35, None, 31, 50, 24, 38, None, 45, 38, 29, 52],
#     "Salary": [55000, 62000, 75000, 55000, 48000, 67000, 62000, 89000, 43000, 58000, 71000, 82000, 58000, 51000, 95000]
# }

# df=pd.DataFrame(employee_df)
# print(df.isna().sum())
# df["Age"]=df["Age"].fillna(df["Age"].mean())
# print(df)
# print(df.duplicated("Name").sum())
# print(df.drop_duplicates("Name"))
# print(df[df["Salary"]>60000])
# print(df["Salary"].sort_values(ascending=False)) #Sort Salary descending.
# print(df.sort_values("Salary",ascending=False)) #whole table sort by salary descending

#mixed2

# student_df = {
#     "StudentID": ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13", "S14", "S15"],
#     "Name": ["John Doe", "Jane Smith", "Sam Wilson", "John Doe", "Emily Davis", "Michael Brown", "Jane Smith", "Sarah Miller", "James Bond", "David Clark", "Emily Davis", "Jessica Taylor", "Kevin Spacey", "Brian Tracy", "Oliver Twist"],
#     "Subject": ["Maths", "Science", "History", "Maths", "Science", "History", "Science", "Maths", "Science", "History", "Science", "Maths", "History", "Science", "Maths"],
#     "Marks": [85, None, 72, 85, 95, 64, None, 88, 45, 91, 95, 78, 83, None, 92]
# }

# df=pd.DataFrame(student_df)
# print(df.info())
# print(df.describe())
# print(df.isna().sum())
# df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
# print(df)
# print(df.duplicated("Name"))
# print(df.drop_duplicates("Name"))
# print(df[df["Marks"]>80])
# print(df["Marks"].sort_values(ascending=False))
# sort_m=df.sort_values("Marks",ascending=False)
# print(sort_m.head(5))
# print(df.head(5))


#mixed 3
# import numpy as np
# import pandas as pd

# np.random.seed(42)


# num_records = 15
# emp_ids = np.arange(101, 101 + num_records)

# salaries = np.random.randint(45000, 120001, size=num_records).astype(float)

# emp_ids[3] = 101
# emp_ids[8] = 105

# salaries[2] = np.nan
# salaries[7] = np.nan
# salaries[12] = np.nan

# employee_df = {
#     "EmployeeID": emp_ids.tolist(),
#     "Salary": salaries.tolist()
# }

# df=pd.DataFrame(employee_df)
# print(df.isna().sum())
# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)
# print(df.drop_duplicates("EmployeeID"))
# print(
#     df[
#         df["Salary"]>df["Salary"].mean()
#     ]
# )
# print(df.sort_values("Salary",ascending=False))
# print(df.sort_values("EmployeeID",ascending=False))

# import pandas as pd

# df = pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Marks":[38,82,67,91,75],
#     "Salary":[45000,52000,61000,55000,48000],
#     "Gender":["M","F","M","F","M"]
# })

# #1
# print(df["Name"].apply(str.upper))

# #2
# df["Bonus"]=df["Salary"].apply(lambda x:x+5000)
# print(df)

# #3
# df["Result"]=df["Marks"].apply(lambda x: "Pass" if x>=40 else "Fail")
# print(df)

# #4
# df["Grade"]=df["Marks"].apply(lambda x:"A" if x>=90 else ("B" if x>=75 and x<=89 else "C"))
# print(df)

# #5
# gender = {
#     "M":"Male",
#     "F":"Female"
# }

# df["Gender"] = df["Gender"].map(gender)
# print(df)

# #6
# df["Tax"]=df["Salary"].apply(lambda x:x*5/100)
# print(df)

# #7
# df["Net Amount"]=df.apply(lambda row:row["Salary"]-row["Tax"],axis=1)
# print(df)

# #8
# df["Full Status"]=df.apply(lambda row:row["Name"]+"-"+row["Result"],axis=1)
# print(df)

# #9
# df["Status"]=df["Marks"].apply(lambda x:"Excellent" if x>=85 else "Average")
# print(df)

#10
# import numpy as np

# np.random.seed(42)

# ages=np.random.randint(20,60,20)
# salaries=np.random.randint(10000,100000,20)

# df=pd.DataFrame({
#     "Age":ages,
#     "Salary":salaries,
#     "Gender":["M","F","F","F","M","F","M","M","M","F","M","F","F","M","F","M","M","F","M","F"]
# })

# df["Bonus"]=df["Salary"].apply(lambda x:"12%" if x>50000  else "10%")
# print(df)


# df["Tax"]=df["Salary"].apply(lambda x:x*5/100)
# print(df)

# df["Net Amount"]=df.apply(lambda row:row["Salary"]-row["Tax"],axis=1)
# print(df)

# gender_data={
#     "M":"Male",
#     "F":"Female"
# }
# df["Gender"]=df["Gender"].map(gender_data)

# print(df)

# df["Status"]=df["Salary"].apply(lambda x:"High Salary" if x>60000 else "Good")
# print(df)


#bonus

# import pandas as pd


# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#     "Marks": [92, 78, 55, 88,34, 95]
# }


# df = pd.DataFrame(data)

# df["Grade"]=df["Marks"].apply(lambda x: "A" if x>90 else ("B" if x>=75 and x<=90 else "C"))
# print(df)

# df["Status"]=df["Marks"].apply(lambda x: "Pass" if x>=35 else "Fail")
# print(df)

# df["Scholarship Eligible"]=df["Marks"].apply(lambda x: "Eligible" if x>=92 else "Not Eligible")
# print(df)

#bonus
# import pandas as pd

# data = {
#     "Product": ["Laptop", "Milk", "Shirt", "Bread", "Headphones"],
#     "Quantity":[4,20,12,15,7],
#     "Price_Per_Unit": [45000, 60, 1200, 45, 2500]
# }

# category_map = {
#     "Laptop": "Electronics",
#     "Headphones": "Electronics",
#     "Milk": "Groceries",
#     "Bread": "Groceries",
#     "Shirt": "Clothing"
# }

# df = pd.DataFrame(data)

# df["Total"]=df.apply(lambda row:row["Quantity"]*row["Price_Per_Unit"],axis=1)
# print(df)

# df["GST"]=df["Total"].apply(lambda x:x*18/100)
# print(df)

# df["Final Price"]=df.apply(lambda row:row["Total"]+row["GST"],axis=1)
# print(df)

# df["Category"] = df["Product"].map(category_map)
# print(df)

#mixed=1
# import numpy as np
# import pandas as pd

# data = {
#     "Emp_ID":["E101","E102","E103","E104","E105","E106","E107"],
#     "Name": ["John", "Sarah", "Mike", "Sarah", "Emma", "David", "John"],
#     "Gender_Code": ["M", "F", "M", "F", "F", "M", "M"],
#     "Salary": [75000, 52000, np.nan, 52000, 68000, np.nan, 45000],
# }

# gender_map = {"M": "Male", "F": "Female"}

# df = pd.DataFrame(data)

# print(df.isna().sum())

# df["Salary"]=df["Salary"].fillna(df["Salary"].median())

# print(df)

# print(df.drop_duplicates("Name"))

# df["Bonus"]=df["Salary"].apply(lambda x:x*5/100)
# print(df)

# df["Gender"]=df["Gender_Code"].map(gender_map)
# print(df)

# print(df[df["Salary"]>60000])

# print(df.sort_index(ascending=False))

#mixed 2

# import numpy as np
# import pandas as pd

# try:
#     df = pd.read_csv("data.csv")
    
# except Exception as e:
#     print(e)

# print(df.info())

# print(df.describe())

# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)

# df=df.drop_duplicates()
# print(df)

# df["Bonus"]=df["Salary"].apply(lambda x:x*7/100)
# print(df)

# df["Tax"]=df["Salary"].apply(lambda x:x*5/100)
# print(df)

# print(df.head(5))

#mixed 3

# import numpy as np
# import pandas as pd

# np.random.seed(42)

# data = {
   
#     "Name": ["Alex", "Blake", "Charlie", "Dana", "Eli", "Blake", "Fox", "Glen", "Dana", "Hunter"],
    
#     "Base_Salary": np.random.randint(40000, 100000, size=10),

#     "Perf_Score": np.random.randint(1, 6, size=10)
# }

# df = pd.DataFrame(data)

# df["Grade"]=df["Perf_Score"].apply(lambda x:"A" if x>=5 else("B" if x<5 and x>=3 else "C"))
# print(df)

# df["Bonus"]=df["Base_Salary"].apply(lambda x:x*5/100)
# print(df)

# df["Category"]=df["Base_Salary"].apply(lambda x:"High Salary" if x>80000 else "Good")
# print(df)

# print(df["Name"].drop_duplicates())

# print(df.sort_values("Name"))

# import pandas as pd

# df = pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya","Manthan","Karan"],
#     "Department":["IT","HR","IT","HR","IT","Sales"],
#     "Salary":[50000,60000,45000,70000,55000,65000],
#     "Age":[24,26,28,30,23,29],
#     "City":["Ahmedabad","Rajkot","Surat","Ahmedabad","Surat","Baroda"]
# })

# #1
# print(df)

#2
# total_salary_dwise=df.groupby("Department")["Salary"].sum()
# print(total_salary_dwise)
# print(df.groupby("Department").sum())

#3

# av_salary=df.groupby("Department")["Salary"].mean()
# print(av_salary)

#4
# max_S=df.groupby("Department")["Salary"].max()
# print(max_S)

# #5
# min_S=df.groupby("Department")["Salary"].min()
# print(min_S)

# #6
# count_E=df.groupby("Department")["Name"].count()
# print(count_E)

# #7
# aggfunction=df.groupby("Department")["Salary"].agg(["sum","mean","min","max","count"])
# print(aggfunction)

# #8
# find_a_city_d=df.groupby(["City","Department"])["Salary"].mean()
# print(find_a_city_d)

#9
# print(df.groupby("Department")["Salary"].mean().reset_index())

#10
# import numpy as np
# import names

# np.random.seed(4)


# # import pandas as pd
# # import numpy as np
# # from faker import Faker

# # fake = Faker()
# # np.random.seed(42)

# # departments = ["HR", "IT", "Finance", "Marketing", "Sales"]
# # cities = ["Ahmedabad", "Mumbai", "Delhi", "Bengaluru", "Pune"]

# # df = pd.DataFrame({
# #     "Name": [fake.name() for _ in range(30)],
# #     "Department": np.random.choice(departments, 30),
# #     "City": np.random.choice(cities, 30),
# #     "Salary": np.random.randint(30000, 120001, 30),
# #     "Age": np.random.randint(21, 61, 30)
# # })

# # print(df)
# # high_salary_a=df.groupby("Department")["Salary"].mean()
# # print(high_salary_a)
# # print(df.groupby("City")["Salary"].max())
# # print(df.groupby("City")["Name"].count())

# # function_agge=df.groupby("Department")["Salary"].agg(["sum","mean","min","max","median","std"])
# # print(function_agge)

# # print(high_salary_a.sort_values(ascending=False))

# #bonus

# try:
#     df=pd.read_csv("student_marks.csv")
#     print(df)
# except Exception as e:
#     print(e)

# av_marks_class=df.groupby("Class")["Marks"].mean()
# print(av_marks_class)

# hi_marks_subject=df.groupby("Subject")["Marks"].max()
# print(hi_marks_subject)

# student_count_class=df.groupby("Class")["Student"].count()
# print(student_count_class)

#bonus

# try:
#     df=pd.read_csv("super_market.csv")
#     print(df)
# except Exception as e:
#     print(e)


# toatl_sale_c=df.groupby("Category")["Sales"].sum()
# print(toatl_sale_c)

# av_quty=df.groupby("Category")["Quantity"].mean()
# print(av_quty)

# high_sale_c=df.groupby("Category")["Sales"].max()
# print(high_sale_c)

# lowest_sale_c=df.groupby("Category")["Sales"].min()
# print(lowest_sale_c)

#mixed 1

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108, 105, 109],
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Eva", "Irene"],
#     "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR", "HR", "Finance"],
#     "Salary": [50000, 70000, np.nan, 80000, 55000, 65000, np.nan, 52000, 55000, 72000],
#     "Experience": [5, 8, 4, 10, 6, 7, 3, 5, 6, 9]
# })

# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)

# df=df.drop_duplicates()
# print(df)

# df["Bonus"]=df["Salary"].apply(lambda x:x*10/100)
# print(df)

# group_department=df.groupby("Department")
# print(group_department.count())

# av_salary_d=df.groupby("Department")["Salary"].mean()
# print(av_salary_d)

# sort_salaryby=df.sort_values("Salary",ascending=False)
# print(sort_salaryby)

# #mixed 2

# try:
#     df=pd.read_csv("Mixed_2.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# print(df.describe())

# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# # print(df)

# df["Experience"]=df["Experience"].fillna(df["Experience"].mean())
# print(df)

# group_by_name_d=df.groupby("Department")["Name"]
# print(group_by_name_d.count())

# aggfunction=df.groupby("Department")["Salary"].agg(["sum","max","min","std","mean","median"])
# print(aggfunction)

# print(df.sort_values("Salary",ascending=False).head(5))
# print(df["Salary"].nlargest(5))

#mixed3
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee_ID": [101, 102, 103, 104, 105, 103, 106, 107, 108, 109, 110, 102],
#     "Name": [
#         "Alice", "Bob", "Charlie", "David", "Eva", "Charlie",
#         "Frank", "Grace", "Henry", "Ivy", "Jack", "Bob"
#     ],
#     "Department": [
#         "HR", "IT", "Finance", "HR", "IT", "Finance",
#         "HR", "Marketing", "IT", "Finance", "Marketing", "IT"
#     ],
#     "Salary": [
#         50000, 60000, np.nan, 55000, 70000, np.nan,
#         52000, 48000, 65000, 72000, np.nan, 60000
#     ]
# })

# # print(df)

# print(df.duplicated().sum())

# print(df["Salary"].isna().sum())

# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)

# df=df.drop_duplicates()
# print(df)

# g_d_n=df.groupby("Department")["Name"].sum()
# print(g_d_n)

# print(df.groupby("Department")["Salary"].mean())

# print(df.groupby("Department")["Salary"].max())

# print(df.groupby("Department")["Name"].count())

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Department":["IT","IT","HR","Sales","HR","Sales"],
#     "Salary":[50000,np.nan,60000,45000,70000,55000]
# })

# print(df.groupby("Department")["Salary"].count())

# print(df.groupby("Department").size())

# print(df.groupby("Department")["Salary"].mean())

# print(
#     df.groupby("Department")["Salary"].agg(
#         ["sum","max","min","count"]
#     )
# )


# import pandas as pd
# import numpy as np
# employees = pd.DataFrame({
#     "EmployeeID":[101,102,103,104],
#     "Name":["Rahul","Neha","Amit","Priya"],
#     "Department":["IT","HR","Sales","Finance"]
# })

# salary = pd.DataFrame({
#     "EmployeeID":[101,102,103,104],
#     "Salary":[50000,60000,45000,70000]
# })



# #1
# print(employees)
# print(salary)

#2
# df=pd.merge(employees,salary,on="EmployeeID")
# print(df)

#3
# salary = pd.DataFrame({
#     "EmployeeID":[101,102,103,105],
#     "Salary":[50000,60000,45000,np.nan]
# })
# print(pd.merge(employees,salary,on="EmployeeID",how="inner"))

#4
# print(pd.merge(employees,salary,on="EmployeeID",how="left"))

#5

# print(pd.merge(employees,salary,on="EmployeeID",how="right"))

#6
# print(pd.merge(employees,salary,on="EmployeeID",how="outer"))

#7
# salary_1 = pd.DataFrame({
#     "EmpID":[101,102,103,104],
#     "Salary":[50000,60000,45000,78000],
    
# })
# pd.merge(
#     employees,
#     salary_1,
#     left_on="EmployeeID",
#     right_on="EmpID"
# )

#8

# employees = pd.DataFrame({
#     "EmployeeID": [1, 2, 3, 4],
#     "Name": ["Alice", "Bob", "Charlie", "David"],
#     "Department": ["HR", "IT", "Finance", "Marketing"]
# })

# salary = pd.DataFrame({
#     "EmployeeID": [1, 2, 3, 4],
#     "Salary": [50000, 60000, 55000, 65000]
# })

# city = pd.DataFrame({
#     "EmployeeID": [1, 2, 3, 4],
#     "City": ["New York", "Chicago", "Boston", "Seattle"]
# })

# df=pd.merge(employees,salary,how="inner")
# print(df)

# df_1=pd.merge(df,city,how="inner")
# print(df_1)

#9
# df_1=df_1.sort_values("Salary")
# print(df_1)

#10
# import numpy as np

# employees_id=[]
# for i in range(30):
#         employee_id="E"+str(i)
#         employees_id.append(employee_id)

# emp_id=pd.DataFrame({
#         "EmpID":employees_id
# })       

# salary=pd.DataFrame({
#         "Salary":np.random.randint(20000,100000,30)
# })

# city=pd.DataFrame({
        
#             "City": ["Mumbai","Delhi","Pune","Chennai","Bengaluru","Hyderabad","Ahmedabad","Mumbai","Jaipur","Lucknow",
#                 "Mumbai","Delhi","Pune","Chennai","Bengaluru","Hyderabad","Ahmedabad","Surat","Jaipur","Lucknow",
#                 "Mumbai","Delhi","Pune","Chennai","Bengaluru","Shrinagar","Ahmedabad","Surat","Jaipur","Lucknow"]
# })


# df = pd.merge(emp_id, salary, left_index=True, right_index=True)
# print(df)

# df_1=pd.merge(df, city, left_index=True, right_index=True)
# print(df_1)

#bonus

# import pandas as pd
# import numpy as np


# student_ids = [f"S{i}" for i in range(1, 31)]

# students_df = pd.DataFrame({
#     "StudentID": student_ids,
#     "Name": ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Krishna", "Ishaan", "Shaurya",
#              "Diya", "Ananya", "Aadhya", "Peehu", "Kavya", "Prisha", "Riya", "Aanya", "Ira", "Avani",
#              "Kabir", "Rohan", "Rahul", "Amit", "Sanjay", "Neha", "Priya", "Pooja", "Anjali", "Jyoti"],
#     "City": ["Mumbai","Delhi","Pune","Chennai","Bengaluru","Hyderabad","Ahmedabad","Mumbai","Jaipur","Lucknow"] * 3
# })


# marks_df = pd.DataFrame({
#     "StudentID": student_ids,
#     "Maths": np.random.randint(40, 100, 30),
#     "Science": np.random.randint(40, 100, 30),
#     "English": np.random.randint(40, 100, 30)
# })

# # 3. Attendance Table (Presence Percentage)
# attendance_df = pd.DataFrame({
#     "StudentID": student_ids,
#     "Attendance%": np.random.randint(60, 100, 30)
# })

# df=pd.merge(students_df,marks_df,on="StudentID",how="left")
# print(df)

# df_1=pd.merge(df,attendance_df,on="StudentID",how="right")
# print(df_1)
# try:
#     df_1.to_csv("data_1.csv")
# except:
#     print("error")



#bonus

# import pandas as pd
# import numpy as np


# customers_df = pd.DataFrame({
#     "CustomerID": [f"C{i:03d}" for i in range(1, 6)],  
#     "CustomerName": ["Amit", "Neha", "Rahul", "Priya", "Vikram"],
#     "City": ["Mumbai", "Chennai", "Pune", "Chennai", "Pune"]
# })


# products_df = pd.DataFrame({
#     "ProductID": [f"P{i:03d}" for i in range(1, 6)],  
#     "ProductName": ["Laptop", "Smartphone", "Wireless Headphones", "Smartwatch", "Tablet"],
#     "Price": [65000, 25000, 3500, 5000, 18000]
# })


# np.random.seed(42)  
# orders_df = pd.DataFrame({
#     "OrderID": [f"O{i:04d}" for i in range(1001, 1006)],
#     "ProductID": [f"P{i:03d}" for i in range(1, 6)],
#     "Quantity": np.random.randint(1, 6, size=5)
# })


# df=pd.merge(customers_df,products_df,left_index=True,right_index=True)
# print(df)

# df_1=pd.merge(df,orders_df,on="ProductID",how="left")
# print(df_1)

# df_1["Total Sale"]=df_1.apply(lambda row:row["Price"]*row["Quantity"],axis=1)
# print(df_1)

# print(df_1.groupby("City")["OrderID"].max())

# print(df_1.groupby("CustomerID").count())

#mixed1
# import pandas as pd
# import numpy as np


# emp_data = {
#     "EmpID": ["E01", "E02", "E03", "E04", "E05", "E02", "E06", "E07", "E08", "E09", "E10"],
#     "Name": ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Vivaan", "Sai", "Reyansh", "Krishna", "Ishaan", "Shaurya"],
#     "DeptID": ["D01", "D02", "D01", "D03", "D02", "D02", "D01", "D03", "D02", "D01", "D03"],
#     "Salary": [50000, 60000, np.nan, 75000, 80000, 60000, np.nan, 45000, 90000, 55000, np.nan]
# }
# employee_df = pd.DataFrame(emp_data)


# dept_data = {
#     "DeptID": ["D01", "D02", "D03", "D04"],
#     "Department": ["HR", "Engineering", "Marketing", "Sales"]
# }
# department_df = pd.DataFrame(dept_data)


# print("--- employee_df ---")
# print(employee_df)
# print("\n--- department_df ---")
# print(department_df)

# print(employee_df.isin(employee_df["Salary"]).sum())

# employee_df["Salary"]=employee_df["Salary"].fillna(employee_df["Salary"].median())
# print(employee_df)

# employee_df=employee_df.drop_duplicates()
# print(employee_df)

# df=pd.merge(employee_df,department_df,on="DeptID")

# print(df)

# group_by_department=df.groupby("Department")["EmpID"].count()
# print(group_by_department)

# group_by_department_as=df.groupby("Department")["Salary"].mean()
# print(group_by_department_as)

# sort_salary=df.sort_values("Salary")
# print(sort_salary)

#mixed2
# try:
#     employee_1=pd.read_csv("employee_details.csv")
#     print(employee_1)
#     employee_2=pd.read_csv("employee_salaries.csv")
#     print(employee_2)
# except Exception as e:
#     print(e)

# df=pd.merge(employee_1,employee_2,on="EmpID")
# print(df)

# print(df.info())

# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)

# group_by_city=df.groupby("City")["Name"].count()
# print(group_by_city)

# print(df["Salary"].nlargest(5))

#mixed3

# import pandas as pd


# employees_df = pd.DataFrame({
#     "EmpID": ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08"],
#     "Name": ["Aarav", "Ananya", "Vihaan", "Diya", "Kabir", "Ishani", "Arjun", "Meera"],
#     "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
#     "DeptID": ["D1", "D2", "D1", "D3", "D2", "D1", "D3", "D2"]
# })

# salaries_df = pd.DataFrame({
#     "EmpID": ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08"],
#     "BaseSalary": [75000, 85000, 62000, 95000, 71000, 58000, 88000, 91000]
# })


# departments_df = pd.DataFrame({
#     "DeptID": ["D1", "D2", "D3"],
#     "Department": ["Engineering", "Marketing", "Sales"]
# })

# gender_map={
#     "M":"Male",
#     "F":"Famale"
# }

# df_1=pd.merge(employees_df,salaries_df,on="EmpID")
# df=pd.merge(df_1,departments_df,how="left")
# print(df)

# df["Bonus"]=df["BaseSalary"].apply(lambda x:x*10/100)
# df["FinalSalary"]=df.apply(lambda row:row["BaseSalary"]+row["Bonus"],axis=1)
# print(df)

# df["Gender"]=df["Gender"].map(gender_map)
# print(df)

# group_by_dep=df.groupby("Department")["Gender"].count()
# print(group_by_dep)

# import pandas as pd

# employees = pd.DataFrame({
#     "EmpID":[1,2,3],
#     "Name":["Rahul","Neha","Amit"]
# })

# salary = pd.DataFrame({
#     "EmpID":[2,3,4],
#     "Salary":[60000,50000,70000]
# })

# print(pd.merge(employees, salary, on="EmpID", how="inner"))

# print(pd.merge(employees, salary, on="EmpID", how="left"))

# print(pd.merge(employees, salary, on="EmpID", how="outer"))

#--------------
# import pandas as pd

# jan = pd.DataFrame({
#     "OrderID":[101,102,103],
#     "Sales":[5000,7000,6500]
# })

# feb = pd.DataFrame({
#     "OrderID":[104,105,106],
#     "Sales":[6200,7100,8000]
# })

# #1
# print(jan)
# print(feb)

# #2
# print(pd.concat([jan,feb]))

# #3
# df=pd.concat([jan,feb],ignore_index=True)
# print(df)

# #4
# print(df["Sales"].sum())

# #5
# print(df.sort_values("Sales",ascending=False))

# #6
# customer = pd.DataFrame({
#     "Customer":["Rahul","Neha","Amit"]
# })

# city = pd.DataFrame({
#     "City":["Ahmedabad","Surat","Rajkot"]
# })

# print(pd.concat([customer,city],axis=1))

#7
# import pandas as pd
# import numpy as np

# jan = pd.DataFrame({
#     "OrderID":[101,102,103],
#     "Sales":[5000,7000,6500]
# })

# feb = pd.DataFrame({
#     "OrderID":[104,105,106],
#     "Sales":[6200,7100,8000]
# })

# mar = pd.DataFrame({
#     "OrderID":[107,108,109],
#     "Sales":[5000,8900,np.nan]
# })

# df=pd.concat([jan,feb,mar],ignore_index=True)
# print(df)

#8
# import pandas as pd
# import numpy as np
# customer = pd.DataFrame({
#     "Customer":["Rahul","Neha","Amit","Manthan","Khushbu","Aastha"]
# })

# city = pd.DataFrame({
#     "City":[np.nan,"Surat","np.nan","Ahmedabad","Baroda","Mahesana"]
# })

# print(pd.concat([customer,city],axis=1))

#9
# import pandas as pd
# import numpy as np
# np.random.seed(1)
# salary = pd.DataFrame({
#     "Salary":np.random.randint(20000,60000,10)
# })

# salary_1 = pd.DataFrame({
#     "Salary":np.random.randint(20000,60000,10)
# })

# salary_2 = pd.DataFrame({
#     "Salary":np.random.randint(20000,60000,10)
# })

# print(salary,salary_1,salary_2)

# df=pd.concat([salary,salary_1,salary_2],ignore_index=True)
# print(df)

#10

# import pandas as pd
# import numpy as np
# import names

# np.random.seed(1)
# ename= pd.DataFrame({
#     "Name":[names.get_full_name() for _ in range(20)]
# })
# print(ename)

# salary = pd.DataFrame({
#     "Salary":np.random.randint(20000,100000,20)
# })

# department = pd.DataFrame({
#     "Department": [
#     "Human Resources",
#     "Finance",
#     "Information Technology",
#     "Marketing",
#     "Sales",
#     "Research and Development",
#     "Customer Service",
#     "Operations",
#     "Legal",
#     "Product Management",
#     "Quality Assurance",
#     "Engineering",
#     "Supply Chain",
#     "Public Relations",
#     "Data Analytics",
#     "Design",
#     "Administration",
#     "Business Development",
#     "Training and Development",
#     "Security"
# ]
# })
# df=pd.concat([ename,salary,department],axis=1)
# print(df)

# print(df["Salary"].mean())

# print(df["Salary"].max())
# print(df.loc[df["Salary"].idxmax()])

# print(df[df["Salary"]>60000])

# print(df.sort_values("Salary",ascending=False))


#bonus1

# import pandas as pd
# import numpy as np

# jan = pd.DataFrame({
#     "OrderID":[101,102,103],
#     "Sales":[5000,np.nan,6500]
# })

# feb = pd.DataFrame({
#     "OrderID":[104,105,106],
#     "Sales":[6200,7100,8000]
# })

# mar = pd.DataFrame({
#     "OrderID":[107,108,109],
#     "Sales":[5000,8900,np.nan]
# })

# april=pd.DataFrame({
#     "OrderID":[110,111,112],
#     "Sales":[2300,np.nan,7400]
# })

# df=pd.concat([jan,feb,mar,april],ignore_index=True)

# df["Sales"]=df["Sales"].fillna(df["Sales"].mean())
# print(df)

# print(df["Sales"].sum())
# print(df["Sales"].mean())
# print(df["Sales"].nlargest(1))
# print(df["Sales"].nsmallest(1))

#bonus 2

# import pandas as pd
# import numpy as np

# np.random.seed(1)

# marks1= pd.DataFrame({
#     "Marks":np.random.randint(36,100,10)
# })

# marks2= pd.DataFrame({
#     "Marks":np.random.randint(36,100,10)
# })

# marks3 = pd.DataFrame({
#     "Marks":np.random.randint(36,100,10)
# })


# df=pd.concat([marks1,marks2,marks3],ignore_index=True)
# print(df)

# print(df["Marks"].mean())
# print(df["Marks"].nlargest(5))
# print(df[df["Marks"]>80])

#mixed1

# try:
#     emp=pd.read_csv("employes.csv")
#     salary=pd.read_csv("salaries.csv")
    
# except Exception as e:
#     print(e)

# # print(emp.info())
# # print(salary.info())

# df=pd.merge(emp,salary,on="Employee_ID")


# df["Final Salary"]=df["Base_Salary"]+df["Bonus"]
# print(df)

# midpoint = len(df) // 2

# part_1 = df.iloc[:midpoint]
# part_2 = df.iloc[midpoint:]

# print(part_1)
# print(part_2)

# d_1f=pd.concat([part_1,part_2])
# print(d_1f)

# print(df==d_1f)


#mixed 2

# import pandas as pd

# df_personal = pd.DataFrame({
#     'Name': ['Amit Kumar', 'Priya Singh', 'Rahul Jain', 'Sneha Roy', 'Mohit Verma'],
#     'Age': [28, 34, 31, 25, 29]
# })


# df_job = pd.DataFrame({
#     'Salary':[23654,43653,25545,65636,46646],
#     'Department': ['IT', 'HR', 'IT', 'Finance', 'Marketing']
# })

# df=pd.concat([df_personal,df_job],axis=1)
# print(df)

# print(df.loc[df["Salary"]>50000])

# print(df.sort_values("Salary",ascending=False))

#mixed3

# try:
#     salary=pd.read_csv("salaries.csv")
#     salary1=pd.read_csv("salaries1.csv")
    
# except Exception as e:
#     print(e)

# print(salary.info())
# print(salary1.info())

# df=pd.concat([salary,salary1])
# print(df.info())

# df["Sales"]=df["Sales"].fillna(df["Sales"].mean())
# print(df)

# group=df.groupby("Month")

# print(group["Sales"].sum())
# print(group["Sales"].mean())
# print(group["Sales"].max())
# print(df["Sales"].nlargest(1))

# jan = pd.DataFrame({
#     "Employee":["A","B"]
# })

# feb = pd.DataFrame({
#     "Employee":["C","D"]
# })

# mar = pd.DataFrame({
#     "Employee":["E","F"]
# })


# all_sales = (
#     pd.concat(
#         [jan, feb, mar],
#         keys=["January", "February", "March"]
#     )
#     .reset_index(level=0)
#     .rename(columns={"level_0": "Month"})
# )
# print(all_sales)

#------------------------------

#1

# employee=pd.DataFrame({
#     "Name":["Rahul","Neha","Amit"]
# })
# salary=pd.DataFrame({
#     "Salary":[50000,60000,45000]
# })

# df=employee.join(salary)
# print(df)

# #2
# city=pd.DataFrame({
#     "City":["Mumbai","Ahmedabad","Surat"]
# })
# df=employee.join([salary,city])
# print(df)

# #3
# print(df.loc[df["Salary"].idxmax()])
# print(df.loc[df["Salary"].idxmin()])
# print(df["Salary"].mean())

# #4
# print(df[df["Salary"]>50000])
# #5
# print(df.sort_values("Salary",ascending=False))
# #6

# employee=pd.DataFrame({
    
#     "Name":["Rahul","Neha","Amit"]
# },
# index=[101,102,103])

# salary=pd.DataFrame({
#     "Salary":[50000,60000,45000]
# },
# index=[101,102,103])

# city=pd.DataFrame({
#     "City":["Ahmebabad","Surat","Baroda"]
# },
# index=[101,104,105])

# print(employee.join(salary))

# #7
# print(employee.join([salary,city]))

# #8
# print(employee.join(city,how="inner"))
# #9
# print(employee.join(city,how="outer"))

#10
# import numpy as np
# import names
#
# np.random.seed(1)
#
# employees=pd.DataFrame({
#     "Name":[names.get_full_name() for _ in range(20)]
# })
#
# salary=pd.DataFrame({
#     "Salary":np.random.randint(20000,100000,20)
# })
#
# df=employees.join(salary)
# print(df)
#
# print(df["Salary"].mean())
# print(df["Salary"].max())
#
# print((df[["Salary","Name"]].nlargest(5,"Salary")))
#
# print((df[["Salary","Name"]].nlargest(1,"Salary")))

#bonus 1
# import pandas as pd
#
# employee_df = pd.DataFrame({
#     "Employee_ID":[101,102,103,104,105],
#     "Name": ["Pooja", "Alex", "David", "Rachel", "Michael"]
# })
#
# salary_df = pd.DataFrame({
#
#     "Salary": [85000, 92000, 78000, 95000, 81000]
# })
#
# department_df = pd.DataFrame({
#
#     "Department": ["IT", "Finance", "HR", "IT", "Marketing"]
# })
#
# city_df = pd.DataFrame({
#
#     "City": ["Mumbai", "Delhi", "Bangalore", "Mumbai", "Pune"]
# })
#
# df=employee_df.join([salary_df,department_df,city_df])
#
# print(df)
# df["Bonus"]=df["Salary"]*10/100
# df["Tax"]=df["Salary"]*7/100
# df["Net Salary"]=df["Salary"]+df["Bonus"]-df["Tax"]
#
# print(df)

#bonus2

# import pandas as pd
# import numpy as np
#
# np.random.seed(42)
#
# df_employees = pd.DataFrame({
#     "Employee_ID": range(101, 126),
#     "Name": [f"Employee_{i}" for i in range(101, 126)],
#     "Salary": np.random.randint(50000, 130000, size=25)
# })
#
# df_jobs = pd.DataFrame({
#
#     "Department": np.random.choice(["IT", "HR", "Finance", "Marketing"], size=20),
#     "City": np.random.choice(["Mumbai", "Delhi", "Bangalore", "Pune"], size=20)
# })
#
# print(df_employees.join(df_jobs))

#because values have Nan because of de_employees have 25 size record and df_jobs have 20 size record that's why join the index and same index but not a value so NaN

# mixed1

# try:
#     employees=pd.read_csv("input_employees.csv")
#     salaries=pd.read_csv("input_salaries.csv")
# except FileNotFoundError:
#     print("File not found")
#
# df=employees.join(salaries)
#
# # print(df.info())
#
# df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
#
# df["Bonus"]=df["Salary"]*10/100
# df["Net Salary"]=df["Salary"]+df["Bonus"]
# print(df)
#
# print(df.sort_values("Salary"))
#
# df.to_csv("final_exported_output.csv")

#MIXED2

# import pandas as pd
#
# df_employees = pd.DataFrame({
#     'EmpID':[101,102,103,104,105],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Salary':[45000,34200,43533,65456,56345]
# })
#
# df_departments = pd.DataFrame({
#     'DeptID': [1, 2, 1, 3, 2],
#     'Department': ['HR', 'Engineering', 'HR','Sales','Engineering']
# })
#
# df_salaries = pd.DataFrame({
#
#     'City': ['New York', 'San Francisco', 'New York', 'Chicago', 'San Francisco']
# })
#
#
# df=df_employees.join([df_departments, df_salaries])
# print(df)
#
# print(df.groupby("Department")["Salary"].mean())
# print(df.groupby("City")["Salary"].nlargest(1))

#mixed3

# import pandas as pd
#
#
# df_employees = pd.DataFrame({
#     'EmpID':[101,102,103,104,105],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Salary': [70000, 95000, 80000, 65000, 90000]
# })
#
#
# df_performance = pd.DataFrame({
#     'Score': [3, 5, 4, 2, 5]
# })
#
# score_to_grade = {5: 'Excellent', 4: 'Good', 3: 'Satisfactory', 2: 'Needs Improvement', 1: 'Poor'}
#
# df=df_employees.join(df_performance)
#
# df["Grades"]=df["Score"].map(score_to_grade)
# print(df)
#
# print(df[df["Grades"]=="Excellent"])
#
# print(df.sort_values("Salary", ascending=False))
# 

#-----------------------------
#1
# df=pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya"],
#     "Department":["IT","HR","IT","HR"],
#     "Salary":[50000,62000,58000,70000] 
# })
# print(df)
# print(df.pivot_table(index="Department",values="Salary",aggfunc="mean"))

#2
# df=pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Department":["IT","HR","IT","HR","IT"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Rajkot","Surat"],

#     "Salary":[50000,62000,58000,70000,64000] 
# })
# print(df)
# print(df.pivot_table(index="Department",columns="City",values="Salary",aggfunc="mean"))

#3
# print(df.pivot_table(index="Department",values="Salary",aggfunc="max"))

#4
# print(df.pivot_table(index="Department",values="Name",aggfunc="count"))

#5
# df=pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Department":["IT","HR","IT","HR","IT"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Rajkot","Surat"],
#     "Age":[32,25,28,21,22],
#     "Salary":[50000,62000,58000,70000,64000] 
# })
# print(df)
# print(df.pivot_table(index="Department",values=["Salary","Age"],aggfunc="mean"))

#6
# import numpy as np

# df=pd.DataFrame({
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Department":["IT","HR","IT","HR","IT"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Rajkot",np.nan],
#     "Age":[32,25,np.nan,21,22],
#     "Salary":[np.nan,62000,58000,70000,64000] 
# })
# print(df)
# print(df.pivot_table(index="Department",values=["Salary","Age"],aggfunc="mean",fill_value=0))
# #
# 7
# print(df.pivot_table(index="Department",values="Age",aggfunc="mean",fill_value=0,margins=True))

#8
# import numpy as np
# import names

# np.random.seed(42)

# df=pd.DataFrame({
#    "Name":[names.get_full_name() for _ in range(20)],
#    "Department":np.random.choice(["Finance", "Sales", "HR", "IT"],20),
#    "City":np.random.choice(["Ahmedabad","Surat","Mumbai","Chhenai","Bengalor"],20),
#    "Salary":np.random.randint(20000,100000,20)
# })
# print(df)

# print(df.pivot_table(index=["Department","City"],values="Salary",aggfunc="mean"))

# #9
# print(df.pivot_table(index="City",values="Salary",aggfunc=["mean","max","min","count"]))

# #10
# print(df.pivot_table(index="Department",columns="City",values="Salary",aggfunc=["mean","max","count"],fill_value=0,margins_name=True))

#bonus1
# sales_data = [
#     {"Product": "iPhone 15", "Category": "Electronics", "City": "New York", "Sales": 1200},
#     {"Product": "Leather Jacket", "Category": "Clothing", "City": "Los Angeles", "Sales": 250},
#     {"Product": "Ergonomic Chair", "Category": "Furniture", "City": "Chicago", "Sales": 350},
#     {"Product": "Running Shoes", "Category": "Clothing", "City": "New York", "Sales": 120},
#     {"Product": "4K Monitor", "Category": "Electronics", "City": "San Francisco", "Sales": 450},
#     {"Product": "Dining Table", "Category": "Furniture", "City": "Houston", "Sales": 800},
#     {"Product": "Wireless Headphones", "Category": "Electronics", "City": "Los Angeles", "Sales": 180},
#     {"Product": "Summer Dress", "Category": "Clothing", "City": "Miami", "Sales": 85},
#     {"Product": "Sofa Bed", "Category": "Furniture", "City": "Chicago", "Sales": 950},
#     {"Product": "Mechanical Keyboard", "Category": "Electronics", "City": "Seattle", "Sales": 130},
#     {"Product": "Winter Coat", "Category": "Clothing", "City": "Boston", "Sales": 300},
#     {"Product": "Office Desk", "Category": "Furniture", "City": "San Francisco", "Sales": 400},
#     {"Product": "Smart Watch", "Category": "Electronics", "City": "Austin", "Sales": 250},
#     {"Product": "Denim Jeans", "Category": "Clothing", "City": "Denver", "Sales": 75},
#     {"Product": "Bookshelf", "Category": "Furniture", "City": "Seattle", "Sales": 220}
# ]

# df=pd.DataFrame(sales_data)
# print(df)
# print(df.pivot_table(index="Category",values="Sales",aggfunc="mean"))
# print(df.pivot_table(index="City",values="Sales",aggfunc="mean"))

# print(df.pivot_table(index=["City","Category"],values="Sales",aggfunc="mean"))

# print(df.pivot_table(index="Category",values="Sales",aggfunc="max"))
# print(df.pivot_table(index="City",values="Sales",aggfunc="max"))

# print(df.pivot_table(index=["City","Category"],values="Sales",aggfunc="max"))

# print(df.pivot_table(index="Category",values="Sales",aggfunc="sum"))
# print(df.pivot_table(index="City",values="Sales",aggfunc="sum"))

# print(df.pivot_table(index=["City","Category"],values="Sales",aggfunc="sum"))

#bonus2
# student_data = [
#     {"Student": "Liam Smith", "Class": "Grade 10", "Subject": "Mathematics", "Marks": 88},
#     {"Student": "Noah Jones", "Class": "Grade 11", "Subject": "Physics", "Marks": 92},
#     {"Student": "Oliver Brown", "Class": "Grade 10", "Subject": "English", "Marks": 79},
#     {"Student": "Elijah Davis", "Class": "Grade 12", "Subject": "Chemistry", "Marks": 85},
#     {"Student": "James Miller", "Class": "Grade 11", "Subject": "Mathematics", "Marks": 95},
#     {"Student": "William Wilson", "Class": "Grade 10", "Subject": "Physics", "Marks": 74},
#     {"Student": "Benjamin Moore", "Class": "Grade 12", "Subject": "Biology", "Marks": 91},
#     {"Student": "Lucas Taylor", "Class": "Grade 11", "Subject": "English", "Marks": 83},
#     {"Student": "Henry Anderson", "Class": "Grade 10", "Subject": "Chemistry", "Marks": 68},
#     {"Student": "Alexander Thomas", "Class": "Grade 12", "Subject": "Mathematics", "Marks": 77},
#     {"Student": "Mia Jackson", "Class": "Grade 11", "Subject": "Biology", "Marks": 89},
#     {"Student": "Ava White", "Class": "Grade 10", "Subject": "History", "Marks": 94},
#     {"Student": "Emma Harris", "Class": "Grade 12", "Subject": "Physics", "Marks": 81},
#     {"Student": "Sophia Martin", "Class": "Grade 11", "Subject": "Chemistry", "Marks": 76},
#     {"Student": "Charlotte Garcia", "Class": "Grade 12", "Subject": "English", "Marks": 88}
# ]
# df=pd.DataFrame(student_data)
# print(df)

# print(df.pivot_table(index="Class",values="Marks",aggfunc="mean"))
# print(df.pivot_table(index="Subject",values="Marks",aggfunc="mean"))

# print(df.pivot_table(index=["Class","Subject"],values="Marks",aggfunc="mean"))

# # print(df.pivot_table(index="Class",values="Marks",aggfunc="max"))
# # print(df.pivot_table(index="Subject",values="Marks",aggfunc="max"))

# print(df.pivot_table(index=["Class","Subject"],values="Marks",aggfunc="max"))

# # print(df.pivot_table(index="Class",values="Marks",aggfunc="count"))
# # print(df.pivot_table(index="Subject",values="Marks",aggfunc="count"))
# print(df.pivot_table(index=["Class","Subject"],values="Marks",aggfunc="count"))

#Mixed1

# try:
#         df=pd.read_csv("mixed_pivottable.csv")
# except Exception as e:
#     print(e)
        
# print(df.info())

# df["Salary"]=df["Salary"].fillna(df["Salary"].median())


# df["Bonus"]=df["Salary"]*10/100
# df["Net Salary"]=df["Salary"]+df["Bonus"]
# print(df)

# print(df.pivot_table(index="Department",values="Salary",aggfunc="mean"))


# #mixed2
# import pandas as pd


# employees = pd.DataFrame({
#     "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108],
#     "Name": ["Anita Sharma","Rajesh Patel","Meena Gupta","Vikram Singh",
#              "Sunita Rao","Arjun Mehta","Kavita Joshi","Suresh Kumar"],
#     "Department": ["HR","IT","Finance","IT","Marketing","Finance","HR","Marketing"],
#     "City": ["Delhi","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai"]
# })


# salaries = pd.DataFrame({
#     "EmployeeID": [101,102,103,104,105,106,107,108],
#     "Salary": [55000,None,62000,72000,None,58000,None,50000]
# })

# df=pd.merge(employees,salaries,on="EmployeeID",how="outer")
# print(df)
# print(df.pivot_table(index="City",values="Salary",aggfunc="mean"))
# print(df.pivot_table(index="Department",values="Salary",aggfunc="max"))

#mixed3

# try:
#     jan=pd.read_csv("sales_jan.csv")
#     feb=pd.read_csv("sales_feb.csv")
#     mar=pd.read_csv("sales_mar.csv")
# except Exception as e:
#     print(e)

# df = pd.concat([jan, feb, mar], keys=["January", "February", "March"]).reset_index(level=0).rename(columns={"level_0": "Month"})
# print(df.info())
# print(df)

# print(df.pivot_table(index="Month",values="Sales",aggfunc=["sum","mean"]))

#-----------------------------

#1

# df=pd.DataFrame({
#     "Name":["Manthan","Khushbu","Aastha","Manthan","Khushbu","Aastha","Manthan","Khushbu","Aastha"],
#     "Month":["January","January" ,"January" ,"February","February","February","March","March","March"],
#     "Salary":[40000,70000,60000,40000,70000,60000,40000,70000,60000,]
# })
# print(df)
# print(df.pivot(index="Name",columns="Month",values="Salary"))

# #2
# df=pd.DataFrame({
#     "Name":["Manthan","Khushbu","Aastha","Manthan","Khushbu","Aastha","Manthan","Khushbu","Aastha"],
#     "Subject":["Math","Math","Math","Science","Science","Science","English","English","English"],
#     "Marks":[45,75,65,63,75,67,78,65,89]
# })
# print(df)
# print(df.pivot(index="Name",columns="Subject",values="Marks"))
# #3

# sales_data = {
#     "Year": [2023, 2023, 2023, 2024, 2024, 2024, 2025, 2025, 2025, 2026, 2026, 2026],
#     "City": ["New York", "Los Angeles", "Chicago", "New York", "Los Angeles", "Chicago", 
#              "New York", "Los Angeles", "Chicago", "New York", "Los Angeles", "Chicago"],
#     "Sales_Volume": [1520, 1180, 940, 1650, 1240, 890, 1710, 1310, 980, 1850, 1420, 1050],
#     "Revenue_USD": [456000, 354000, 282000, 495000, 372000, 267000, 513000, 393000, 294000, 555000, 426000, 315000]
# }
# df = pd.DataFrame(sales_data)

# print(df.pivot(index="Year",columns="City",values=["Sales_Volume","Revenue_USD"]))

# #4

# quarterly_data = {
#     "Product": ["Laptop", "Smartphone", "Tablet", "Laptop", "Smartphone", "Tablet",
#                 "Laptop", "Smartphone", "Tablet", "Laptop", "Smartphone", "Tablet"],
#     "Quarter": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2", 
#                 "Q3", "Q3", "Q3", "Q4", "Q4", "Q4"],
#     "Units_Sold":[4,32,35,36,36,25,43,65,34,64,35,66],
#     "Revenue_USD": [1440000, 1250000, 320000, 1740000, 1350000, 380000,
#                     1320000, 1550000, 280000, 2280000, 2100000, 520000]
# }

# df_products = pd.DataFrame(quarterly_data)

# print(df_products.pivot(index="Product",columns="Quarter",values=["Units_Sold","Revenue_USD"]))

# #5
# performance_data = {
#     "Employee": ["Alex Jones", "Maria Silva", "Kenji Sato", 
#                  "Alex Jones", "Maria Silva", "Kenji Sato",
#                  "Alex Jones", "Maria Silva", "Kenji Sato"],
#     "Month": ["January", "January", "January", 
#               "February", "February", "February", 
#               "March", "March", "March"],
#     "Tasks_Completed":[34,43,64,35,55,34,46,36,64],
#     "Performance_Score": [8.5, 9.2, 7.8, 8.9, 9.0, 8.2, 9.1, 9.5, 8.6]
# }

# df_performance = pd.DataFrame(performance_data)

# print(df_performance.pivot(index="Employee",columns="Month",values=["Tasks_Completed","Performance_Score"]))

#6
# import numpy as np
#
# np.random.seed(42)
#
# products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
# months = ['January', 'February', 'March', 'April', 'May', 'June',
#           'July', 'August', 'September', 'October', 'November', 'December']
#
# random_products = np.random.choice(products, size=20)
# random_months = np.random.choice(months, size=20)
# random_sales = np.random.randint(50, 500, size=20)
#
# df_random_sales = pd.DataFrame({
#     "Product": random_products,
#     "Month": random_months,
#     "Sales": random_sales
# })
# print(df_random_sales)
# df_random_sales=df_random_sales.drop_duplicates("Product")
# df_random_sales=df_random_sales.drop_duplicates("Month")
# df_random_sales=df_random_sales.drop_duplicates("Sales")
# print(df_random_sales)
# print(df_random_sales.pivot(index="Product",columns="Month",values="Sales"))

#---------------------------

#1

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha"],
#     "Jan":[50000,60000],
#     "Feb":[52000,62000],
#     "Mar":[54000,64000]
# })
#
# print(df)
#
# print(pd.melt(
#     df,
#     id_vars="Employee",
#     var_name="Month",
#     value_name="Salary"
# ))

#2

# df = pd.DataFrame({
#     "Student":["Rahul","Neha"],
#     "Math":[50000,60000],
#     "Science":[52000,62000],
#     "English":[54000,64000]
# })
#
# print(df)
#
# print(pd.melt(
#     df,
#     id_vars="Student",
#     var_name="Subject",
#     value_name="Marks"
# ))

#3

# df = pd.DataFrame({
#     "Product":["Laptop","Mobile"],
#     "Q1":[120,150],
#     "Q2":[140,170],
#     "Q3":[160,180],
#     "Q4":[180,190],
# })
#
# print(pd.melt(
#     df,
#     id_vars="Product",
#     var_name="Quarter",
#     value_name="Sales"
# ))

#4
# df = pd.DataFrame({
#     "City":["Surat","Ahmedabad","Mumbai"],
#     "2023":[120,150,190],
#     "2024":[140,170,100],
#     "2025":[160,180,165]
# })
# print(df.melt(id_vars="City",var_name="Years",value_name="Population"))

#5

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Manthan","Khushbu"],
#     "Jan":[50000,60000,53533,64664],
#     "Feb":[52000,62000,63633,67574],
#     "Mar":[54000,64000,45644,76567],
#     "Apr":[54000,65000,45644,76567],
# })
#
# df=df.melt(id_vars="Employee",var_name="Month",value_name="Salary")
# print(df)
# print(df.sort_values(by="Salary",ascending=False))

#--------------------------------------------

#1

# df=pd.DataFrame({
#     "Name":["Khushbu","Manthan","Aastha"]
# })
#
# df["Name"]=df["Name"].str.upper()
# print(df)
#
# #2
#
# df=pd.DataFrame({
#     "Name":["KHUSHBU SHAH","MANTHAN PATEL","AASTHA PATEL"]
# })
#
# df["Name"]=df["Name"].str.lower()
# print(df)
#
# #3
# df["Name"]=df["Name"].str.title()
# print(df)

#4
# df=pd.DataFrame({
#     "Name":[" KHUSHBU SHAH ","   MANTHAN PATEL "," AASTHA PATEL"]
# })
# print(df)
# df["Name"]=df["Name"].str.strip().str.title()
#
# print(df)
#
# #5
# df=pd.DataFrame({
#     "City":["Ahmebabad","Surat","Mumbai","Chhenai","Dehli","Gurugram"]
# })
# print(df["City"].str.len())

#6
# df=pd.DataFrame({
#     "City":["Ahmebabad","Bombay","Bombay","Chhenai","Dehli","Bombay"]
# })
# df["City"]=df["City"].str.replace("Bombay","Mumbai")
# print(df)

#7
# df=pd.DataFrame({
#     "Email":["manthan@gmail.com","khushbu@outlook.com","aastha@yahoo.com","khushubu@gmail.com","aastha@gmail.com","admin@yahoo.com"]
# })

# df=df[df["Email"].str.contains("gmail.com")]
# print(df)

#8
# df=df[df["Email"].str.startswith("admin")]
# print(df)

#9
# df=df[df["Email"].str.endswith(".com")]
# print(df)

#10
# df[["Username", "Domain"]] = df["Email"].str.split("@", expand=True)
# print(df)

#bonus1

# import names
# from faker import Faker
#
# fake = Faker()
#
# df = pd.DataFrame({
#     "Name": [names.get_full_name() for _ in range(30)],
#     "Email": [fake.unique.email() for _ in range(30)]
# })
#
# df["Name"]=df["Name"].str.title()
# print(df)
#
# print(df[df["Name"].str.contains("gmail")])
#
# df[["Username","Domain"]]=df["Email"].str.split("@",expand=True)
# print(df)
#
# print(df["Username"].str.len())

#bonus2
# import pandas as pd
#
# df = pd.DataFrame({
#     "Product": [
#         "  Laptop Pro 15 ", "wireless Mouse", "PRO Keyboard", "smart Watch",
#         "Phone pro Max", "Tablet Air", " Gaming Headset ", "Bluetooth Speaker",
#         "Camera Pro X", "USB Cable", "Power Bank", " Pro Charger ",
#         "Monitor HD", "Desk Lamp", "Office Chair", "Pro Dock",
#         "External SSD", "Webcam pro", "Printer", "Scanner Pro",
#         "Fitness Band", "Smart Plug", "Coffee Maker Pro", "Electric Kettle",
#         "Air Purifier", " Vacuum Cleaner ", "Robot Pro Vacuum", "Water Bottle",
#         "Travel Backpack", "Pro Earbuds", "Gaming Mouse", "Mechanical Keyboard",
#         "Phone Stand", "Laptop Sleeve", "Wireless Charger Pro", "Microphone",
#         "Ring Light Pro", "Action Camera", "Drone Pro", "Projector",
#         "Mini PC", "Graphics Tablet Pro", "Smart Lock", "Doorbell Camera",
#         "VR Headset Pro", "Router", "WiFi Extender Pro", "Portable Monitor",
#         "Streaming Stick", "Pro Tripod"
#     ],
#     "Brand": [
#         " Facebook ", "twitter", "SONY", "samsung",
#         "Apple", " facebook", "Logitech", "TWITTER",
#         "Canon", "anker", "Xiaomi", "facebook",
#         "LG", "Philips", "IKEA", "Twitter",
#         "Samsung", "logitech", "HP", "CANON",
#         "Fitbit", "TP-Link", "Philips", "Prestige",
#         "Dyson", " samsung ", "Xiaomi", "Milton",
#         "Wildcraft", "APPLE", "Logitech", "Keychron",
#         "Spigen", "HP", "Anker", "Blue",
#         "Sony", "DJI", "DJI", "Epson",
#         "Intel", "Wacom", "Yale", "Google",
#         "Meta", "Netgear", "TP-link", "LG",
#         "Amazon", "Manfrotto"
#     ],
#     "Price": [
#         1200, 25, 90, 250, 999, 650, 80, 60, 1400, 12,
#         45, 35, 300, 40, 180, 110, 150, 75, 220, 260,
#         70, 30, 95, 55, 400, 350, 600, 20, 85, 130,
#         50, 140, 18, 28, 65, 120, 150, 500, 900, 450,
#         700, 320, 180, 210, 800, 95, 110, 270, 60, 85
#     ]
# })
#
# print(df)
#
# df["Product"]=df["Product"].str.strip()
#
# df["Brand"]=df["Brand"].str.strip()
#
# df["Product"]=df["Product"].str.capitalize()
#
# df["Brand"]=df["Brand"].str.capitalize()
#
# print(df)
#
# print(df[df["Product"].str.contains("Pro")])

#mixed1

# try:
#     product=pd.read_csv("products.csv")
#     suppliers=pd.read_csv("suppliers.csv")
# except Exception as e:
#     print(e)
#
# print(product.info())
# print(suppliers.info())
#
# df=pd.merge(product,suppliers,how="inner",on="SupplierID")
# print(df)
#
# print(df.info())
#
# df["Category"]=df["Category"].fillna("No Category")
# df["Brand"]=df["Brand"].fillna("No Brand")
# df["Price"]=df["Price"].fillna(df["Price"].mean())
# df["Quantity"]=df["Quantity"].fillna(0)
#
#
# df=df.drop_duplicates()
#
# print(df.info())
#
# df["Product"]=df["Product"].str.strip()
# df["Category"]=df["Category"].str.strip()
# df["Brand"]=df["Brand"].str.strip()
# df["SupplierID"]=df["SupplierID"].str.strip()
# df["Supplier"]=df["Supplier"].str.strip()
# df["City"]=df["City"].str.strip()
#
# df["Product"]=df["Product"].str.title()
# df["Category"]=df["Category"].str.title()
# df["Brand"]=df["Brand"].str.title()
# df["SupplierID"]=df["SupplierID"].str.title()
# df["Supplier"]=df["Supplier"].str.title()
# df["City"]=df["City"].str.title()
#
# print(df.groupby("Brand")["Product"].count())
#
# df=df.sort_values("Product")
# print(df)
#
# print(df[df["Product"].str.contains("A")])

#Mixed

# try:
#     employees=pd.read_csv('employees_str.csv')
#     salary=pd.read_csv('salary_str.csv')
# except FileNotFoundError:
#     print('File not found')
#
# print(employees.info())
# print(employees.describe())
# print(salary.info())
# print(salary.describe())
# print(salary.isna().sum())
# print(salary.isna().sum())
#
# employees["Age"]=employees["Age"].fillna(employees["Age"].mean())
# salary["Salary"]=salary["Salary"].fillna(salary["Salary"].median())
#
# print(employees.info())
#
# print(salary.info())
#
# df=pd.merge(employees,salary,on="EmpID",how="inner")
# df["Name"]=df["Name"].str.strip().str.title()
# df["City"]=df["City"].str.strip().str.title()
# df=df.drop_duplicates("Name")
# print(df)
# df["Bonus"]=df["Salary"]*10/100
# df["Net Salary"]=df["Salary"]+df["Bonus"]
# print(df)
# print(df[df["Salary"]>55000])
# print(df[df["Department"]=="IT"])
# print(df.sort_values("Salary",ascending=False))
#
# print(df.groupby("Department")["Salary"].agg(["mean","max","count"]))
# df.to_csv("employee_clean_report.csv")

#mixed
# try:
#     data=pd.read_csv('data_email.csv')
# except FileNotFoundError:
#     print('File not found')
#
# print(data.info())
# print(data.describe())
# print(data.head(1))
# print(data.tail(1))
#
# data["Purchase"]=data["Purchase"].fillna(data["Purchase"].median())
# data["Name"]=data["Name"].str.strip().str.title()
# data=data.drop_duplicates("Name")
# print(data)
# data[["Username","Domain"]]=data["Email"].str.split("@",expand=True)
# print(data)
# print(data[data["Email"].str.contains("gmail")])
# data["VIP Customer"]=data["Purchase"].apply(lambda x:"VIP" if x>6000 else "Regular")
# print(data)
# print(data.sort_values("Purchase",ascending=False))
# group_by_city=data.groupby("City")
# print(group_by_city["Purchase"].mean())
# print(group_by_city["Purchase"].max())
# print(group_by_city["Purchase"].count())

#-----------------------------------------------

#1
# df = pd.DataFrame({
#     "Department":["IT","HR","IT","Sales","HR"],
#     "Gender":["M","F","M","F","F"]
# })

# print(pd.crosstab(df["Department"],df["Gender"]))

# #2
# print(pd.crosstab(df["Department"],df["Gender"],margins=True))

# #3
# print(pd.crosstab(df["Department"],df["Gender"],normalize="index"))

# #4
# print(pd.crosstab(df["Department"],df["Gender"],normalize="columns"))

# #5
# print(pd.crosstab(df["Department"],df["Gender"],normalize=True))

#6
# df = pd.DataFrame({
#     "Department":["IT","HR","IT","HR","Sales"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Rajkot","Surat"]
# })

# print(pd.crosstab(df["Department"],df["City"]))

#7
# df = pd.DataFrame({
#     "Department":["IT","IT","HR","Sales","HR"],
#     "Gender":["M","F","F","M","F"],
#     "Salary":[50000,65000,62000,70000,55000]
# })

# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="mean"))

# #8
# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="max"))

# #9
# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="sum"))

# #10
# df = pd.DataFrame({
#     "Department":["IT","IT","HR","Sales","HR"],
#     "Gender":["M","F","F","M","F"],
#     "Salary":[50000,65000,62000,70000,55000]
# })

# print(pd.crosstab(df["Department"],df["Gender"],normalize="index",margins=True,margins_name="Total"))

#bonus1
# import numpy as np

# np.random.seed(33)

# df=pd.DataFrame({
#     "Department":np.random.choice(["HR","IT","Sales","Marketing","Purchase","Finance"],size=30),
#     "Gender":np.random.choice(["Male","Female"],size=30),
#     "City":np.random.choice(["Ahmedabad","Surat","Baroda","Mumbai","Chhenai"],size=30),
#     "Salary":np.random.randint(20000,100000,30)
# })

# print(pd.crosstab(df["Department"],df["Gender"]))
# print(pd.crosstab(df["City"],df["Gender"]))
# print(pd.crosstab(df["Department"],df["City"]))
# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="mean"))

# #bonus2

# import pandas as pd

# supermarket_data = {
#     "Product": ["Milk", "Shampoo", "Soft Drink", "Rice", "Bread", "Detergent", "Coffee", "Soap", "Cooking Oil", "Yogurt"],
#     "Category": ["Dairy & Bakery", "Personal Care", "Beverages", "Groceries", "Dairy & Bakery", "Household Supplies", "Beverages", "Personal Care", "Groceries", "Dairy & Bakery"],
#     "PaymentMode": ["UPI", "Credit Card", "Cash", "UPI", "Debit Card", "Mobile Wallet", "Cash", "UPI", "Credit Card", "Debit Card"],
#     "Sales": [120.50, 450.00, 95.00, 850.00, 60.00, 320.00, 210.00, 85.00, 1250.00, 110.00]
# }

# df = pd.DataFrame(supermarket_data)

# print(df)

# print(pd.crosstab(df["Category"],df["PaymentMode"]))

# print(pd.crosstab(df["Category"],df["PaymentMode"],normalize=True))

# print(pd.crosstab(df["Category"],df["PaymentMode"],values=df["Sales"],aggfunc="sum",margins=True))

# print(pd.crosstab(df["Category"],df["PaymentMode"],values=df["Sales"],aggfunc="mean"))

#mixed1

# try:
#     employees=pd.read_csv("mixed1_crosstab.csv")
#     salary=pd.read_csv("mixed1_crosstab1.csv")
# except Exception as e:
#     print(e)

# print(employees.info())
# print(salary.info())

# df=pd.merge(employees,salary,on="EmployeeID",how="outer")
# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# df["Bonus"]=df["Salary"]*10/100
# df["Net Salary"]=df["Salary"]+df["Bonus"]
# df["Salary Category"]=df["Salary"].apply(lambda x:"High" if x>65000 else "Normal")
# print(df)

# print(df.groupby("Department")["Salary"].mean())

# print(df.sort_values("Salary"))

# print(pd.crosstab(df["Department"],df["Gender"],margins=True))
# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="mean"))
# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="max"))
# print(df.nlargest(5, "Salary"))
# print(df["Salary"].nlargest(5))

#mixed2

# try:
#     df=pd.read_csv("mixed2_crosstab.csv")

# except Exception as e:
#     print(e)

# print(df.info())


# df["Price"]=df["Price"].fillna(df["Price"].mean())
# df["PaymentMode"]=df["PaymentMode"].fillna("Not Found")
# print(df)

# df=df.drop_duplicates()
# print(df)

# print(df.pivot_table(values="Price",index="Category",columns="PaymentMode"))

# print(df.pivot_table(values="Quantity",index="Category",columns="PaymentMode"))

# print(pd.crosstab(df["Category"],df["PaymentMode"]))

# df.to_csv("Finalcrosstab_mixed2.csv")

# mixed3

# import numpy as np

# np.random.seed(33)

# df=pd.DataFrame({
#     "Department":np.random.choice(["HR","IT","Sales","Marketing","Purchase","Finance"],size=300),
#     "Gender":np.random.choice(["Male","Female"],size=300),
#     "City":np.random.choice(["Ahmedabad","Surat","Baroda","Mumbai","Chhenai"],size=300),
#     "Salary":np.random.randint(20000,100000,300)
# })

# print(df.groupby("Department")["Salary"].mean())
# print(df.pivot_table(values="Salary",index="Department",columns="City"))

# print(pd.crosstab(df["Department"],df["Gender"]))

# df=df.sort_values("Salary")

# df.to_csv("Finalcross_mixed2.csv")

# Mentor Challenge

# import numpy as np

# np.random.seed(33)

# empid=[]
# for i in range(50):
#     empid.append("E"+str(i))

# df=pd.DataFrame({
#     "EmpID":empid,
#     "Department":np.random.choice(["HR","IT","Sales","Marketing","Purchase","Finance"],size=50),
#     "Gender":np.random.choice(["Male","Female"],size=50),
#     "City":np.random.choice(["Ahmedabad","Surat","Baroda","Mumbai","Chhenai"],size=50),
#     "Salary":np.random.randint(20000,100000,50),
#     "Experience":np.random.randint(1,20,50)
# })

# df.to_csv("employees_crosstab.csv")
# try:
#     df=pd.read_csv("employees_crosstab.csv")
# except:
#     print("Not open")

# print(df.info())

# print(df.isna().sum())

# print(pd.crosstab(df["Department"],df["Gender"]))
# print(pd.crosstab(df["Department"],df["City"]))

# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="mean"))

# print(pd.crosstab(df["Department"],df["City"],values=df["Salary"],aggfunc="max"))

# print(df.nlargest(5,"Salary"))

# print(df.pivot_table(values="Salary",index="Department",columns="City",aggfunc="mean"))


# df.to_csv("employees_crosstab.csv")

#-------------------------------------------------------------------------


# import pandas as pd

# df = pd.DataFrame({
#     "OrderID":[101,102,103,104,105],
#     "OrderDate":[
#         "2025-01-10",
#         "2025-02-15",
#         "2025-03-20",
#         "2025-04-25",
#         "2025-05-30"
#     ],
#     "Sales":[500,700,650,900,800]
# })
# df["OrderDate"] = pd.to_datetime(df["OrderDate"])
# print(df["OrderDate"])


# df["OrderDate"]=df["OrderDate"].dt.year
# print(df["OrderDate"])

# df["OrderDate"]=df["OrderDate"].dt.month
# print(df["OrderDate"])

# print(df["OrderDate"].dt.month_name())

# print(df["OrderDate"].dt.day)

# print(df["OrderDate"].dt.day_name())

# print(df["OrderDate"].dt.quarter)

# print(df["OrderDate"].dt.is_month_end)

# print(df[df["OrderDate"]>"2025-03-01"])

# df["Weekend"]=df["OrderDate"].dt.weekday.apply(lambda x:True if x==5 or x==6 else False)
# print(df["Weekend"])
# print(df)

#bonus

# df = pd.DataFrame(
#     {
#         "Date": pd.date_range(start="2026-01-01", end="2026-12-31",freq="MS"),
#     }
# )
# mapping={
#     1:"Winter",
#     2:"Winter",
#     3:"Summer",
#     4:"Summer",
#     5:"Summer",
#     6:"Summer",
#     7:"Monsoon",
#     8:"Monsoon",
#     9:"Monsoon",
#     10:"Monsoon",
#     11:"Winter",
#     12:"Winter",
# }
# print(df)

# df["Month"]=df["Date"].dt.month
# print(df)

# df["Month Name"]=df["Date"].dt.month_name()
# print(df)

# #bonus
# import pandas as pd


# data = {
#     "Order_ID":["O101","O102","O103","O104"],
#     "Order_Date": ["2026-07-01", "2026-07-05", "2026-07-10", "2026-07-12"],
#     "Delivery_Date": ["2026-07-06", "2026-07-07", "2026-07-16", "2026-07-13"],
# }
# df = pd.DataFrame(data)
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Delivery_Days"] = (df["Delivery_Date"] - df["Order_Date"]).dt.days

# print(df)

#minxed1:

# try:
#     df=pd.read_csv("mixed1_datetime.csv")
# except Exception as e:
#     print(e)

# print(df.info())

# df["Discount"]=df["Discount"].fillna(df["Discount"].median())
# print(df)

# df["Order_Date"]=pd.to_datetime(df["Order_Date"])


# df["Month Name"]=df["Order_Date"].dt.month_name()
# print(df)

# print(df.groupby("Category")["Sales"].mean())

# print(df.sort_values("Quantity"))

# print(df.pivot_table(values="Discount",index="Category",columns="Product"))

#mixed2

# try:
#     df1=pd.read_csv("mixed2_datetime.csv")
#     df2=pd.read_csv("mixed2_datetime1.csv")
#     df3=pd.read_csv("mixed2_datetime2.csv")
# except Exception as e:
#     print(e)

# df=pd.merge(df1,df2,on="Customer_ID",how="inner")
# df=pd.merge(df,df3,on="Order_ID",how="inner")

# df["Order_Date"]=pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"]=pd.to_datetime(df["Delivery_Date"])

# df["Delivery Time"]=df["Delivery_Date"]-df["Order_Date"]

# df["Month Name"]=df["Order_Date"].dt.month_name()
# print(df)
# print(df.groupby("Month Name")["City"].count())

# df.to_csv("Mixed2_datetime_final.csv")

#mixed3

# import pandas as pd

# df = pd.DataFrame({
#     "Order Date": [
#         "2024-01-05","2024-01-12","2024-01-20","2024-02-03","2024-02-15",
#         "2024-02-28","2024-03-08","2024-03-19","2024-03-27","2024-04-05",
#         "2024-04-14","2024-04-25","2024-05-06","2024-05-18","2024-05-29",
#         "2024-06-07","2024-06-16","2024-06-28","2024-07-09","2024-07-21"
#     ],
#     "Delivery Date": [
#         "2024-01-08","2024-01-16","2024-01-24","2024-02-07","2024-02-19",
#         "2024-03-03","2024-03-12","2024-03-23","2024-03-31","2024-04-09",
#         "2024-04-18","2024-04-30","2024-05-10","2024-05-22","2024-06-02",
#         "2024-06-11","2024-06-20","2024-07-02","2024-07-13","2024-07-25"
#     ],
#     "Sales": [
#         2500,4200,3100,5800,2700,
#         6500,3900,4800,7200,5100,
#         4600,8300,2900,7600,5500,
#         6100,4300,8700,6900,5200
#     ],
#     "City": [
#         "Ahmedabad","Surat","Vadodara","Rajkot","Bhavnagar",
#         "Ahmedabad","Surat","Vadodara","Rajkot","Bhavnagar",
#         "Ahmedabad","Surat","Vadodara","Rajkot","Bhavnagar",
#         "Ahmedabad","Surat","Vadodara","Rajkot","Bhavnagar"
#     ]
# })

# print(df)

# print(df.groupby("City")["Sales"].mean())
# print(df.pivot_table(values="Sales",index="Order Date",columns="City"))
# print(pd.crosstab(df["City"],df["Sales"]))
# df.to_csv("Final_mixed3_datetime.csv")

#----------------------------------------------------------------

# import pandas as pd

# df = pd.DataFrame({
#     "Employee": [
#         "Rahul","Neha","Amit","Priya",
#         "Karan","Riya","Sneha","Jay",
#         "Harsh","Tirth","Manthan","Shukan"
#     ],
#     "Department": [
#         "IT","HR","IT","Sales",
#         "HR","Finance","IT","Sales",
#         "Finance","IT","IT","HR"
#     ],
#     "City": [
#         "Ahmedabad","Surat","Ahmedabad","Rajkot",
#         "Surat","Vadodara","Ahmedabad","Rajkot",
#         "Vadodara","Ahmedabad","Ahmedabad","Surat"
#     ],
#     "Gender": [
#         "M","F","M","F",
#         "M","F","F","M",
#         "M","M","M","F"
#     ],
#     "Salary":[
#         50000,60000,55000,65000,
#         62000,58000,54000,70000,
#         68000,61000,59000,60000
#     ]
# })
# #1
# print(df["Department"].value_counts())
# #2
# print(df["City"].value_counts())
# #3
# print(df["Department"].value_counts(normalize=True))
# values=df["Department"].value_counts(normalize=True)
# print(values*100)

# #4
# print(df["City"].unique())

# #5
# print(df["Department"].unique())

# #6
# print(df["City"].nunique())

# #7
# print(df["Department"].nunique())

# #8
# print(df["Gender"].value_counts())

# #9
# print(df["Department"].value_counts().sort_values())

# #10
# # import numpy as np

# # df=pd.DataFrame({
# #     "EmpID":[101,102,103,104,105],
# #     "Name":["Manthan","Khushbu","Aastha","Tirth","John"],
# #     "Department":["IT","HR",np.nan,"IT",np.nan]
# # })
# # print(df.info())
# # print(df["Department"].value_counts())
# # print(df["Department"].value_counts(dropna=False))

# #bonus1
# print(df["City"].value_counts().nlargest(1))

# #bonus2
# print(df["Department"].value_counts().nsmallest(1))

#mixed1
# data = {
#     "Product": ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"],
#     "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Wearables"],
#     "City": ["Ahmedabad", "Mumbai", "Delhi", "Ahmedabad", "Chennai"],
#     "Sales": [120000, 95000, 45000, 15000, 30000]
# }

# df = pd.DataFrame(data)

# print(df)

# print(df.groupby("Category")["Product"].count())
# print(df["Category"].value_counts())

# print(df["City"].nunique())

# print(df["Category"].value_counts(normalize=True))
# values=df["Category"].value_counts(normalize=True)
# print(values*100)

# print(df.groupby("City")["Product"].count().nlargest(1))
# print(df["City"].value_counts().nlargest(1))

#mixed2

# data = {
#     "Customer": ["Amit", "Priya", "Rohan", "Sneha", "Vikas", "Meera", "Arjun", "Neha"],
#     "PaymentMode": ["Credit Card", "UPI", "Cash", "Credit Card", "UPI", "Cash", "Credit Card", "UPI"],
#     "State": ["Gujarat", "Maharashtra", "Delhi", "Gujarat", "Maharashtra", "Delhi", "Gujarat", "Maharashtra"]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df["PaymentMode"].value_counts())
# print(df["State"].unique())
# print(df["State"].nunique())

#mixed3
# data = {
#     "Movie": ["Inception", "Dangal", "Parasite", "Interstellar", "Bahubali", "Spirited Away", "The Dark Knight", "3 Idiots"],
#     "Genre": ["Sci-Fi", "Drama", "Thriller", "Sci-Fi", "Action", "Animation", "Action", "Comedy"],
#     "Language": ["English", "Hindi", "Korean", "English", "Telugu", "Japanese", "English", "Hindi"]
# }
# df = pd.DataFrame(data)

# print(df)

# print(df.groupby("Genre")["Movie"].count())
# print(df["Genre"].value_counts())

# print(df.groupby("Language")["Movie"].count())
# print(df["Language"].value_counts())

# print(df["Genre"].unique())
# print(df["Language"].nunique())

# df.to_csv("Mixed3_final_unv.csv")

# Interview Challenge
# data = {
#     "OrderID": [101, 102, 103, 104, 105, 106,107],
#     "CustomerID": ["C001", "C002", "C003", "C004", "C005", "C006","C007"],
#     "City": ["Ahmedabad", "Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad","Mumbai"],
#     "PaymentMode": ["Credit Card", "UPI", "Cash", "Credit Card", "UPI", "Cash","UPI"],
#     "Category": ["Electronics", "Fashion", "Groceries", "Electronics", "Books", "Fashion","Books"]
# }
# df = pd.DataFrame(data)

# print(df)

# print(df["City"].value_counts())

# print(df["PaymentMode"].unique())

# print(df["Category"].nunique())

# print(df["PaymentMode"].value_counts().nlargest(1))

# print(df["City"].value_counts().nsmallest(1))

#------------------------------------------------------------------

# import pandas as pd
#
# df = pd.DataFrame({
#     "EmpID":["101","102","103","104","105"],
#     "Age":["21","25","30","28","26"],
#     "Salary":["45000","55000","62000","58000","51000"],
#     "Experience":["1","3","5","4","2"],
#     "Active":[1,0,1,1,0]
# })
# #1
# print(df.dtypes)
# #2
# #empid already in str so i converted in int
# df = df.astype({
#     "EmpID":"int",
#     "Age":"int",
#     "Salary":"float",
#     "Experience":"int",
# })
# print(df.dtypes)
# #3
#
# df["Active"]=df["Active"].astype(bool)
# print(df.dtypes)
#
# #4
# print(df.dtypes)
#
# #5
# df["Total Salary"]=df["Salary"]*df["Experience"]
# print(df)
#
# #6,7,8,9
# df=df.astype({
#     "Experience":"float",
#     "Age":"str",
#     "Salary":"int",
#     "Total Salary":"int",
#     })
# print(df.dtypes)
#
# #10
# df["Experience Level"]=df["Experience"].apply(lambda x:"Senior" if x>=4 else "Junior")
# print(df)

#bonus
#
# df=pd.DataFrame({
#     "Name":["Manthan","Tirth","Khushbu","Aastha"],
#     "Age":["21","abc","30","28"]
# })
# try:
#     df["Age"]=df["Age"].astype(int)
#     print(df)
# except Exception as e:
#     print(e)
#
# df["Age"]=pd.to_numeric(df["Age"],errors="coerce")
# print(df.dtypes)
# df["Age"]=df["Age"].fillna(df["Age"].mean())
# print(df)

#bonus
# print(df.dtypes)
# df["Experience"]=df["Experience"].astype("category")
# print(df.dtypes)

#experience fileds data type changes into the category

#mixed1

# employees = [
#     {"Name": "Alice", "Age": "25", "Salary": "50000", "Experience": "2"},
#     {"Name": "Bob", "Age": "30", "Salary": "60000", "Experience": "5"},
#     {"Name": "Charlie", "Age": "28", "Salary": "55000", "Experience": "3"},
#     {"Name": "Diana", "Age": "35", "Salary": "75000", "Experience": "2"},
#     {"Name": "Ethan", "Age": "40", "Salary": "90000", "Experience": "5"}
# ]
# df=pd.DataFrame(employees)
# print(df.dtypes)
#
# df=df.astype({
#     "Age":"int",
#     "Salary":"float",
#     "Experience":"float",
# })
#
# print(df.dtypes)
#
# df["Total Salary"]=df["Salary"]*df["Experience"]
# print(df)
#
# print(df["Experience"].value_counts())
#
# df.to_csv("mixed1_final_astype.csv")

#mixed2

# orders = [
#     {"OrderID": "ORD001", "Quantity": "2", "Price": "1500", "OrderDate": "2026-07-01"},
#     {"OrderID": "ORD002", "Quantity": "1", "Price": "2500", "OrderDate": "2026-07-02"},
#     {"OrderID": "ORD003", "Quantity": "5", "Price": "500", "OrderDate": "2026-07-03"},
#     {"OrderID": "ORD004", "Quantity": "3", "Price": "1200", "OrderDate": "2026-07-04"},
#     {"OrderID": "ORD005", "Quantity": "4", "Price": "800", "OrderDate": "2026-07-05"}
# ]
# df=pd.DataFrame(orders)
# print(df.dtypes)
#
# df=df.astype({
#     "Quantity": "int",
#     "Price": "float",
# })
# df["OrderDate"]=pd.to_datetime(df["OrderDate"])
# df["Total Amount"]=df["Quantity"]*df["Price"]
# df["Month Name"]=df["OrderDate"].dt.month_name()
# print(df["Month Name"].value_counts())
# print(df.dtypes)
# df.to_csv("mixed2_final_astype.csv")

#mixed3
# customers = [
#     {"CustomerID": "CUST001", "Age": "25", "State": "Gujarat", "PurchaseAmount": "1500", "Active": 1},
#     {"CustomerID": "CUST002", "Age": "32", "State": "Maharashtra", "PurchaseAmount": "2500", "Active": 0},
#     {"CustomerID": "CUST003", "Age": "28", "State": "Delhi", "PurchaseAmount": "1800", "Active": 1},
#     {"CustomerID": "CUST004", "Age": "40", "State": "Karnataka", "PurchaseAmount": "3200", "Active": 1},
#     {"CustomerID": "CUST005", "Age": "35", "State": "Tamil Nadu", "PurchaseAmount": "2100", "Active": 0}
# ]
# df=pd.DataFrame(customers)
# print(df.dtypes)
#
# df=df.astype({
#     "Age":"int",
#     "PurchaseAmount":"float",
#     "Active":"bool"
# })
# print(df.dtypes)
# print(df)
# print(df["State"].value_counts())
# print(df.groupby("State")["PurchaseAmount"].mean())
# df.to_csv("mixed3_final_astype.csv")

# # Interview Challenge
# import pandas as pd
# data = [
#     {"Product": "Laptop", "Quantity": "2", "Price": "55000", "OrderDate": "2025-01-05"},
#     {"Product": "Mouse", "Quantity": "5", "Price": "700", "OrderDate": "2025-01-10"},
#     {"Product": "Keyboard", "Quantity": "3", "Price": "1500", "OrderDate": "2025-01-15"}
# ]
# df = pd.DataFrame(data)
# print(df.dtypes)
# df=df.astype({
#     "Quantity": "int",
#     "Price": "float",
# })
# df["OrderDate"]=pd.to_datetime(df["OrderDate"])
# print(df.dtypes)
# df["Total Amount"]=df["Quantity"]*df["Price"]
# highest_product = df.groupby("Product")["Total Amount"].sum().idxmax()
# highest_amount = df.groupby("Product")["Total Amount"].sum().max()
#
# print(f"Product with highest total sales: {highest_product} ({highest_amount})")
#
# df.to_csv("Astype_in_questions.csv")

#----------------------------------------------------------------

# import pandas as pd
#
# df = pd.DataFrame({
#     "Emp_ID": [101,102,103,104,105],
#     "Emp_Name": ["Rahul","Neha","Amit","Priya","Manthan"],
#     "Dept": ["IT","HR","IT","Sales","Finance"],
#     "Sal": [50000,60000,55000,70000,65000],
#     "Loc": ["Ahmedabad","Surat","Ahmedabad","Rajkot","Vadodara"]
# })
#
# #1
# print(df.columns)
#
# #2
# df=df.rename(columns={"Emp_ID":"EmployeeID"})
# print(df.columns)
#
# #3
# df=df.rename(columns={"Emp_Name":"EmployeeName"})
# print(df.columns)
#
# #4
# df=df.rename(columns={
# "Dept":"Department",
# "Sal":"Salary",
# "Loc":"City"
# })
#
# #5
# print(df.columns)
#
# #6
# df=df.rename(index={
#     0 :"Employee_1",
#     1 :"Employee_2",
#     2 :"Employee_3",
#     3 :"Employee_4",
#     4 :"Employee_5",
# })
# print(df.index)
#
# #7
# df.columns=df.columns.str.lower()
# print(df.columns)
#
# #8
#
# df = pd.DataFrame({
#     "Emp_ID": [101,102,103,104,105],
#     "Emp_Name": ["Rahul","Neha","Amit","Priya","Manthan"],
#     "Dept": ["IT","HR","IT","Sales","Finance"],
#     "Sal": [50000,60000,55000,70000,65000],
#     "Loc": ["Ahmedabad","Surat","Ahmedabad","Rajkot","Vadodara"]
# })
# df.columns=[
#     "Employee ID",
#     "Employee Name",
#     "Department",
#     "Salary",
#     "City"
# ]
# df.columns=df.columns.str.replace(" ","_")
# print(df.columns)
#
# #9
#
# df.columns=[
#     "Employee ID",
#     "Employee Name",
#     "Department",
#     "Salary",
#     "City"
# ]
# print(df.columns)
#
# #10
# print(df[df["Salary"]>55000])

#bonus1

# df = pd.DataFrame({
#     " Employee Name ": ["Rahul","Neha"],
#     " Monthly Salary ": [50000,60000],
#     " Department ": ["IT","HR"]
# })
# print(df)
# df.columns=[
#     df.columns.str.strip().str.replace(" ","_")
# ]
# print(df)
#
# #bonus2
# df=df.rename(columns={
#     "Monthly_Salary":"Salary"
# })
# print(df.columns)
# print(df)
# df["Bonus"]=df["Salary"]*10/100
# print(df)
# df["Net_Salary"] = df.apply(lambda row: row["Salary"] + row["Bonus"], axis=1)
# # df["Net_Salary"]=df["Bonus"]+df["Salary"] this is not working why? give me value error
# print(df)

#mixed 1

# import pandas as pd
# data = {
#     " Emp ID ":[101,102,103,104],
#     " Employee Name ": [" Alice Smith ", "bob johnson", "charlie BROWN", "DIANA prince"],
#     "  Salary  ": ["$85,000", "90000",None, "$120,000"],
#     " Department": [" HR ", "IT",None, "Finance "]
# }
# df = pd.DataFrame(data)
# print(df)
#
# df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
#
# print(df.dtypes)
#
# df["salary"]=df["salary"].str.replace("$","").str.replace(",","")
#
# df["employee_name"]=df["employee_name"].str.strip().str.title()
# df["department"]=df["department"].str.strip()
# print(df)
#
# df["salary"]=df["salary"].astype(float)
# print(df.dtypes)
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["department"]=df["department"].fillna("Unknows")
# df["bonus"]=df["salary"]*10/100
# df["net_salary"]=df["salary"]+df["bonus"]
# print(df)
# print(df.groupby("department")["emp_id"].count())
# print(df.groupby("department")["salary"].mean())
# print(df["salary"].mean())
# df.to_csv("Mixed1_final.columnsrename.csv")

# #mixed2
# import pandas as pd
#
# employee_data = {
#     'EmpID': [101, 102, 103, 104],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'DeptID': [1, 2, 1, 3]
# }
# df_employee = pd.DataFrame(employee_data)
#
# department_data = {
#     'DeptID': [1, 2, 3],
#     'DeptName': ['HR', 'Engineering', 'Marketing']
# }
# df_department = pd.DataFrame(department_data)
#
# df=pd.merge(df_employee, df_department, on='DeptID')
# print(df)
#
# df=df.rename(columns=
#              {"Name":"EmployeeName",
#               "DeptName":"Department",
#               })
# print(df.columns)
# print(df)
# print(df["Department"].value_counts())
# df.to_csv("Mixed2_final.columnsrename.csv")

#mixed3
# import pandas as pd
#
# df = pd.DataFrame({
#     " Order ID ": [101, 102, 103, 104, 105, 106, 107, 108],
#     " Customer Name ": [
#         " Alice ", "BOB", "charlie", " David",
#         "emma ", " Frank ", "GRACE", " henry "
#     ],
#     " Product Category ": [
#         " Electronics ", "Furniture", " clothing ",
#         "ELECTRONICS", " Furniture ", "CLOTHING",
#         " electronics", "FURNITURE "
#     ],
#     " Sales Amount ": [
#         "1200", "850", "450", "2100",
#         "1350", "700", "980", "1600"
#     ],
#     " Order Date ": [
#         "15-01-2024",
#         "22/01/2024",
#         "Feb 05, 2024",
#         "2024/02/18",
#         "10-Mar-2024",
#         "25 March 2024",
#         "08-04-2024",
#         "April 19, 2024"
#     ]
# })
#
# print(df)
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
#
# print(df)
# df["customer_name"]=df["customer_name"].str.strip().str.title()
#
# df["product_category"]=df["product_category"].str.strip().str.title()
# import pandas as pd
#
# df["order_date"] = pd.to_datetime(df["order_date"], format="mixed")
#
# df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")
#
# df["order_date"] = pd.to_datetime(df["order_date"])
# print(df.dtypes)
#
# print(df)
# df["sales_amount"]=df["sales_amount"].astype(int)
# df=df.rename(columns={
#     "sales_amount":"sales"
# })


# df["month_name"]=df["order_date"].dt.month_name()
# print(df)
#
# print(df.groupby("month_name")["sales"].sum())
# print(df.groupby("product_category")["sales"].sum())
# print(df.sort_values("sales",ascending=False))
# df.to_csv("Mixed3_final.columnsrename.csv")

# Interview Challenge

# import pandas as pd
#
# df = pd.DataFrame({
#     " Employee ID ": [101,102,103,104],
#     " Customer Name ": ["Rahul","Neha","Amit","Priya"],
#     " Total Purchase ": [5000,8000,3500,12000],
#     " Customer City ": ["Ahmedabad","Surat","Ahmedabad","Rajkot"]
# })
# print(df.columns)
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.columns)
# df=df.rename(columns={
#     "customer_name":"name",
#      "total_purchase":"purchase"
# })
# print(df.columns)
#
# print(df[df["purchase"]>5000])
# print(df.groupby("customer_city")["purchase"].sum())
# print(df.groupby("customer_city")["purchase"].sum().nlargest(1))
# print(df.sort_values(["name","purchase"], ascending=False))
# df.to_csv("customer_clean_report.csv")

#Mentor Challenge

# try:
#     df=pd.read_csv("Mentor_Challenge_rename.csv")
# except Exception as e:
#     print(e)
#
# print(df.info())
# print(df.describe())
# print(df.head())
# print(df.tail())
# print(df.dtypes)
# print(df.columns)
#
# df.columns=df.columns.str.strip().str.lower().str.replace(' ', '_')
# print(df.columns)
#
# df=df.rename(columns={
#     "employee_id":"emp_id",
#     "employee_name":"name",
#     "department_name":"department",
#     "monthly_salary":"salary"
# })
# print(df.columns)
#
# df["salary"]=df["salary"].fillna(df["salary"].median())
# print(df)
#
# df["joining_date"]=pd.to_datetime(df["joining_date"],format="mixed")
#
# print(df.dtypes)
# df["joining_year"]=df["joining_date"].dt.year
# df["bonus"]=df["salary"]*10/100
# df["final_salary"]=df["salary"]+df["bonus"]
# print(df)
# print(df.groupby("department")["salary"].mean())
# print(df.sort_values("salary",ascending=False).head(1))
# print(df.pivot_table(index="joining_date",columns="department",values="salary",aggfunc="mean"))
# print(df.pivot_table(index="department",columns="joining_date",values="salary",aggfunc="mean"))
# df.to_csv("Clean_Mentor_Challenge_rename.csv")


#-----------------------------------------------------------------

# import pandas as pd

# df = pd.DataFrame({
#     "EmpID":[105,101,104,102,103,106],
#     "Name":["Manthan","Rahul","Priya","Neha","Amit","Karan"],
#     "Department":["IT","IT","Sales","HR","IT","HR"],
#     "City":["Ahmedabad","Ahmedabad","Rajkot","Surat","Surat","Ahmedabad"],
#     "Salary":[65000,50000,70000,60000,55000,62000]
# })
#1
# print(df)
# #2
# df=df.set_index("EmpID")
# print(df)
# #3
# print(df.loc[103])
# #4
# print(df.loc[105])
# #5
# df=df.sort_index()
# print(df)
# #6
# df=df.sort_index(ascending=False)
# print(df)
# #7
# df=df.reset_index()
# print(df)
# #8
# df=df[df["Salary"]>55000]
# print(df)
# df=df.reset_index(drop=True)
# print(df)
#9
# df=df.set_index(["Department","City"])
# print(df)
# #10
# print(df.loc["IT"])

#Bonus Question 1

# df = pd.DataFrame({
#     "OrderID":["O103","O101","O105","O102","O104"],
#     "Customer":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Sales":[5000,8000,3000,12000,7000]
# })
# print(df)
# df=df.set_index("OrderID")
# print(df)
# print(df.loc["O104"])
# df=df.sort_index()
# print(df)
# print(df.sort_values("Sales",ascending=False).head(1))
# df=df.reset_index()
# print(df)
# df.to_csv("sort_index_bonus1.csv")

#Bonus Question 2

# df = pd.DataFrame({
#     "EmpID":[101,102,102,103],
#     "Name":["Rahul","Neha","Amit","Priya"],
#     "Salary":[50000,60000,55000,70000]
# })
# print(df)
# df=df.set_index("EmpID")
# print(df)
# df=df.set_index("EmpID",verify_integrity=True) #because error this is have duplicate EmpID
# print(df)

#MIXED1

# try:
#     df=pd.read_csv("employee.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# print(df.columns)
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.columns)
# df["employee_name"]=df["employee_name"].str.strip().str.title()
# print(df)
# df["age"]=df["age"].fillna(df["age"].mean())
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["city"]=df["city"].fillna("Unknown")
# print(df)
# print(df.dtypes)
# df=df.astype({
#     "age":"int"
# })
# print(df.dtypes)
# df=df.set_index("employee_id")
# print(df)
# print(df.loc[102])
# print(df.loc[109])
# df=df.reset_index()
# print(df)
# print(df.groupby("department")["salary"].mean())
# df=df.sort_values("employee_name",ascending=False)
# print(df)
# df.to_csv("mixed1_sortindex.csv")

#mixed2

# import pandas as pd

# employees = pd.DataFrame({
#     "EmpID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Neha", "Rohan", "Priya", "Karan", "Sneha"],
#     "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance"],
#     "Experience": [2, 5, 3, 7, 1, 4]
# })

# salary = pd.DataFrame({
#     "EmpID": [101, 102, 103, 104, 106, 107],
#     "Salary": [40000, 65000, None, 80000, 55000, 50000]
# })

# print(employees.info())
# print(salary.info())

# df=pd.merge(employees,salary,on="EmpID",how="inner")
# print(df)

# print(df.info())
# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)
# df=df.set_index("EmpID")
# print(df)
# print(df.loc[106])
# print(df.loc[102])
# df=df.sort_index()
# print(df)
# df=df.reset_index()
# print(df)

# df["Salary Category"]=df["Salary"].apply(lambda x:"High" if x>=65000 else "Normal")
# print(df)
# print(df.groupby("Department")["Salary"].sum())
# df["Bonus"]=df["Salary"]*10/100
# df["Final Salary"]=df["Salary"]+df["Bonus"]
# print(df)
# df.to_csv("mixed2_sortindex.csv")

#mixed3

# import pandas as pd

# data = {
#     "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015],
#     "Customer": ["Alice","Bob","Charlie","David","Emma","Frank","Grace","Henry","Ivy","Jack","Alice","Bob","Charlie","David","Emma"],
#     "City": ["New York","Chicago","New York","Houston","Chicago","Houston","New York","Miami","Miami","Chicago","Houston","New York","Miami","Chicago","Houston"],
#     "Category": ["Electronics","Furniture","Clothing","Electronics","Clothing","Furniture","Electronics","Clothing","Furniture","Electronics","Clothing","Furniture","Electronics","Clothing","Furniture"],
#     "OrderDate": ["2024-01-05","2024-01-06","2024-01-08","2024-01-10","2024-01-12","2024-01-15","2024-01-18","2024-01-20","2024-01-22","2024-01-25","2024-01-28","2024-02-01","2024-02-03","2024-02-05","2024-02-08"],
#     "Sales": [1200,850,320,1500,450,980,760,290,1150,1340,410,920,1680,530,1020]
# }

# df = pd.DataFrame(data)

# print(df)

# df["OrderDate"]=pd.to_datetime(df["OrderDate"])
# print(df.dtypes)

# df=df.set_index("OrderID")
# print(df)

# print(df.loc[1005])
# print(df.loc[1007])

# print(df.value_counts("City"))
# print(df["City"].nunique())
# print(df.groupby("City")["Sales"].sum())
# print(df.pivot_table(index="City",columns="Category",values="Sales"))
# print(pd.crosstab(index=df["Category"],columns=df["City"]))
# df=df.reset_index()
# print(df)
# df.to_csv("mixed3_sortindex.csv")


# Interview Challenge

# df = pd.DataFrame({
#     "CustomerID":["C105","C101","C104","C102","C103"],
#     "Customer":["Manthan","Rahul","Priya","Neha","Amit"],
#     "City":["Ahmedabad","Ahmedabad","Rajkot","Surat","Ahmedabad"],
#     "Purchase":[7500,5000,12000,8500,4000]
# })

# df=df.set_index("CustomerID")
# print(df)
# print(df.loc["C104"])
# print(df[df["Purchase"]>6000])
# df=df.sort_index()
# print(df)
# location_i=df["Purchase"].idxmax()
# print("location_i",df.loc[location_i])
# df=df.reset_index()
# print(df)
# total_purchase_bycity=df.groupby("City")["Purchase"].sum()
# print(total_purchase_bycity)
# print(total_purchase_bycity.nlargest(1))
# df.to_csv("customer_index_report.csv")

#mentor
#
# try:
#     df=pd.read_csv("employee_index_data.csv")
# except:
#     print("File not found")
#
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.dtypes)
# print(df.isna().sum())
#
# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# print(df)
#
# df.columns=df.columns.str.strip().str.lower()
# print(df.columns)
# df["employeename"]=df["employeename"].str.strip().str.title()
# print(df)
#
# df["joiningdate"]=pd.to_datetime(df["joiningdate"])
# print(df.dtypes)
# df["joiningyear"]=df["joiningdate"].dt.year
# print(df)
# df=df.set_index("employeeid")
# print(df)
# print(df.loc[105])
# print(df.loc[107])
# print(df.sort_values("employeename"))
# print(df.sort_values("salary",ascending=False ).head())
# print(df.groupby("department")["salary"].mean())
# print(df.pivot_table(index="department",columns="joiningyear",values="salary",fill_value=0))
# df=df.reset_index()
# print(df)
# df.to_csv("employee_index_final_report.csv")




