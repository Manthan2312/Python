import pandas as pd

try:
    emp=pd.read_csv("employeess.csv")
    attendance=pd.read_csv("attendance.csv")
    customers=pd.read_csv("customers.csv")
    products=pd.read_csv("products.csv")
    sales=pd.read_csv("sales.csv")
    price_history=pd.read_csv("price_history.csv")
except Exception as e:
 print(e)

print(emp.info())
print(attendance.info())
print(customers.info())
print(products.info())
print(sales.info())
print(price_history.info())