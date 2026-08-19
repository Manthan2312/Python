import pandas as pd
import numpy as np

try:
    customer=pd.read_csv("p1_customers.csv")
    orders=pd.read_csv("p1_orders.csv")
    emp=pd.read_csv("p1_employee.csv")
except Exception as e:
    print(e)

# print(customer.info())
# print(customer.head())
# print(customer.tail())
# print(customer.dtypes)
# print(customer.columns)
# print(customer.shape)
# print(customer.isna().sum())
# print(customer.duplicated().sum())

# print(orders.info())
# print(orders.head())
# print(orders.tail(10))
# print(orders.dtypes)
# print(orders.columns)
# print(orders.shape)
# print(orders.isna().sum())
# print(orders.duplicated().sum())

# print(emp.info())
# print(emp.head())
# print(emp.tail())
# print(emp.dtypes)
# print(emp.columns)
# print(emp.shape)
# print(emp.isna().sum())
# print(emp.duplicated().sum())


customer["name"]=customer["name"].fillna("Unknown").str.strip().str.title()
customer["age"]=customer["age"].where((customer["age"]>5)&(customer["age"]<=100))
customer["age"]=customer["age"].fillna(customer["age"].mean()).astype(int)
customer["email"]=customer["email"].fillna("Unknown")
customer["signup_date"]=pd.to_datetime(customer["signup_date"],format="mixed")
customer["signup_date"]=customer["signup_date"].fillna(customer["signup_date"].mean())
customer=customer.drop_duplicates()
customer["gender"]=customer["gender"].replace({
    "M":"Male",
    "F":"Female"
})
customer["city"]=customer["city"].str.strip().str.title()


orders["quantity"]=pd.to_numeric(orders["quantity"],errors="coerce")
orders["quantity"]=orders["quantity"].fillna(orders["quantity"].mean()).astype("int")
orders["price"]=orders["price"].where((orders["price"]>=15)&(orders["price"]<=62000))
orders["price"]=orders["price"].fillna(orders["price"].mean())
orders["order_date"]=pd.to_datetime(orders["order_date"],format="mixed")
orders["payment_method"]=orders["payment_method"].str.strip().str.title()
orders["status"]=orders["status"].str.strip().str.title()

emp["name"]=emp["name"].fillna("Unknown")
emp["age"]=emp["age"].fillna(emp["age"].mean()).astype("int")
emp["salary"]=emp["salary"].fillna(emp["salary"].median())
emp["joining_date"]=pd.to_datetime(emp["joining_date"],errors="coerce")
emp["performance_score"]=emp["performance_score"].fillna(emp["performance_score"].mean())
emp=emp.drop_duplicates()
emp["gender"]=emp["gender"].replace({
    "M":"Male",
    "F":"Female"
})
print(customer.query("city=='Ahmedabad'"))
print(emp.query("department=='IT'"))
print(orders.query("quantity>5"))
print(orders.query("status=='Cancelled'"))
print(emp.query("salary>70000"))
print(customer.query("age>30"))
print(customer[["name","city","email"]])
print(orders[["product","quantity","price"]])

orders["total_amount"]=orders["quantity"]*orders["price"]
print(orders)
print(orders["total_amount"].sum())
print(orders["total_amount"].mean())
print(orders["total_amount"].max())
print(orders["total_amount"].min())
print(orders.groupby("product")["price"].mean())
print(orders.query("status=='Delivered'").groupby("status")["quantity"].sum())
print(emp["salary"].mean())
print(emp.nlargest(1,"salary"))
print(emp.nsmallest(1,"salary"))
average_performance_score=emp["performance_score"].mean()
print(average_performance_score)
print(emp[emp["performance_score"]>average_performance_score])

print(orders.groupby("product")["total_amount"].sum())
print(orders.groupby("category")["total_amount"].sum())
print(orders.groupby("product")["quantity"].sum())
print(orders.groupby("product")["price"].mean())
print(orders["payment_method"].value_counts())
print(orders["status"].value_counts())
df=pd.merge(orders,customer,on="customer_id",how="inner")
print(df.columns)
print(df.groupby("customer_id")["total_amount"].sum())
print(df.groupby("customer_id")["total_amount"].sum().nlargest(5))
orders["month_name"]=orders["order_date"].dt.month_name()
print(orders.groupby("month_name")["total_amount"].sum())
print(customer.groupby("city")["customer_id"].count())
print(customer.groupby("city")["age"].count())
print(emp.groupby("department")["salary"].mean())
emp["department_rank_salary"]=emp.groupby("department")["salary"].rank(ascending=False,method="dense")
print(emp.query("department_rank_salary==1"))
print(emp.groupby("department")["performance_score"].mean())
print(emp["department"].value_counts())

print(df.groupby("customer_id")["total_amount"].sum())
print(df["order_id"].isna().sum()) #so showing zero means not any customer is like never placed an order.
df_duplicates = df[df.duplicated(subset=["customer_id"], keep=False)]
print(df_duplicates.sort_values("customer_id"))
print(df.groupby("customer_id")["total_amount"].sum().nlargest(10))
print(df.groupby("city")["total_amount"].sum())
print(df.groupby(["city","product"])["total_amount"].sum())
product_counts = df.groupby(["city", "product"]).size().reset_index(name="count")
most_popular_per_city = product_counts.loc[product_counts.groupby("city")["count"].idxmax()]
print(most_popular_per_city)
city_revenue = df.groupby("city")["total_amount"].sum()
top_revenue_city = city_revenue.idxmax()
highest_revenue_value = city_revenue.max()

print(f"Top City: {top_revenue_city} with a revenue of {highest_revenue_value}")
