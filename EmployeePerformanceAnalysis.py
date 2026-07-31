from sys import exception
import pandas as pd

# Add these lines before printing your DataFrame
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

import numpy as np

# employees = pd.DataFrame({
#     "EmpID":[101,102,103,104,105,106,107,108,109,110],
#     "Name":["Rahul","Neha","Amit","Priya","Manthan","Karan","Riya","Sneha","Vikas","Aastha"],
#     "Department":["IT","HR","IT","Sales","Finance","IT","HR","Sales","Finance","IT"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Rajkot","Vadodara",
#             "Ahmedabad","Surat","Rajkot","Vadodara","Ahmedabad"],
#     "Age":[24,28,np.nan,30,26,29,31,np.nan,27,25]
# })
#
# employees.to_csv("employees.csv",index=False)
#
# salary = pd.DataFrame({
#     "EmpID":[101,102,103,104,105,106,107,108,109,110],
#     "Salary":[50000,65000,np.nan,72000,58000,61000,55000,np.nan,70000,62000]
# })
#
# salary.to_csv("salary.csv",index=False)
#
# performance = pd.DataFrame({
#     "EmpID":[101,102,103,104,105,106,107,108,109,110],
#     "Performance":[5,4,3,5,2,4,3,5,4,5]
# })
#
# performance.to_csv("performance.csv",index=False)


try:
    employees=pd.read_csv('employees.csv')
    salary=pd.read_csv('salary.csv')
    performance=pd.read_csv('performance.csv')
except exception as e:
    print(e)


print(employees.head())
print(salary.head())
print(performance.head())


print(performance.info())

print(employees.describe())
print(salary.describe())
print(performance.describe())

employees["Age"]=employees["Age"].fillna(employees["Age"].mean())
salary["Salary"]=salary["Salary"].fillna(salary["Salary"].median())

print(employees)
print(salary)


print(employees.info())
print(salary.info())


df_1=pd.merge(employees,salary,on='EmpID')
df=pd.merge(df_1,performance,on='EmpID')

df["Bonus"]=df["Salary"].apply(lambda x:x*10/100)

# print(df)

df["Tax"]=df["Salary"].apply(lambda x:x*5/100)

df["Net Salary"]=df["Salary"]+df["Bonus"]-df["Tax"]




df["Performance Grade"] = df["Performance"].apply(
    lambda x: "Excellent" if x == 5 else
              "Very Good" if x == 4 else
              "Good" if x == 3 else
              "Average" if x == 2 else "Poor"
)
# print(df)
# grade_mapping = {
#     5: "Excellent",
#     4: "Very Good",
#     3: "Good",
#     2: "Average",
#     1: "Poor"
# }
#
# df["Performance Grade"] = df["Performance"].map(grade_mapping)

df["Salary Category"]=df["Salary"].apply(lambda x:"High Salary" if x>=65000 else "Normal")
print(df)


department_wise_av_salary=df.groupby("Department")["Salary"].mean()
print(department_wise_av_salary)

department_wise_h_salary=df.groupby("Department")["Salary"].max()
print(department_wise_h_salary)

print(df.groupby("Department")["Salary"].max().tail(1))

department_wise_e_count=df.groupby("Department")["EmpID"].count()
print(department_wise_e_count)


city_wise_av_salary=df.groupby("City")["Salary"].mean()
print(city_wise_av_salary)

city_wise_h_salary=df.groupby("City")["Salary"].max()
print(city_wise_h_salary)

print(df.groupby("City")["Salary"].max().tail(1))


print(df.loc[df["Salary"].idxmax()])

print(df.loc[df["Salary"].idxmin()])

print(df["Salary"].mean())
print(df["Salary"].median())

print(df[df["Salary"]>60000])
print(df[df["Performance"]>=4])
print(df[df["City"]=="Ahmedabad"])
print(df
      [
          (df["Salary"]>60000)
            &
          (df["Performance"]>=4)
      ]
      )

salary_desc=df["Salary"].sort_values(ascending=False)#show only salary descending
print(salary_desc)
print(df.sort_values("Salary",ascending=False)) #show full rows with deatils descending
print(salary_desc.head(5))
print(salary_desc.tail(3))

# try:
#     df.to_csv('employee_final_report.csv')
#     print("Employee Final Report")
# except Exception as e:
#     print(e)

# Bonus 1
df["Experience Bonus"]=df["Age"].apply(lambda x:2000 if x<26 else 5000)

# Bonus 2
df["Final Salary"]=df["Net Salary"]+df["Experience Bonus"]
print(df)

# Bonus 3
print(df.groupby("Department")["Salary"].agg(["mean","median","std","max","min","count"]))

# Bonus 4
print(department_wise_h_salary.head(1))

# Bonus 5
print(df[["Final Salary", "Name"]].nlargest(3, "Final Salary"))

try:
    df.to_csv('employee_final_report.csv')
    print("Employee Final Report")
except Exception as e:
    print(e)