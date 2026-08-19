# import pandas as pd
# import numpy as np

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# # employees = pd.DataFrame({
# #     "EmpID":[101,102,103,104,105,106,107,108,109,110,
# #              111,112,113,114,115],

# #     "Name":[
# #         "Rahul","Neha","Amit","Priya","Manthan",
# #         "Karan","Riya","Sneha","Vikas","Aastha",
# #         "Jay","Khushbu","Tirth","Shukan","Harsh"
# #     ],

# #     "Department":[
# #         "IT","HR","Sales","Finance","IT",
# #         "HR","Marketing","Sales","Finance","IT",
# #         "Marketing","HR","IT","Sales","Finance"
# #     ],

# #     "City":[
# #         "Ahmedabad","Surat","Rajkot","Vadodara","Ahmedabad",
# #         "Surat","Ahmedabad","Rajkot","Vadodara","Ahmedabad",
# #         "Surat","Ahmedabad","Rajkot","Vadodara","Ahmedabad"
# #     ],

# #     "Age":[
# #         24,np.nan,28,31,25,
# #         30,np.nan,29,26,27,
# #         32,24,29,np.nan,35
# #     ]
# # })

# # employees.to_csv("employees.csv",index=False)

# # salary = pd.DataFrame({

# #     "EmpID":[
# #         101,102,103,104,105,
# #         106,107,108,109,110,
# #         111,112,113,114,115
# #     ],

# #     "Salary":[
# #         50000,
# #         62000,
# #         np.nan,
# #         75000,
# #         58000,
# #         61000,
# #         47000,
# #         np.nan,
# #         72000,
# #         66000,
# #         52000,
# #         69000,
# #         64000,
# #         71000,
# #         np.nan
# #     ]
# # })

# # salary.to_csv("salary.csv",index=False)

# # performance = pd.DataFrame({

# #     "EmpID":[
# #         101,102,103,104,105,
# #         106,107,108,109,110,
# #         111,112,113,114,115
# #     ],

# #     "Performance":[
# #         5,4,3,5,2,
# #         4,3,5,4,5,
# #         2,3,4,5,4
# #     ]
# # })

# # performance.to_csv("performance.csv",index=False)

# # jan = pd.DataFrame({

# #     "Month":["January"]*5,

# #     "Sales":[
# #         55000,
# #         62000,
# #         71000,
# #         np.nan,
# #         69000
# #     ]
# # })

# # feb = pd.DataFrame({

# #     "Month":["February"]*5,

# #     "Sales":[
# #         60000,
# #         58000,
# #         np.nan,
# #         72000,
# #         68000
# #     ]
# # })

# # mar = pd.DataFrame({

# #     "Month":["March"]*5,

# #     "Sales":[
# #         65000,
# #         70000,
# #         75000,
# #         68000,
# #         np.nan
# #     ]
# # })

# # jan.to_csv("jan.csv",index=False)
# # feb.to_csv("feb.csv",index=False)
# # mar.to_csv("mar.csv",index=False)



# try:
#     employees=pd.read_csv("employees.csv")
#     salary=pd.read_csv("salary.csv")
#     performance=pd.read_csv("performance.csv")
#     jan=pd.read_csv("jan.csv")
#     feb=pd.read_csv("feb.csv")
#     mar=pd.read_csv("mar.csv")
 
# except :
#     print("Error")

# # print(employees.head())
# # print(employees.tail())
# # print(employees.info())
# # print(employees.describe())

# # print(salary.head())
# # print(salary.tail())
# # print(salary.info())
# # print(salary.describe())

# # print(performance.head())
# # print(performance.tail())
# # print(performance.info())
# # print(performance.describe())

# # print(jan.head())
# # print(jan.tail())
# # print(jan.info())
# # print(jan.describe())

# # print(feb.head())
# # print(feb.tail())
# # print(feb.info())
# # print(feb.describe())

# # print(mar.head())
# # print(mar.tail())
# # print(mar.info())
# # print(mar.describe())

# # print(employees.shape)
# # print(employees.size)
# # print(employees.columns)
# # print(employees.index)
# # print(employees.dtypes)

# # print(salary.shape)
# # print(salary.size)
# # print(salary.columns)
# # print(salary.index)
# # print(salary.dtypes)

# # print(performance.shape)
# # print(performance.size)
# # print(performance.columns)
# # print(performance.index)
# # print(performance.dtypes)

# # print(jan.shape)
# # print(jan.size)
# # print(jan.columns)
# # print(jan.index)
# # print(jan.dtypes)

# # print(feb.shape)
# # print(feb.size)
# # print(feb.columns)
# # print(feb.index)
# # print(feb.dtypes)

# # print(mar.shape)
# # print(mar.size)
# # print(mar.columns)
# # print(mar.index)
# # print(mar.dtypes)


# employees["Age"]=employees["Age"].fillna(employees["Age"].mean())
# # print(employees)

# salary["Salary"]=salary["Salary"].fillna(salary["Salary"].median())
# # print(salary)

# jan["Sales"]=jan["Sales"].fillna(jan["Sales"].mean())
# # print(jan)

# feb["Sales"]=feb["Sales"].fillna(feb["Sales"].mean())
# # print(feb)

# mar["Sales"]=mar["Sales"].fillna(mar["Sales"].mean())
# # print(mar)

# df=pd.merge(employees,salary,on="EmpID")
# df=pd.merge(df,performance,on="EmpID")

# df["Bonus"]=df["Salary"]*10/100

# df["Tax"]=df["Salary"]*5/100

# df["Net Salary"]=df["Salary"]+df["Bonus"]-df["Tax"]

# Performance_Grade={
#     5: "Excellent",
#     4: "Very Good",
#     3: "Good",
#     2: "Average",
#     1: "Poor"
# }
# df["Performance Grade"]=df["Performance"].map(Performance_Grade)

# df["Salary Category"]=df["Salary"].apply(lambda x:"High" if x>60000 else "Normal")

# df["Experience Bonus"]=df["Age"].apply(lambda x:2000 if x<26 else 5000)

# df["Final Salary"]=df["Net Salary"]+df["Experience Bonus"]
# print(df)

# print(df[df["Salary"]>60000])

# print(df[df["Age"]>28])

# print(df[df["Performance"]>=4])

# print(df[df["Department"]=="IT"])

# print(df[df["Department"]=="HR"])

# print(
#     df[
#         (df["Salary"]>60000)
#         &
#         (df["Performance"]>=4)
#     ]
# )


# filtered_df = df[df["Department"].isin(["IT", "HR"])]
# print(filtered_df)

# filtered_df = df[df["Salary"].between(60000, 70000)]
# print(filtered_df)

# print(df.sort_values("Salary",ascending=False).head(5))
# print(df.sort_values("Salary").head(2))

# print(df.sort_values("Name"))
# print(df.sort_values("Name",ascending=False))

# print(df.sort_values(["Department","Salary"]))
# print(df.sort_values(["Department","Salary"],ascending=False))


# print(df.groupby("Department")["Salary"].agg(["mean","max","min","median","std","count"]))

# print(df.groupby("City")["Salary"].mean())

# print(df.groupby("Performance")["Salary"].mean())

# print(df.groupby(["Department","City"])["Salary"].mean())

# df_sales=pd.concat([jan,feb,mar],ignore_index=True)
# print(df_sales.info())

# print(df_sales["Sales"].sum())
# print(df_sales["Sales"].mean())
# print(df_sales["Sales"].nlargest(1))
# print(df_sales["Sales"].nsmallest(1))
# print(df_sales["Sales"].nlargest(5))

# # Part 10
# # df.to_csv("Final.csv")

# # df_final=pd.read_csv("Final.csv")

# # print(df_final)

# # print(df_final[df_final.duplicated()])
# # print(df_final.drop_duplicates(keep="first"))
# # print(df_final.drop_duplicates(keep="last"))
# # print(df_final.drop_duplicates(keep=False))

# print(df.loc[df["EmpID"]==105])
# print(df.loc[3:8])
# print(df.loc[3:8, ["Name", "Salary"]])

# try:
#     df.to_csv("employee_final_report.csv")
#     df_sales.to_csv("sales_report.csv")
# except Exception as e:
#     print(e)


#-------------------------------------------------------------
# import pandas as pd

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# try:
#     employees=pd.read_csv("employees.csv")
#     salary=pd.read_csv("salary.csv")
#     performance=pd.read_csv("performance.csv")
# except Exception as e:
#     print(e)

# print(employees.info())
# print(salary.info())
# print(performance.info())

# df=pd.merge(employees,salary,on="EmpID")
# df=pd.merge(df,performance,on="EmpID")

# print(df.info())
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.shape)
# print(df.size)
# print(df.columns)
# print(df.dtypes)

# print(df.isna().sum())
# print(df.isnull().sum())

# df["Age"]=df["Age"].fillna(df["Age"].mean())
# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# df["City"]=df["City"].fillna("Unknown")


# df["Name"]=df["Name"].str.strip().str.title()

# df["Bonus"]=df["Salary"]*10/100
# df["Tax"]=df["Salary"]*5/100
# df["Net Salary"]=df["Salary"]+df["Bonus"]+df["Tax"]
# df["Experience Bonus"]=df["Age"].apply(lambda x:2000 if x<25 else 5000)
# df["Final Salary"]=df["Net Salary"]+df["Experience Bonus"]
# df["Salary Category"]=df["Salary"].apply(lambda x:"High" if x>65000 else "Normal")
# mapping={
#     5:"Excellent",
#     4: "Very Good",
#     3: "Good",
#     2: "Average",
#     1:"Poor"
# }
# df["Performance Grade"]=df["Performance"].map(mapping)
# print(df)
# print(df[df["Salary"]>60000])
# print(df[df["Performance"]>=4])
# print(df[df["Department"]=="IT"])
# print(df[df["City"]=="Ahmedabad"])
# print(df[df["Salary"].between(60000,70000)])
# print(df[df["Department"].isin(["IT","HR"])])

# print(df
#       [
#           (df["Salary Category"]=="High")
#           &
#           (df["Performance"]>=4)
#       ])

# print(df.sort_values(by="Salary",ascending=True))
# print(df.sort_values(by="Salary"))
# print(df.sort_values(by=["Department","Salary"]))
# print(df.sort_values(by="Name"))
# print(df.nlargest(1,"Salary"))
# print(df.nsmallest(1,"Salary"))
# print(df["Salary"].mean())
# print(df["Salary"].median())
# print(df["Salary"].max())
# print(df["Salary"].min())

# print(df.groupby("Department")["Salary"].mean())
# print(df.groupby("Department")["Salary"].max())
# print(df.groupby("Department")["Salary"].min())
# print(df.groupby("Department")["EmpID"].count())
# print(df.groupby("Department")["Salary"].sum())
# print(df.groupby("Department")["Salary"].sum())
# print(df.groupby("City")["Salary"].mean())
# print(df.groupby("Performance Grade")["Salary"].mean())
# print(df.groupby(["Department","City"])["Salary"].mean())

# print(df.pivot_table("Salary","Department","City"))
# print(df.pivot_table("Salary","Department","Performance Grade"))

# print(pd.crosstab(df["Department"],df["Gender"]))
# print(pd.crosstab(df["Department"],df["City"]))
# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="mean"))
# print(pd.crosstab(df["Department"],df["Gender"],values=df["Salary"],aggfunc="max"))
# print(pd.crosstab(df["Department"],df["Gender"],margins=True,margins_name="Total"))
# print(pd.crosstab(df["Department"],df["Gender"],normalize="index"))

# print(df.nlargest(5,"Salary"))
# print(df.nsmallest(5,"Salary"))
# print(df.nlargest(3,"Final Salary"))

# print(df)
# print(df.loc[9,["Name","Salary","Department"]])
# print(df.iloc[5:10, [0, 1, 2]])

# df.to_csv("employee_final_report_3.csv")


#---------------------------------------------------------------

# import pandas as pd
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)
#
# try:
#     df=pd.read_csv("sales_data.csv")
# except Exception as e:
#     print(e)
#
# # print(df.head())
# # print(df.tail())
# print(df.info())
# # print(df.describe())
# # print(df.shape)
# # print(df.size)
# # print(df.columns)
# # print(df.dtypes)
#
# # print(df.isna())
# # print(df.isna().sum())
#
# df["Discount"]=df["Discount"].fillna(df["Discount"].median())
#
# # print(df.info())
#
# df["CustomerName"]=df["CustomerName"].str.strip().str.title()
#
# df["OrderDate"]=pd.to_datetime(df["OrderDate"])
# print(df["OrderDate"].dtype)
# df["Year"]=df["OrderDate"].dt.year
# df["Month Number"]=df["OrderDate"].dt.month
# df["Month Name"]=df["OrderDate"].dt.month_name()
# df["Day"]=df["OrderDate"].dt.day
# df["Day Name"]=df["OrderDate"].dt.day_name()
# df["Quarter"]=df["OrderDate"].dt.quarter
# df["Weekend Days"]=df["OrderDate"].dt.weekday
# df["Weekend"]=df["OrderDate"].dt.weekday>=5
#
# df["Total Amount"]=df["Quantity"]*df["Price"]
# df["Discount Amount"]=df["Total Amount"]*df["Discount"]/100
# df["Net Sales"]=df["Total Amount"]-df["Discount Amount"]
# df["Sales Category"]=df["Net Sales"].apply(lambda  x:"High" if x>50000 else "Medium")
# # print(df)
#
# print(df["Department"].value_counts())
# print(df["City"].value_counts())
# print(df["PaymentMode"].value_counts())
# print(df["Department"].value_counts(normalize=True)*100)
# print(df["Category"].unique())
# print(df["City"].nunique())
# print(df["Product"].nunique())
#
# print(df[df["Department"]=="Electronics"])
# print(df[df["City"]=="Ahmedabad"])
# print(df[df["Net Sales"]>20000])
# print(df[df["PaymentMode"]=="UPI"])
# print(df[df["Month Number"]==2])
# print(df[df["Month Name"]=="February"])
# print(df[df["Weekend"]==True])
# print(df[df["Discount"].between(5,10)])
# print(df[df["Category"].isin(["Food","Clothing"])])
#
# print(df.sort_values("Net Sales", ascending=False))
# print(df.sort_values("CustomerName"))
# print(df.sort_values(["Month Name","Net Sales"]))
#
# print(df.groupby("Department")["Net Sales"].agg(["sum","mean","max","min","count"]))
# print(df.groupby("City")["Net Sales"].sum())
# print(df.groupby("Month Name")["Net Sales"].sum())
# print(df.groupby("PaymentMode")["Net Sales"].mean())
#
# print(df.pivot_table(index="Department",columns="PaymentMode",values="Net Sales",aggfunc="mean"))
# print(df.pivot_table(index="Month Name",columns="City",values="Net Sales",aggfunc="sum"))
#
# print(pd.crosstab(df["Department"],df["PaymentMode"]))
# print(pd.crosstab(df["City"],df["Category"]))
# print(pd.crosstab(df["Department"],df["PaymentMode"],normalize=True))
# print(pd.crosstab(df["Department"],df["PaymentMode"],normalize=True)*100)
# print(pd.crosstab(df["Department"],df["PaymentMode"],margins=True,margins_name="Total"))
#
# print(df.sort_values("Net Sales", ascending=False).head(5))
# print(df.sort_values("Net Sales").head(5))
# print(df.sort_values("Net Sales", ascending=False).head(1))
# print(df.groupby("Department")["Net Sales"].mean().nlargest(1))
#
# print(df.loc[9])
# print(df.iloc[5:10,[1,20,3]])
#
#
# print(df.groupby("City")["Net Sales"].sum().nlargest(1))
# print(df.groupby("Department")["Net Sales"].sum().nlargest(1))
# print(df["PaymentMode"].unique().max())
# print(df.groupby("Month Name")["Net Sales"].sum().nlargest(1))
# print(df.groupby("Product")["Net Sales"].sum().nlargest(1))
# print(df.groupby("Category")["Net Sales"].sum().nsmallest(1))
# order_counts = df["Weekend Days"].value_counts()
# print(order_counts.idxmax())
# print(df.groupby("CustomerName")["Net Sales"].sum().nlargest(1))
# print(df.groupby("Department")["Net Sales"].mean().nlargest(1))
# print(df.groupby("City")["Net Sales"].mean().nlargest(1))
#
# df.to_csv("sales_analysis_final.csv")

#------------------------------------------------------------------------

# import pandas as pd
# import numpy as np

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# try:
#     customers=pd.read_csv("customers.csv")
#     products=pd.read_csv("products.csv")
#     orders_jan=pd.read_csv("orders_jan.csv")
#     orders_feb=pd.read_csv("orders_feb.csv")
# except Exception as e:
#     print(e)

# # print(customers.head())
# # print(customers.tail())
# # print(customers.info())
# # print(customers.describe())
# # print(customers.shape)
# # print(customers.size)
# print(customers.columns)
# # print(customers.dtypes)
# # print(customers.isna().sum())

# # print(products.head())
# # print(products.tail())
# # print(products.info())
# # print(products.describe())
# # print(products.shape)
# # print(products.size)
# print(products.columns)
# # print(products.dtypes)
# # print(products.isna().sum())

# # print(orders_jan.head())
# # print(orders_jan.tail())
# # print(orders_jan.info())
# # print(orders_jan.describe())
# # print(orders_jan.shape)
# # print(orders_jan.size)
# print(orders_jan.columns)
# # print(orders_jan.dtypes)
# # print(orders_jan.isna().sum())


# # print(orders_feb.head())
# # print(orders_feb.tail())
# # print(orders_feb.info())
# # print(orders_feb.describe())
# # print(orders_feb.shape)
# # print(orders_feb.size)
# print(orders_feb.columns)
# # print(orders_feb.dtypes)
# # print(orders_feb.isna().sum())


# customers.columns=customers.columns.str.strip().str.lower().str.replace(" ","_")
# print(customers.columns)

# orders_jan=orders_jan.rename(columns={
#         "CustomerID":"customer_id"
# })

# orders_feb=orders_feb.rename(columns={
#         "CustomerID":"customer_id"
# })

# print(orders_jan.columns)
# print(orders_feb.columns)

# customers["customer_name"]=customers["customer_name"].str.strip().str.title()
# print(customers)


# products["Product"]=products["Product"].str.strip().str.title()
# print(products)

# customers["age"]=customers["age"].fillna(customers["age"].mean()) #because of the age is have 20 to 60 in company so for that range i would prefer the mean of age because that is av.. age for the data


# customers["city"]=customers["city"].fillna("Unknown") #because of the city is missing so str no have arthimatic operation so we fill with str not idea out it 
# print(customers)

# orders_jan["Discount"]=orders_jan["Discount"].fillna(orders_jan["Discount"].median())  #because of repeat discount is prefect for the missing discount value 
# print(orders_jan)

# orders_feb["Discount"]=orders_feb["Discount"].fillna(orders_feb["Discount"].median())  #because of repeat discount is prefect for the missing discount value 
# print(orders_feb)

# customers=customers.drop_duplicates()
# print(customers)
# products=products.drop_duplicates()
# print(products)
# orders_jan=orders_jan.drop_duplicates()
# print(orders_jan)

# orders_feb=orders_feb.drop_duplicates()
# print(orders_feb)

# print(customers.dtypes)
# print(products.dtypes)
# print(orders_jan.dtypes)
# print(orders_feb.dtypes)


# customers["age"]=customers["age"].astype(int)
# print(customers.dtypes)

# products["Price"]=products["Price"].astype(float)
# print(products.dtypes)

# orders_jan["OrderDate"]=pd.to_datetime(orders_jan["OrderDate"])
# orders_feb["OrderDate"]=pd.to_datetime(orders_feb["OrderDate"])

# print(orders_jan.dtypes)
# print(orders_feb.dtypes)


# orders=pd.concat([orders_jan,orders_feb],ignore_index=True)
# print(orders)

# df_final=pd.merge(orders,customers,on="customer_id",how="outer")
# print(df_final)
# df=pd.merge(df_final,products,on="ProductID",how="outer")
# print(df)

# df["Total Amount"]=df["Price"]*df["Quantity"]

# df["Discount Amount"] =df["Total Amount"]*df["Discount"] / 100

# df["Net Sales"] =df["Total Amount"] - df["Discount Amount"]

# df["Sales Category"] = df["Net Sales"].apply(
#     lambda x: "High" if x >= 50000 else ("Medium" if x >= 20000 else "Low")
# )


# mapping_gender={
#     "M":"Male",
#     "F":"Female"
# }
# df["gender"]=df["gender"].map(mapping_gender)

# df["Year"]=df["OrderDate"].dt.year
# df["Month Number"]=df["OrderDate"].dt.month
# df["Month Name"]=df["OrderDate"].dt.month_name()
# df["Day"]=df["OrderDate"].dt.day
# df["Day Name"]=df["OrderDate"].dt.day_name()
# df["Quarter"]=df["OrderDate"].dt.quarter
# df["Weekend"]=df["OrderDate"].dt.weekday
# print(df)
# print(df[df["Weekend"]>=5])

# print(
#     df[
#     (df["Month Name"]=="January")
#        |
#     (df["Month Name"]=="February")
#       ]
#       )

# print(df[df["Month Number"].between(1,2)])

# print(df["Month Name"].value_counts())

# print(df[df["Net Sales"]>50000])

# print(df[df["city"]=="Ahmedabad"])
# print(df[df["PaymentMode"]=="UPI"])
# print(df[df["Category"]=="Electronics"])
# print(df[df["age"].between(25,30)])
# print(df[df["Discount"].between(5,10)])
# print(
#     df[
#     (df["gender"]=="Male")
#        &
#     (df["city"]=="Ahmedabad")
#       ]
#       )
# print(df[df["Sales Category"]=="High"])

# print(df[df["city"].isin(["Ahmedabad","Surat"])])

# print(df.nlargest(5,"Net Sales"))
# print(df.nsmallest(3,"Net Sales"))

# top_sales_index = df['Net Sales'].idxmax()  
# print(df.loc[top_sales_index, 'Product'])

# low_sales_index=df["Net Sales"].idxmin()
# print(df.loc[low_sales_index, 'Product'])

# print(df.sort_values("Net Sales",ascending=False))

# print(df.sort_values("customer_name"))
# print(df.sort_values(["city","Net Sales"]))

# print(df["PaymentMode"].value_counts())
# print(df["city"].value_counts())
# uniquecategory=df["Category"].unique()
# print(uniquecategory)
# print(df["city"].unique())
# print(df["Product"].unique())
# print(df["PaymentMode"].value_counts().idxmax())
# print(df["city"].value_counts().idxmax())
# print(df["PaymentMode"].value_counts(normalize=True)*100)

# print(df.groupby("city")["Net Sales"].sum())
# print(df.groupby("city")["Net Sales"].mean())

# print(df.groupby("Category")["Net Sales"].sum())
# print(df.groupby("Category")["Net Sales"].mean())

# print(df.groupby("PaymentMode")["Net Sales"].sum())

# print(df.groupby("gender")["Net Sales"].mean())
# print(df.groupby("Month Name")["Net Sales"].sum())


# print(df.groupby("Category")["Net Sales"].agg(["sum","mean","max","min","count"]))

# print(df.pivot_table(index="Category",columns="PaymentMode",values="Net Sales",fill_value=0,aggfunc="sum",margins=True,margins_name="Total"))

# print(df.pivot_table(index="city",columns="Category",values="Net Sales",aggfunc="mean"))

# print(df.pivot_table(index="Month Name",columns="Category",values="Net Sales",fill_value=0,aggfunc="sum",margins=True,margins_name="Total"))

# print(pd.crosstab(df["city"],df["gender"],values=df["OrderID"],aggfunc="count"))

# print(pd.crosstab(df["Category"],df["PaymentMode"],values=df["OrderID"],aggfunc="count"))

# print(pd.crosstab(df["city"],df["PaymentMode"],values=df["OrderID"],aggfunc="count"))

# print(pd.crosstab(df["Category"],df["PaymentMode"],values=df["Net Sales"],aggfunc="mean",normalize=True)*100)


# #right now i can not creates the small dataset for the pivot and melt please..

# #Business Questions
# print(df.groupby("city")["Net Sales"].sum().idxmax())
# top_sales_index = df['Net Sales'].idxmax()  
# print(df.loc[top_sales_index, 'Product'])
# print(df.groupby("Category")["Net Sales"].sum().idxmax())
# print(df["PaymentMode"].value_counts().idxmax())
# print(df.groupby("Month Name")["Net Sales"].sum().idxmax())
# print(df.groupby("customer_name")["Net Sales"].sum().idxmax())

# print(df.groupby("city")["Net Sales"].mean().idxmax())

# print(df["Sales Category"].value_counts(normalize=True)*100)

# print(df.groupby(["Category","PaymentMode"])["Net Sales"].sum().idxmax())

# df["Day_Type"] = df["OrderDate"].dt.weekday.apply(lambda x: "Weekend" if x >= 5 else "Weekday")
# sales_comparison = df.groupby("Day_Type")["Net Sales"].sum()
# print(sales_comparison)


# print(df.loc[df["OrderID"]=="O104"])
# print(df.columns)
# print(df.iloc[3:7, [7, 11, 16, 8]])

# df.to_csv("ecommerce_sales_final.csv.csv")

# total_orders = df["OrderID"].nunique()  
# total_net_sales = df["Net Sales"].sum()
# avg_order_value = df["Net Sales"].mean()
# highest_sales_city = df.groupby("city")["Net Sales"].sum().idxmax()
# best_product = df["Product"].value_counts().idxmax()

# best_category = df.groupby("Category")["Net Sales"].sum().idxmax()

# top_payment_mode = df["PaymentMode"].value_counts().idxmax()

# unique_customers = df["customer_name"].nunique()
# summary_data = {
#     "Metric": [
#         "Total Orders",
#         "Total Net Sales",
#         "Average Order Value",
#         "Highest Sales City",
#         "Best Product",
#         "Best Category",
#         "Top Payment Mode",
#         "Unique Customers"
#     ],
#     "Result": [
#         total_orders,
#         total_net_sales,
#         avg_order_value,
#         highest_sales_city,
#         best_product,
#         best_category,
#         top_payment_mode,
#         unique_customers
#     ]
# }

# df_summary = pd.DataFrame(summary_data)
# print(df_summary)

# df_summary.to_csv("ecommerce_business_summary.csv", index=False)

#------------------------------------------------------------------------

# import pandas as pd
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)
#
# try:
#     excel=pd.read_excel("internship_retail_messy_data.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)
#
#
# customers=excel["Customers"]
# product=excel["Products"]
# order_1=excel["Orders_Q1"]
# order_2=excel["Orders_Q2"]
#
# print(customers.info())
# print(customers.head())
# print(customers.tail())
# print(customers.describe())
# print(customers.shape)
# print(customers.columns)
# print(customers.dtypes)
# print(customers.isna().sum())
# #customers have the messay columns not good in data type of columns and some unusefull columns
#
# print(product.info())
# print(product.head())
# print(product.tail())
# print(product.describe())
# print(product.shape)
# print(product.columns)
# print(product.dtypes)
# print(product.isna().sum())
#
# #products have the messay columns not good in data type of columns and some unusefull columns
#
# print(order_1.info())
# print(order_1.head())
# print(order_1.tail())
# print(order_1.describe())
# print(order_1.shape)
# print(order_1.columns)
# print(order_1.dtypes)
# print(order_1.isna().sum())
#
# #order_1 have the messay columns not good in data type of columns and some unusefull columns
#
# print(order_2.info())
# print(order_2.head())
# print(order_2.tail())
# print(order_2.describe())
# print(order_2.shape)
# print(order_2.columns)
# print(order_2.dtypes)
# print(order_2.isna().sum())
#
# #order_2 have the messay columns not good in data type of columns and some unusefull columns
#
# customers.columns=customers.columns.str.strip().str.lower().str.replace(" ","_")
# print(customers.columns)
#
#
# product.columns=product.columns.str.strip().str.lower().str.replace(" ","_")
# print(product.columns)
#
# product=product.rename(columns={
#     "productid":"product_id"
# })
# print(product.columns)
#
# order_1.columns=order_1.columns.str.strip().str.lower().str.replace(" ","_")
# print(order_1.columns)
#
# order_1=order_1.rename(columns={
#     "productid":"product_id",
#     "customerid":"customer_id"
# })
# print(order_1.columns)
#
#
# order_2.columns=order_2.columns.str.strip().str.lower().str.replace(" ","_")
# print(order_2.columns)
#
# order_2=order_2.rename(columns={
#     "productid":"product_id",
#     "customerid":"customer_id"
# })
# print(order_2.columns)
#
# orders=pd.concat([order_1,order_2])
# print(orders)
#
# df_1=pd.merge(customers,orders,on="customer_id",how="inner")
#
# print(df_1)
#
# df=pd.merge(df_1,product,on="product_id",how="inner")
#
# df=df.drop_duplicates()
# print(df)
#
#
# df=df.drop(columns=["internal_tracking_id","temp_product_flag","internal_code"])
#
#
# print(df["age"])
# df["age"]=pd.to_numeric(df["age"],errors="coerce")
# df["age"]=df["age"].fillna(df["age"].mean()).astype(int)
# df["city"]=df["city"].fillna("Unknown")
# df["gender"]=df["gender"].fillna("Unknown")
# df["signup_date"]=pd.to_datetime(df["signup_date"],format="mixed")
# df["signup_date"]=df["signup_date"].fillna(df["signup_date"].mean())
# df["order_date"]=pd.to_datetime(df["order_date"],format="mixed",errors="coerce")
# df["order_date"]=df["order_date"].fillna(df["order_date"].mean())
# df["quantity"]=df["quantity"].fillna(df["quantity"].mean()).astype(int)
# df["discount%"]=df["discount%"].fillna(0) #discount always have datatype float and if you can direct fill but ask first then fill because some products does not have discount
# df["status"]=df["status"].fillna("Unknown")
# df["category"]=df["category"].fillna("Unknown")
# df["unit_price"]=df["unit_price"].str.replace("$","").str.replace(",","").astype(float)
# df["stock"]=pd.to_numeric(df["stock"],errors="coerce")
# df["stock"]=df["stock"].fillna(df["stock"].mean()).astype(int)
# print(df.columns)
# print(df.dtypes)
# print(df.isna().sum())
# df["customer_name"]=df["customer_name"].str.strip().str.title()
# df["city"]=df["city"].str.strip().str.title()
# df["gender"]=df["gender"].apply(lambda x:"Female" if x=="F" or x=="Female" else("Male" if x=="M" or x=="Male" else "Unknown"))
# df["payment_mode"]=df["payment_mode"].str.strip().str.title()
# df["status"]=df["status"].str.strip().str.title()
# df["product_name"]=df["product_name"].str.strip().str.title()
# df["category"]=df["category"].str.strip().str.title()
#
# df["total_amount"]=df["unit_price"]*df["quantity"]
# df["discount_amount"]=df["total_amount"]*df["discount%"]/100
# df["net_sales"]=df["total_amount"]-df["discount_amount"]
# df["sales_category"]=df["net_sales"].apply(lambda x:"High" if x>2000 else("Medium" if x>=500 else "Low"))
# df["year"]=df["order_date"].dt.year
# df["month_number"]=df["order_date"].dt.month
# df["month_name"]=df["order_date"].dt.month_name()
# df["day"]=df["order_date"].dt.day
# df["day_name"]=df["order_date"].dt.day_name()
# df["quarter"]=df["order_date"].dt.quarter
# df["weekend"]=df["order_date"].dt.weekday >=5
# print(df)
# orders_from_each_City=df["city"].value_counts()
# print(orders_from_each_City)
# payment_modes=df["payment_mode"].unique()
# print(payment_modes)
# unique_city_count=df["city"].nunique()
# print(unique_city_count)
# unique_products_count=df["product_name"].nunique()
# print(unique_products_count)
# percentage_of_orders_belongs_payment_mode=df["payment_mode"].value_counts(normalize=True)*100
# print(percentage_of_orders_belongs_payment_mode)
# unique_product_categories=df["category"].unique()
# print(unique_product_categories)
# order_status_occurs_most_frequently=df["status"].value_counts().head(1)
# print(order_status_occurs_most_frequently)
# net_sales_des_sort=df.sort_values("net_sales",ascending=False)
# print(net_sales_des_sort)
# print(df[df["city"]=="Ahmedabad"])
# print(df[df["payment_mode"]=="Upi"])
# print(df[df["weekend"]==True])
# print(df[df["category"]=="Accessories"])
# print(df
#         [
#         (df["net_sales"]>2000)
#         &
#          (df["payment_mode"]=="Cash")
#       ])
# print(df[
#         (df["weekend"]==True)
#         &
#          (df["month_name"]=="June")
#       ])
#
# print(df[
#         (df["discount%"]==0)
#         |
#          (df["status"]=="Cancelled")
#       ])
#
# print(df
#       [
#           (df["payment_mode"]!="Cash")
#       ])
# print(net_sales_des_sort.head())
# print(net_sales_des_sort.tail())
# print(df.groupby("city")["net_sales"].mean())
# print(df.groupby("category")["net_sales"].sum())
# print(df.groupby("product_name")["net_sales"].sum())
# print(df.groupby("payment_mode")["net_sales"].count())
# print(df.groupby("month_name")["net_sales"].max())
# print(df.groupby("gender")["net_sales"].min())
#
# cate_payment_total_net=df.pivot_table("net_sales","category","payment_mode",aggfunc="sum",fill_value=0,margins=True,margins_name="total_net")
# print(cate_payment_total_net)
#
# city_cate_av_net=df.pivot_table("net_sales","city","category",aggfunc="mean",fill_value=0,margins=True,margins_name="average_net")
# print(city_cate_av_net)
#
# month_cate_total_net=df.pivot_table("net_sales","month_name","category",aggfunc="sum",fill_value=0,margins=True,margins_name="total_net")
# print(month_cate_total_net)
#
# city_gender_crosstab=pd.crosstab(df["city"],df["gender"])
# print(city_gender_crosstab)
#
# cate_payment_mode_crosstab=pd.crosstab(df["category"],df["payment_mode"],values=df["net_sales"],aggfunc="sum",margins=True,margins_name="total")
# print(cate_payment_mode_crosstab)
#
# city_payment_mode_crosstab=pd.crosstab(df["city"],df["payment_mode"])
# print(city_payment_mode_crosstab)
#
# print(df.set_index("order_id"))
# print(df.reset_index())
# print(df.reset_index(drop=True))
# print(df)
# print(df.loc[2])  #give me the second index row means 0 1 2  2 is my answer and if i set the index unique so i want the direct the row
# print(df.iloc[:,[1,6]])
# print(df.loc[df["net_sales"].idxmax()])
# print(df.loc[df["net_sales"].idxmin()])
#
# gene_high_sale_total_city=df.groupby("city")["net_sales"].sum().idxmax()
# print(gene_high_sale_total_city)
#
# gene_high_sale_product=df.groupby("product_name")["net_sales"].sum().idxmax()
# print(gene_high_sale_product)
#
# category_performs_best=df["category"].value_counts().idxmax()
# print(category_performs_best)
#
# payment_methods_fe_used=df["payment_mode"].value_counts().idxmax()
# print(payment_methods_fe_used)
#
# month_name_high_sale=df.groupby("month_name")["net_sales"].sum().idxmax()
# print(month_name_high_sale)
#
# highest_value_customer=df.groupby("customer_name")["net_sales"].sum().idxmax()
# print(highest_value_customer)
#
# city_with_high_av_order_v=df.groupby("city")["order_id"].count().idxmax()
# print(city_with_high_av_order_v)
#
# product_sell_high_total_q=df.groupby("product_name")["quantity"].sum().idxmax()
# print(product_sell_high_total_q)
#
# pre_statu=df["status"].value_counts(normalize=True)*100
# print(pre_statu)
#
# # i don not solution of the 10
#
# #business_summary
#
# Total_Orders=df["order_id"].count()
# print(Total_Orders)
#
# TotalNet_Sales=df["net_sales"].sum()
# print(TotalNet_Sales)
#
# Average_Order_Value=df["net_sales"].mean()
# print(Average_Order_Value)
#
# Unique_Customers=df["customer_name"].nunique()
# print(Unique_Customers)
#
# print(gene_high_sale_total_city)
#
# print(gene_high_sale_product)
# print(category_performs_best)
# print(payment_methods_fe_used)
# print(month_name_high_sale)
# print(highest_value_customer)
#
# business_summary = pd.DataFrame({
#     "Metric": [
#         "Total Orders",
#         "Total Net Sales",
#         "Average Order Value",
#         "Unique Customers",
#         "Top City by Sales",
#         "Top Product",
#         "Best Performing Category",
#         "Most Used Payment Method",
#         "Peak Sales Month",
#         "Highest Value Customer"
#     ],
#     "Value": [
#         Total_Orders,
#         TotalNet_Sales,
#         Average_Order_Value,
#         Unique_Customers,
#         gene_high_sale_total_city,
#         gene_high_sale_product,
#         category_performs_best,
#         payment_methods_fe_used,
#         month_name_high_sale,
#         highest_value_customer
#     ]
# })
# try:
#     with pd.ExcelWriter("retail_sales_analysis_final.xlsx", engine="openpyxl") as writer:
#         df.to_excel(writer, sheet_name="Clean Data", index=False)
#         business_summary.to_excel(writer, sheet_name="Summary", index=False)
#         cate_payment_total_net.to_excel(writer, sheet_name="Pivot_table", index=False)
#     print("Excel file created successfully with vertical KPI layout!")
# except Exception as e:
#     print(f"An error occurred: {e}")

#------------------------------------------------------------------------------------------
# import pandas as pd

# try:
#     emp=pd.read_csv("practical_emp.csv")
#     attendance=pd.read_csv("practical_attendance.csv")
#     performance=pd.read_csv("practical_performance.csv")
# except Exception as e:
#     print(e)

# # print(emp.head())
# # print(emp.tail())
# # print(emp.info())
# # print(emp.describe())
# # print(emp.shape)
# # print(emp.size)
# # print(emp.columns)
# # print(emp.dtypes)
# # print(emp.isna().sum())
# # print(emp.duplicated().sum())

# # print(attendance.head())
# # print(attendance.tail())
# # print(attendance.info())
# # print(attendance.describe())
# # print(attendance.shape)
# # print(attendance.size)
# # print(attendance.columns)
# # print(attendance.dtypes)
# # print(attendance.isna().sum())
# # print(attendance.duplicated().sum())

# # print(performance.head())
# # print(performance.tail())
# # print(performance.info())
# # print(performance.describe())
# # print(performance.shape)
# # print(performance.size)
# # print(performance.columns)
# # print(performance.dtypes)
# # print(performance.isna().sum())
# # print(performance.duplicated().sum())

# emp.columns=emp.columns.str.strip().str.lower().str.replace(" ","_")
# emp["joining_date"]=pd.to_datetime(emp["joining_date"],format="mixed")
# emp["city"]=emp["city"].fillna("Unknown")
# emp["gender"]=emp["gender"].fillna("Unknown")
# emp["salary"]=emp["salary"].fillna(emp["salary"].median())
# emp=emp.rename(columns={
#     "emp_id":"employee_id"
# })
# print(emp[emp.duplicated()])
# emp=emp.drop_duplicates()

# attendance.columns=attendance.columns.str.strip().str.lower().str.replace(" ","_")
# attendance["present_days"]=attendance["present_days"].fillna(attendance["present_days"].mean()).astype(int)
# attendance["leave_days"]=attendance["leave_days"].fillna(attendance["leave_days"].mean()).astype(int)
# print(attendance[attendance.duplicated()])
# attendance=attendance.drop_duplicates()

# performance.columns=performance.columns.str.strip().str.lower().str.replace(" ","_")
# performance["rating"]=performance["rating"].fillna(performance["rating"].mean())
# performance["bonus"]=performance["bonus"].fillna(performance["bonus"].mean())
# print(performance[performance.duplicated()])
# performance=performance.drop_duplicates()

# df_1=pd.merge(emp,attendance,on="employee_id",how="inner")
# df=pd.merge(df_1,performance,on="employee_id",how="inner")
# df.columns=df.columns.str.title()
# df["Employee_Name"]=df["Employee_Name"].str.strip().str.title()
# print(df.columns)
# df["Gender"]=df["Gender"].str.title().replace({
#     "M":"Male"
# })
# df["Attendance_%"]=df["Present_Days"]/df["Working_Days"]*100
# df["Salary_Category"] = pd.cut(
#     df["Salary"], 
#     bins=[35000, 70000, 96000, float("inf")], 
#     labels=["Low", "Medium", "High"],
#     right=False
# )

# df["Performance_Level"]=pd.cut(
#     df["Rating"],
#     bins=[0,3.5,4,4.5,5],
#     labels=["Poor","Average","Good","Excellent"]
# )
# #i dicided this bins bounatry with max min and mean
# df["Salary_Quartile"]=pd.qcut(
#     df["Salary"],
#     q=4,
#     labels=["q1","q2","q3","q4"]
# )
# df["Total_Compensation"]=df["Salary"]+df["Bonus"]

# print(df.query("Status=='Active'"))
# print(df.query("Salary>70000"))
# print(df.query("Department=='IT'"))
# print(df.query("Salary_Category=='High'"))
# print(df.query("City=='Ahmedabad'"))

# print(df["Department"].value_counts(normalize=True)*100)
# print(df["City"].value_counts(normalize=True)*100)
# print(df["Salary_Category"].value_counts())
# print(df["Performance_Level"].value_counts())
# print(df["Department"].unique())
# print(df["City"].unique())
# print(df["Department"].nunique())
# print(df["City"].nunique())
# print(df.groupby("Department")["Salary"].agg(["mean","max","min","count"]))
# print(df.columns)
# print(df.groupby("Department")["Attendance_%"].agg("mean"))
# print(df.groupby("Department")["Rating"].agg("mean"))
# print(df.groupby("Department")["Bonus"].agg("sum"))
# df["Dept_Avg_Salary"]=df.groupby("Department")["Salary"].transform("mean")
# df["Dept_Total_Salary"]=df.groupby("Department")["Salary"].transform("sum")
# df["Contribution_%"]=df["Salary"]/df["Dept_Total_Salary"]*100
# df["Salary_Difference"]=df["Salary"]-df["Dept_Avg_Salary"]

# print(df.pivot_table(index="Department",columns="City",values="Salary",aggfunc="mean",fill_value=0))
# print(df.pivot_table(index="Department",columns="Performance_Level",values="Salary",aggfunc="count",fill_value=0))
# print(df.pivot_table(index="City",columns="Salary_Category",values="Salary",aggfunc="mean",fill_value=0))

# print(pd.crosstab(df["Department"],df["Gender"],normalize=True)*100)
# print(pd.crosstab(df["Department"],df["Performance_Level"],normalize=True)*100)

# #we did not learn about the rank so i used the sort

# print(df.sort_values("Salary",ascending=False)[["Employee_Name","Salary"]].head())
# print(df["Salary"].nlargest(5))
# print(df.sort_values("Bonus",ascending=False)[["Employee_Name","Salary","Bonus"]].head())
# print(df["Bonus"].nlargest(5))
# print(df.sort_values("Rating",ascending=False)[["Employee_Name","Rating"]].head(1))
# print(df["Rating"].nlargest(1))

# print(df.groupby("Department")["Salary"].sum().nlargest(1))
# print(df.groupby("Department")["Attendance_%"].mean().nlargest(1))
# print(df.groupby("City")["Rating"].sum().nlargest(1))
# print(df.query("Salary>Dept_Avg_Salary")[["Employee_Name","Salary","Department"]])
# print(df.query("`Attendance_%`< 80")[["Employee_Name","Salary","Department","Attendance_%"]])
# print(df.query("Bonus>20000")[["Employee_Name","Salary","Department"]])
# print(df.groupby("Department")["Salary"].sum().nlargest(1))
# print(df["Salary_Category"].value_counts().nlargest(1))
# print(df.groupby("Performance_Level")["Bonus"].mean())
# print(df.sort_values("Total_Compensation",ascending=False,ignore_index=True)[["Employee_Name","Salary","Department"]].head(10))

# df.to_excel("internship_project_final.xlsx")
# #i did not creates the sheets because of the some reason please undeestand that


#-------------------------------------------------------------------------------
# import pandas as pd
#
# try:
#     emp=pd.read_csv("interview_emp.csv")
#     salary=pd.read_csv("interview_salary.csv")
#     performance=pd.read_csv("interview_performance.csv")
# except Exception as e:
#     print(e)
#
# # print(emp.info())
# # print(emp.head())
# # print(emp.tail())
# # print(emp.describe())
# # print(emp.shape)
# # print(emp.columns)
# # print(emp.dtypes)
# # print(emp.isna().sum())
# # print(emp.duplicated().sum())
#
# # print(salary.info())
# # print(salary.head())
# # print(salary.tail())
# # print(salary.describe())
# # print(salary.shape)
# # print(salary.columns)
# # print(salary.dtypes)
# # print(salary.isna().sum())
# # print(salary.duplicated().sum())
#
# # print(performance.info())
# # print(performance.head())
# # print(performance.tail())
# # print(performance.describe())
# # print(performance.shape)
# # print(performance.columns)
# # print(performance.dtypes)
# # print(performance.isna().sum())
# # print(performance.duplicated().sum())
#
# emp.columns=emp.columns.str.strip().str.lower().str.replace(" ","_")
# salary.columns=salary.columns.str.strip().str.lower().str.replace(" ","_")
# performance.columns=performance.columns.str.strip().str.lower().str.replace(" ","_")
#
#
# emp=emp.rename(columns={
#     'employee_name':"name",
#     'dept_name':"department"
# })
# emp["joining_date"]=pd.to_datetime(emp["joining_date"])
# emp["gender"]=emp["gender"].str.strip().str.title().replace({
#     "M":"Male",
#     "F":"Female"
# })
# emp["department"]=emp["department"].str.strip().str.title().replace({
#     "It":"IT",
#     "Hr":"HR",
#     "Human Resources":"HR"
# })
# emp["city"]=emp["city"].fillna("Unknown")
# emp["salary"]=emp["salary"].fillna(emp["salary"].median())
# print(emp["department"].unique())#to check our changes means replace work or check to other values
# print(emp["gender"].unique())#to check our changes means replace work or check to other values
#
# salary=salary.rename(columns={
#     "emp_id":"employee_id",
#     "attendance_percentage":"attendance_%"
# })
# salary["attendance_%"]=salary["attendance_%"].fillna(salary["attendance_%"].mean())
# salary=salary.drop_duplicates()
#
# performance=performance.rename(columns={
#     "id_employee":"employee_id",
#     "performance_rating":"rating"
# })
# performance["rating"]=performance["rating"].fillna(performance["rating"].mean())
# performance=performance.drop_duplicates()
#
#
# me=pd.merge(emp,salary,on="employee_id",how="inner")
# df=pd.merge(me,performance,on="employee_id",how="inner")
# print(df.info())
# print(df.columns)
# print(df.dtypes)
#
# df["total_compensation"]=df["salary"]+df["bonus"]
# #attendance_% is already thier
# df["salary_category"]=pd.cut(df["salary"],
# bins=[58000,80000,100000,float("inf")],
# labels=["Low","Medium","High"],
# include_lowest=True)
# df["salary_quartile"]=pd.qcut(df["salary"],
#                               q=4,
#                               labels=["Q1","Q2","Q3","Q4"])
# df["performance_level"]=pd.cut(df["rating"],
#                                bins=[0,3,4,float("inf")],
#                                labels=["Poor","Average","High"])
# df["joining_year"]=df["joining_date"].dt.year
# df["joining_month"]=df["joining_date"].dt.month_name()
# df["joining_quarter"]=df["joining_date"].dt.quarter
# df["experience"]=2026-df["joining_year"]
# df["experience_band"]=df["experience"].apply(lambda x:"Junior" if x<=2 else("Under-qualified" if x<5 else "Senior"))
# df["department_average_salary"]=df.groupby("department")["salary"].transform("mean")
# df["department_total_salary"]=df.groupby("department")["salary"].transform("sum")
# df["salary_gap"]=df["salary"]-df["department_average_salary"]
# df["salary_contribution_%"]=df["salary"]/df["department_total_salary"]*100
# # print(df.groupby("department")["salary_contribution_%"].sum()) # to check df["salary_contribution_%"] is right
# df["company_salary_rank"]=df["salary"].rank(ascending=False,method="dense")
# df["department_salary_rank"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# df["Rating_Rank"]=df["company_salary_rank"].apply(lambda x:3 if x>=8 else(2 if x>3 else 1))
# df["Top Performer Flag"]=df["Rating_Rank"].apply(lambda x:"Low" if x==3 else("Medium" if x==2 else "Top"))
# print(df.corr(numeric_only=True))
# data = df.select_dtypes(include=["number"])
# print(data.cov())
# print(df["salary"].corr(df["experience"]))
# print(df["salary"].corr(df["rating"]))
# print(df["bonus"].corr(df["salary"]))
# matrix_corr=df.corr(numeric_only=True)["salary"]
# matrix_corr=matrix_corr.drop("salary").idxmax()
# print(matrix_corr) #answer is : total_compensation 0.999518
# df["rolling_avrage_salary"]=df["salary"].rolling(3,min_periods=1).mean()
# df["rolling_avrage_bonus"]=df["bonus"].rolling(3,min_periods=1).mean()
# df["rolling_avrage_rating"]=df["rating"].rolling(3,min_periods=1).mean()
# print(df)
# it_average = df[df["department"] == "IT"]["salary"].mean()
# print(df.query("department == 'IT' and salary > @it_average").reset_index())
# print(df.query("performance_level=='High'").reset_index()) #i have not the Employees with Excellent rating
# print(df.query("`attendance_%`>90").reset_index())
# print(df.query("salary_category=='High'").reset_index())
# print(df.query("joining_year<2022").reset_index())
#
# department_wise=df.groupby("department")["salary"].agg(["mean","max","min","count"])
# print(department_wise)
# department_wise_avrage_rating=df.groupby("department")["rating"].agg("mean")
# print(department_wise_avrage_rating)
# department_wise_avrage_attendance=df.groupby("department")["attendance_%"].agg("mean")
# print(department_wise_avrage_attendance)
# pivot_table1=df.pivot_table(index="department",columns="city",values="salary",aggfunc="mean",fill_value=0)
# print(pivot_table1)
# pivot_table2=df.pivot_table(index="department",columns="salary_category",values="employee_id",aggfunc="count",fill_value=0)
# print(pivot_table2)
# pivot_table3=df.pivot_table(index="joining_year",columns="department",values="rating",aggfunc="mean",fill_value=0)
# print(pivot_table3)
#
# crosstab1=pd.crosstab(index=df["department"],columns=df["gender"])
# print(crosstab1)
# crosstab2=pd.crosstab(index=df["department"],columns=df["performance_level"])
# print(crosstab2)
# crosstab3=pd.crosstab(index=df["city"],columns=df["salary_category"])
# print(crosstab3)
#
# print(df.groupby("department")["salary"].mean().idxmax())
# print(df.groupby("city")["rating"].mean().idxmax())
# print(df.groupby("department")["total_compensation"].sum().idxmax())
# print(df.nlargest(1,"total_compensation")[["employee_id","name","department","salary","total_compensation"]])
# print(df.nlargest(1,"rating")[["employee_id","name","department","salary","rating"]])
# print(df["salary_category"].value_counts().idxmax())
# print(df.groupby("department")["rating"].mean().idxmax())#i do not have the performance in int so i used the rating
# print(df["joining_year"].value_counts().idxmax())
# print(df["city"].value_counts().idxmax())
# print(df.groupby("department")["salary"].sum().idxmax())
#
#
# Total_Employees=df["employee_id"].count()
# print(Total_Employees)
# Total_Salary =df["salary"].sum()
# print(Total_Salary)
# Average_Salary=df["salary"].mean()
# print(Average_Salary)
# Average_Rating=df["rating"].mean()
# print(Average_Rating)
# Average_Attendance=df["attendance_%"].mean()
# print(Average_Attendance)
# Highest_Paid_Department = df.groupby("department")["salary"].mean().idxmax()
# print(Highest_Paid_Department)
# Top_Employee = df.nlargest(1,"rating")
# print(Top_Employee)
# Best_Performing_Department=df.groupby("department")["rating"].mean().idxmax()
# print(Best_Performing_Department)
# Most_Common_Salary_Category =df["salary_category"].value_counts().idxmax()
# print(Most_Common_Salary_Category)
# Highest_Salary=df["salary"].max()
# print(Highest_Salary)
# Lowest_Salary=df["salary"].min()
# print(Lowest_Salary)
#
#
# kpi_data = {
#     "Metric Name": [
#         "Total Employees",
#         "Total Salary Expenditure",
#         "Average Salary",
#         "Average Performance Rating",
#         "Average Attendance %",
#         "Highest Paid Department (Avg)",
#         "Highest Revenue/Compensation Dept",
#         "Best Performing Department (Avg Rating)",
#         "Most Common Salary Category",
#         "Highest Individual Salary",
#         "Lowest Individual Salary",
#         "Top Employee (Highest Compensation)",
#         "Top Rated Employee",
#         "Peak Hiring Year",
#         "Most Common Employee City"
#     ],
#     "Value": [
#         Total_Employees,
#         Total_Salary,
#         Average_Salary,
#         Average_Rating,
#         Average_Attendance,
#         Highest_Paid_Department,
#         df.groupby("department")["total_compensation"].sum().idxmax(),
#         Best_Performing_Department,
#         Most_Common_Salary_Category,
#         Highest_Salary,
#         Lowest_Salary,
#         df.nlargest(1,"total_compensation")["name"].values[0],
#         df.nlargest(1,"rating")["name"].values[0],
#         df["joining_year"].value_counts().idxmax(),
#         df["city"].value_counts().idxmax()
#     ]
# }
#
# business_summary_df = pd.DataFrame(kpi_data)
#
#
#
# try:
#     with pd.ExcelWriter("HR_Analytics_Report.xlsx", engine="openpyxl") as writer:
#
#
#         df.to_excel(writer, sheet_name="Clean Data", index=False)
#
#         # Sheet 2: Department Summary (MUST keep index=True so department names show!)
#         department_wise.to_excel(writer, sheet_name="Department Summary", index=True)
#
#         start_row = 0
#         pivots = [
#             ("Average Salary by Department & City", pivot_table1),
#             ("Employee Count by Department & Salary Category", pivot_table2),
#             ("Average Rating by Joining Year & Department", pivot_table3)
#         ]
#         for title, pivot in pivots:
#             pd.DataFrame([title]).to_excel(writer, sheet_name="Pivot Tables", startrow=start_row, index=False, header=False)
#             pivot.to_excel(writer, sheet_name="Pivot Tables", startrow=start_row + 1, index=True)
#             start_row += len(pivot) + 4
#         start_row = 0
#         crosstabs = [
#             ("Gender Distribution by Department", crosstab1),
#             ("Performance Level Distribution by Department", crosstab2),
#             ("Salary Category Distribution by City", crosstab3)
#         ]
#         for title, x_tab in crosstabs:
#             pd.DataFrame([title]).to_excel(writer, sheet_name="Crosstabs", startrow=start_row, index=False, header=False)
#             x_tab.to_excel(writer, sheet_name="Crosstabs", startrow=start_row + 1, index=True)
#             start_row += len(x_tab) + 4
#
#
#         business_summary_df.to_excel(writer, sheet_name="Business Summary", index=False)
#
#     print("Excel file 'HR_Analytics_Report.xlsx' created successfully with all 5 sheets!")
#
# except Exception as e:
#     print(f"An error occurred: {e}")

#-------------------------------------------------------------------------------------------------------------
#
# import pandas as pd
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)
#
# try:
#     emp=pd.read_csv("iemployees.csv")
#     attendance=pd.read_csv("attendance.csv")
#     customer=pd.read_csv("customers.csv")
#     product=pd.read_csv("products.csv")
#     sale = pd.read_csv("sales.csv")
#     price_history = pd.read_csv("price_history.csv")
#     target=pd.read_csv("targets.csv")
# except Exception as e:
#     print(e)
#
# # print(emp.info())
# # print(emp.head())
# # print(emp.tail())
# # print(emp.describe())
# # print(emp.columns)
# # print(emp.dtypes)
# # print(emp.size)
# # print(emp.shape)
# # print(emp.isna().sum())
# # print(emp.duplicated().sum())
# #
# # print(customer.info())
# # print(customer.head())
# # print(customer.tail())
# # print(customer.describe())
# # print(customer.columns)
# # print(customer.dtypes)
# # print(customer.size)
# # print(customer.shape)
# # print(customer.isna().sum())
# # print(customer.duplicated().sum())
# #
# # print(attendance.info())
# # print(attendance.head())
# # print(attendance.tail())
# # print(attendance.describe())
# # print(attendance.columns)
# # print(attendance.dtypes)
# # print(attendance.size)
# # print(attendance.shape)
# # print(attendance.isna().sum())
# # print(attendance.duplicated().sum())
# #
# # print(product.info())
# # print(product.head())
# # print(product.tail())
# # print(product.describe())
# # print(product.columns)
# # print(product.dtypes)
# # print(product.size)
# # print(product.shape)
# # print(product.isna().sum())
# # print(product.duplicated().sum())
# #
# # print(price_history.info())
# # print(price_history.head())
# # print(price_history.tail())
# # print(price_history.describe())
# # print(price_history.columns)
# # print(price_history.dtypes)
# # print(price_history.size)
# # print(price_history.shape)
# # print(price_history.isna().sum())
# # print(price_history.duplicated().sum())
# #
# # print(sale.info())
# # print(sale.head())
# # print(sale.tail())
# # print(sale.describe())
# # print(sale.columns)
# # print(sale.dtypes)
# # print(sale.size)
# # print(sale.shape)
# # print(sale.isna().sum())
# # print(sale.duplicated().sum())
# #
# # print(target.info())
# # print(target.head())
# # print(target.tail())
# # print(target.describe())
# # print(target.columns)
# # print(target.dtypes)
# # print(target.size)
# # print(target.shape)
# # print(target.isna().sum())
# # print(target.duplicated().sum())
#
#
# emp.columns=emp.columns.str.strip().str.lower().str.replace(" ","_")
# emp["joining_date"]=pd.to_datetime(emp["joining_date"])
# emp["salary"]=emp["salary"].str.strip().str.replace(",","").str.replace("₹","")
# emp["salary"]=pd.to_numeric(emp["salary"])
# emp["salary"]=emp["salary"].fillna(emp["salary"].median())
# emp=emp.drop_duplicates()
# emp["employee_name"]=emp["employee_name"].str.strip().str.title()
# emp["city"]=emp["city"].replace({
#     "Ahd":"Ahmedabad"
# })
# emp["gender"]=emp["gender"].replace({
#    "M":"Male",
#     "F":"Female"
# })
# emp["skills"]=emp["skills"].str.split(",")
# emp=emp.explode("skills")
#
# customer.columns=customer.columns.str.strip().str.lower().str.replace(" ","_")
# customer=customer.rename(columns={
#     "customerid":"customer_id"
# })
# customer["city"]=customer["city"].replace({
#     "Ahd":"Ahmedabad"
# })
#
#
# attendance.columns=attendance.columns.str.strip().str.lower().str.replace(" ","_")
# attendance=attendance.rename(columns={
#     "employeeid":"employee_id"
# })
# attendance["present_days"]=attendance["present_days"].fillna(attendance["present_days"].mean()).astype("int")
# attendance["leave_days"]=attendance["leave_days"].fillna(attendance["leave_days"].mean()).astype("int")
# attendance["month"]=pd.to_datetime(attendance["month"])
# attendance=attendance.drop_duplicates()
#
# product.columns=product.columns.str.strip().str.lower().str.replace(" ","_")
# product=product.rename(columns={
#     "productid":"product_id"
# })
# product["base_price"]=product["base_price"].str.strip().str.replace(",","").str.replace("₹","")
# product["base_price"]=pd.to_numeric(product["base_price"])
# product["stock"]=product["stock"].fillna(product["stock"].mean())
#
# price_history.columns=price_history.columns.str.strip().str.lower().str.replace(" ","_")
# price_history=price_history.rename(columns={
#     'productid':"product_id",
#     'pricetime':"price_time",
#     'unitprice':"unit_price"
# })
# price_history["price_time"]=pd.to_datetime(price_history["price_time"])
#
# sale.columns=sale.columns.str.strip().str.lower()
# sale=sale.rename(columns={
#     'orderid':"order_id",
#     'ordertime':"order_time",
#     'employeeid':"employee_id",
#     'customerid':"customer_id",
#     'productid':"product_id",
#     'salesamount':"sales_amount"
# })
# sale["order_time"]=pd.to_datetime(sale["order_time"])
# sale["discount%"]=sale["discount%"].fillna(0)
# sale=sale.drop_duplicates()
#
# target.columns=target.columns.str.strip().str.lower()
# target["date"]=pd.to_datetime(target["date"])
#
# df=pd.merge(emp,attendance,on="employee_id",how="inner")
# df=pd.merge(df,sale,on="employee_id",how="inner")
# df=pd.merge(df,target,on="department",how="inner")
# df=pd.merge(df,price_history,on="product_id",how="inner")
# df=pd.merge(df,customer,on="customer_id",how="inner")
# df=pd.merge(df,product,on="product_id",how="inner")
#
# df=df.rename(columns={
#     "city_x":"employee_city",
#     "city_y":"customer_city"
# })
#
# print(df["skills"].value_counts().idxmax())
# print(df.groupby("skills")["salary"].sum().nlargest(3)) #What are the top 3 skills by salary
# print(df["skills"].value_counts().nsmallest(3))#What are the top 3 skills by rareness
# print(df["skills"].nunique())
# most_emp_python=df.query("skills=='Python'")
# print(df.groupby("department")["skills"].count().idxmax())
# print(df.groupby("employee_id")["skills"].nunique().idxmax())
# print(df.pivot_table(index="department",columns="skills",values="salary",aggfunc="mean",fill_value=0))
# print(pd.crosstab(index=df["department"],columns=df["skills"],normalize=True)*100)
#
# # Employee Analysis
#
# print(df["salary"].mean())
# print(df["salary"].max())
# print(df["salary"].min())
# print(df["salary"].sum())
# print(df["employee_id"].nunique())
# print(df.groupby("department")["salary"].agg(["mean","max","min","sum","count"]))
#
#
# df["department_average_salary"]=df.groupby("department")["salary"].transform("mean")
# df["department_total_salary"]=df.groupby("department")["salary"].transform("sum")
# df["salary_difference"]=df["salary"]-df["department_average_salary"]
# df["salary_contribution_%"]=df["salary"]/df["department_total_salary"]*100
# print(df.query("salary>`department_average_salary`"))
#
# df["salary_band"]=pd.cut(df["salary"],
#                          bins=[68000,80000,100000,float("inf")],
#                          labels=["Low","Medium","High"],include_lowest=True)
# df["salary_quartile"]=pd.qcut(df["salary"],q=3,duplicates='drop',labels=["Q1","Q2","Q3"]) #if i wrote the 4 so show me this error: ValueError: Bin labels must be one fewer than the number of bin edges
# print(df["salary_band"].value_counts().idxmax())
# print(df.groupby("department")["salary"].mean().idxmax())
# print(df.groupby("employee_city")["salary"].mean().idxmax())
#
# df["company_salary_rank"]=df["salary"].rank(ascending=False,method="dense")
# df["department_salary_rank"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# emp_unique=df.drop_duplicates(subset="employee_id",keep="first")
# print(emp_unique.nlargest(5,"salary"))
# emp_unique=df.drop_duplicates(subset="employee_id",keep="first")
# print(emp_unique[emp_unique["department_salary_rank"]==1])
# print(emp_unique[emp_unique["department_salary_rank"]<=2])
#
# #customer analysis
# #DO NOT NEEDS TO MERGE I ALREADY MERGE ALL
# print(df["customer_id"].count())
# print(df["customer_name"].unique())
# print(df.groupby("customer_city")["customer_name"].count())
# print(df.groupby("segment")["customer_name"].count())
# print(df.groupby("customer_name")["sales_amount"].sum().nlargest(5))
# print(df["customer_city"].value_counts().idxmax())
# print(df.groupby("customer_city")["sales_amount"].sum().idxmax())
# print(df.groupby("customer_name")["sales_amount"].sum()/df["sales_amount"].sum()*100)
#
# # Product Analysis
#
# df["total_sales"]=df["quantity"]*df["unit_price"]
# print(df.groupby("product_id")["quantity"].count().idxmax())
# print(df.groupby("product_id")["quantity"].count().idxmin())
# print(df.groupby("product_id")["total_sales"].mean().idxmax())
# print(df.groupby("product_id")["total_sales"].mean().idxmin())
# print(df.groupby("category")["total_sales"].sum())
# print(df.groupby("category")["quantity"].count())
# print(df.groupby("category")["unit_price"].mean())
# df["product_wise_rank"]=df.groupby("product_id")["total_sales"].rank(ascending=False,method="dense")
#
#
# df["discount_amount"]=df["total_sales"]*df["discount%"]/100
# df["net_sales"]=df["total_sales"]-df["discount_amount"]
# print(df)
# print(df["discount_amount"].nlargest(1))
# print(df.groupby("product_id")["net_sales"].sum().idxmax())
# print(df.groupby("product_id")["discount_amount"].mean())
# print(df["discount_amount"].sum())
# print(df["net_sales"].sum())
#
# print(df.pivot_table(index="department",columns="employee_city",values="salary",aggfunc="mean",fill_value=0))
# print(df.pivot_table(index="category",columns="product_name",values="sales_amount",aggfunc="sum",fill_value=0))
# print(df.pivot_table(index="department",columns="skills",values="employee_id",aggfunc="count",fill_value=0))
#
# print(pd.crosstab(index=df["department"],columns=df["gender"],normalize=True)*100)
# print(pd.crosstab(index=df["department"],columns=df["skills"]))
# print(pd.crosstab(index=df["customer_city"],columns=df["segment"]))
#
# melt_data = pd.melt(
#     df,
#     id_vars="employee_id",
#     value_vars=["present_days", "leave_days"],
#     var_name="attendance_status",
#     value_name="days_count"
# )
#
# print(melt_data)
#
# melt_data_unique = melt_data.drop_duplicates(subset=["employee_id", "attendance_status"], keep="first")
#
# pivot_data = melt_data_unique.pivot(
#     index="employee_id",
#     columns="attendance_status",
#     values="days_count"
# ).reset_index()
#
# print(pivot_data)
#
# #i may be do not use the good of melt and pivot
#
# print(df.corr(numeric_only=True))
#
# number_data = df.select_dtypes(["number"])
# covariance_matrix = number_data.cov()
# print(covariance_matrix)
#
#
# print(df["salary"].corr(df["sales_amount"])) #-0.47100144643597247
# df["attendance%"]=df["present_days"]/df['working_days']*100
# print(df["attendance%"].corr(df["sales_amount"]))# -0.10511014447540605
# print(df["quantity"].corr(df["sales_amount"]))# -0.3139563039850516
# print(df["discount_amount"].corr(df["net_sales"])) #0.9626971209379639
# # i did not learn stack and unstack so i can not answer this : strongest positive correlation.
# # Strongest negative correlation.
# # Weakest correlation.
#
# df["3day_rolling_average_sales"]=df["sales_amount"].rolling(3,min_periods=1).mean()
# df["7day_rolling_average_sales"]=df["sales_amount"].rolling(7,min_periods=1).mean()
# df["3day_rolling_total_sales"]=df["total_sales"].rolling(3,min_periods=1).sum()
#
# print(df.nlargest(1,"3day_rolling_average_sales"))
# print(df.nlargest(1,"7day_rolling_average_sales"))
# # Is sales performance improving?
# # yes
# # What happens if min_periods=1 is used?
# #the nan values become the columns value as it is
#
# df["previous_sale"]=df["sales_amount"].shift(1)
# df["next_sale"]=df["sales_amount"].shift(-1)
# df["sale_different%"]=df["previous_sale"]-df["next_sale"]
# print(df["previous_sale"].nlargest(1))
# print(df["sale_different%"].nlargest(1))
# print(df["sale_different%"].nsmallest(1))
#
# df["sales_growth_%"]=df["sales_amount"].pct_change()*100
# print(df.nlargest(1,"sales_growth_%"))
# print(df.nsmallest(1,"sales_growth_%"))
# print(df["sales_growth_%"].mean())
# print(df[df["sales_growth_%"]>0])
#
#
# df["running_total_sales"]=df["total_sales"].expanding().sum()
# df["running_average_sales"]=df["total_sales"].expanding().mean()
# df["running_max_sales"]=df["total_sales"].expanding().max()
# df["running_min_sales"]=df["total_sales"].expanding().min()
# print(df)
#
# print(df.nlargest(1,"running_total_sales"))
# print(df.nlargest(1,"running_average_sales"))
# # Day on which cumulative sales first crossed ₹100,000.i can not find this
#
# # year
# df["order_year"]=df["order_time"].dt.year
# df["order_month"]=df["order_time"].dt.month
# df["order_month_name"]=df["order_time"].dt.month_name()
# df["order_quarter"]=df["order_time"].dt.quarter
# df["order_day"]=df["order_time"].dt.day
# df["order_day_name"]=df["order_time"].dt.day_name()
# df["order_hour"]=df["order_time"].dt.hour
# df["order_weekday"]=df["order_time"].dt.weekday
# df["is_weekend"]=df["order_weekday"]>=5
# # Best month.
# # Best quarter.
# # above both can not find because of the month and quarter are january and 1
# print(df.groupby("order_weekday")["sales_amount"].sum().idxmax())
# print(df["is_weekend"].corr(df["order_weekday"])) #0.807330000740084
# print(df.groupby("order_hour")["sales_amount"].sum().idxmax())
#
# # i can not find the resample because of the data have for 1 month only
# print(df)
#
# df.to_excel("final_project_internship_done.xlsx",index=False)

#-------------------------------------------------------------------

# import numpy as np
# import pandas as pd

# df= pd.DataFrame(
#     {
#         "Employee": [
#             "  Rahul ",
#             "Neha",
#             "Amit",
#             "Priya",
#             "manthan",
#             "Khushbu",
#             "Jay",
#             "Riya",
#             "Amit",
#             "ANANYA",
#             "Vikram*",
#             None,
#         ],
#         "Department": [
#             "IT",
#             "I.T.",
#             "HR",
#             "Human Resources",
#             "Finance",
#             "FINANCE",
#             "Sales",
#             "sales",
#             "HR",
#             "IT",
#             "Marketing",
#             "Sales",
#         ],
#         "City": [
#             "Ahmedabad",
#             "Surat ",
#             "Ahmedabad",
#             "surat",
#             "Mumbai",
#             "mumbai",
#             "Ahmdabad",
#             "Surat",
#             "Ahmedabad",
#             "Delhi",
#             "Bangalore",
#             "Mumbai",
#         ],
#         "Skills": [
#             "Python,SQL,Excel",
#             "Python/Power BI",
#             "Excel;Tally",
#             "Python,Excel",
#             "Python, SQL",
#             "Excel,Power BI",
#             "Python,Excel,SQL",
#             "Power BI",
#             "Excel,Tally",
#             "Java,,SQL",
#             "SEO, Ads",
#             np.nan,
#         ],
#         "Sales": [
#             "1,00,000",
#             140000,
#             60000,
#             80000,
#             150000,
#             "180000",
#             120000,
#             -140000,
#             60000,
#             "95k",
#             200000,
#             0,
#         ],
#         "Target": [
#             90000,
#             130000,
#             70000,
#             75000,
#             140000,
#             160000,
#             110000,
#             150000,
#             70000,
#             100000,
#             np.nan,
#             50000,
#         ],
#         "Salary": [
#             60000,
#             80000,
#             55000,
#             60000,
#             90000,
#             110000,
#             75000,
#             95000,
#             55000,
#             "N/A",
#             120000,
#             45000,
#         ],
#         "Rating": [
#             4.2,
#             4.6,
#             3.2,
#             3.8,
#             4.8,
#             4.9,
#             4.1,
#             4.5,
#             3.2,
#             "four",
#             3.9,
#             52.0,
#         ],
#     }
# )

# # print(df.info())
# df.columns=df.columns.str.strip().str.lower()
# df=df.rename(columns={
#     "employee":"employee_name",
# })
# df["employee_name"]=df["employee_name"].str.strip().str.title().str.replace("*","").fillna("Unknown")
# df["department"]=df["department"].str.strip().str.title().str.replace(".","")
# df["department"]=df["department"].replace({
#     "It":"IT",
#     "Hr":"HR",
#     "Human Resources":"HR"
# }).astype("category")
# df["city"]=df["city"].str.strip().str.title().replace({
#     'Ahmdabad':'Ahmedabad',
# }).astype("category")
# df["skills"] = df["skills"].str.split(r"\s*[,;/]\s*")
# df=df.explode("skills")
# df["skills"]=df["skills"].str.replace({
#     "Ads":"ADS"
# }).fillna("Unknown").replace("", "Unknown")
# df["sales"]=df["sales"].replace({
#     '1,00,000':"100000",
#     "95k":"95000",
# })

# df["sales"]=df["sales"].astype("str").str.replace("-","")
# df["sales"]=pd.to_numeric(df["sales"],errors="coerce")
# df["target"]=df["target"].fillna(df["target"].median()).astype("int")
# df["salary"]=df["salary"].replace("N/A",np.nan).astype("float")
# df["salary"]=df["salary"].fillna(df["salary"].mean()).round(2)
# df["rating"]=df["rating"].astype("str").replace({
#     "four":np.nan,
#     "52.0":np.nan
#     }).astype("float")
# df["rating"]=df["rating"].fillna(df["rating"].mean()).round(2)
# df=df.drop_duplicates()
# # print(df.columns)
# # print(df.dtypes)
# # print(df.isna().sum())
# # print(df.duplicated().sum())
# df["achievement_%"]=df["sales"]/df["target"]*100
# df["target_status"]=np.where(df["achievement_%"]>=100,"Achieved","Not Achieved")
# df["department_average_sales"]=df.groupby("department")["sales"].transform("mean")
# df["department_salary_rank"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# print(df[["employee_name","salary"]])
# df["salary_category"]=pd.cut(df["salary"],bins=[0,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# print(df)
# df_1=df.groupby("department").filter(lambda x:x["sales"].mean()>100000 and x["rating"].mean()>=4)
# print(df_1)
# print(df["skills"].value_counts().idxmax())
# print(df["skills"].nunique())
# print(df["skills"].value_counts().nlargest(3)) #value_counts the sort by the large to small so top 3 is easy

# print(df.pivot_table(index="department",columns="city",values="sales",aggfunc="sum",fill_value=0))

# print(df.nlargest(2,"sales"))
# print(df.groupby("department")["sales"].sum().idxmax())
# print(df.nlargest(1,"achievement_%"))
# df=df.sort_values("sales",ascending=False)
# df["previous_sales"]=df["sales"].shift(1)
# df["sales_growth_%"]=df["sales"].pct_change()*100
# df["running_total_sales"]=df["sales"].expanding().mean()
# df["rolling_average_3days"]=df["sales"].rolling(3,min_periods=1).mean()
# print(df)
# print(df_1.nlargest(1,"salary"))
# df.to_excel("questions_16_8_final.xlsx",index=False)

#--------------------------------------------------------------


# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee": [
#         " Rahul ", "Neha", "Amit", "Priya",
#         "Manthan", "Khushbu", "Jay", "Riya"
#     ],
#     "Department": [
#         "IT", "I.T.", "HR", "Human Resources",
#         "Finance", "FINANCE", "Sales", "sales"
#     ],
#     "City": [
#         "Ahmedabad", "Surat ", "Ahmedabad", "surat",
#         "Mumbai", "mumbai", "Ahmdabad", "Surat"
#     ],
#     "Skills": [
#         "Python,SQL,Excel",
#         "Python/Power BI",
#         "Excel;Tally",
#         "Python,Excel",
#         "Python, SQL",
#         "Excel,Power BI",
#         "Python,Excel,SQL",
#         "Power BI"
#     ],
#     "Sales": [
#         "1,00,000", 140000, 60000, 80000,
#         150000, "180000", 120000, -140000
#     ],
#     "Target": [
#         90000, 130000, 70000, 75000,
#         140000, 160000, 110000, 150000
#     ],
#     "Salary": [
#         60000, 80000, 55000, 60000,
#         90000, 110000, 75000, 95000
#     ],
#     "Rating": [
#         4.2, 4.6, 3.2, 3.8,
#         4.8, 4.9, 4.1, 4.5
#     ]
# })
# # print(df.head())
# # print(df.tail())
# # print(df.info())
# # print(df.describe())
# # print(df.columns)
# # print(df.dtypes)
# # print(df.shape)
# # print(df.isna().sum())
# # print(df.duplicated().sum())

# df.columns=df.columns.str.strip().str.lower()
# df=df.rename(columns={
#     "employee":"employee_name",
# })
# df["employee_name"]=df["employee_name"].str.strip().str.title()
# df["department"]=df["department"].str.strip().str.title().replace({
#     "It":"IT",
#     "I.T.":"IT",
#     "Hr":"HR",
#     "Human Resources":"HR"
# })
# df["city"]=df["city"].str.strip().str.title().replace({
#     "Ahmdabad":"Ahmedabad"
# })
# df["skills"]=df["skills"].str.strip().str.title()
# df["skills"] = df["skills"].str.split(r"\s*[,;/]\s*")
# df=df.explode("skills")
# df["sales"]=df["sales"].astype(str).str.replace(",","").astype(int)
# df["sales"]=np.where(df["sales"]<0,0,df["sales"])
# print(df["sales"])
# print(df["skills"].value_counts().idxmax())
# print(df["skills"].value_counts().head(3))
# print(df["skills"].nunique())
# python_users=df.query("skills=='Python'")
# print(python_users)
# print(python_users["department"].value_counts().idxmax())
# df["achievement_%"]=df["sales"]/df["target"]*100
# df["target_status"]=np.where(df["achievement_%"]>=100,"Achieved","Not Achieved")
# print(df)
# print(df.where(df["achievement_%"]>=100))
# print(df.query("`achievement_%`>=100"))

# df["department_average_sales"]=df.groupby("department")["sales"].transform("mean")
# df["average_above"]=np.where(df["sales"]>df["department_average_sales"],"Above","Below")
# df["department_salary_rank"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# print(df.query("department_salary_rank==1"))
# df["salary_category"]=pd.cut(df["salary"],
#     bins=[0,75000,100000,float("inf")],
#     labels=["Low","Medium","High"]
#                              )
# print(df)
# filter_department=df.groupby("department").filter(lambda x:x["sales"].mean()>100000 and x["rating"].mean()>=4)
# print(filter_department)
# print(filter_department.nlargest(1,"salary"))
# print(df.pivot_table(index="department",columns="city",values="sales",aggfunc="sum",fill_value=0))

# sales_df=df.drop_duplicates(subset=["employee_name"])
# print(sales_df.nlargest(2,"sales"))
# print(df.nlargest(1,"achievement_%"))
# print(df.groupby("department")["sales"].sum().idxmax())
# print(df["skills"].value_counts().idxmax())
# print(df.nlargest(1,"salary"))


# monthly_sales = pd.Series(
#     [100000, 120000, 150000, 180000, 200000],
#     index=["Jan", "Feb", "Apr", "Jun", "Jul"]
# )
# monthly_sales=monthly_sales.reindex(index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],fill_value=0)
# print(monthly_sales)
# print(monthly_sales.sum())
# print(monthly_sales.idxmax())
# print(monthly_sales.expanding().sum())
# print(monthly_sales.rolling(3,min_periods=1).mean())

# try:
#     df.to_excel(
#     "final_pandas_revision_project_17_08.xlsx",
#     index=False
#     )
# except Exception as e:
#     print(e)

# 🐛 Debugging Challenge

# A junior developer writes:

# df["achievement_%"] = (
#     df["sales"] / df["target"] * 100
# )

# df["status"] = np.where(
#     df["achievement_%"] > 100,
#     "Achieved",
#     "Not Achieved"
# )

# Find the business logic error.

# An employee with exactly 100% achievement should be considered successful.

# Fix the code:
# df["achievement_%"] = (
#     df["sales"] / df["target"] * 100
# )

# df["status"] = np.where(
#     df["achievement_%"] >= 100,
#     "Achieved",
#     "Not Achieved"
# )
# 🔎 Trace Challenge

# Predict the result:

# s = pd.Series(
#     [100, 200, 300],
#     index=["Jan", "Mar", "May"]
# )

# result = s.reindex(
#     ["Jan", "Feb", "Mar", "Apr", "May"],
#     method="ffill"
# )

# print(result)

# What are the values of:

# Feb:100
# Apr:200


# 🧠 Thinking Question

# You have an employee whose:

# Sales = 0
# Target = 100000

# Should the company classify this employee as:

# Achieved

# or

# Not Achieved

# and why?
# not achieved because of the because of it is negitive then you convert in to the 0 so not achieved

#-----------------------------------------------------------------------------
import pandas as pd
import numpy as np
try:
    df=pd.read_csv("messy_data_practice_17_08.csv")
except Exception as e:
    print(e)
print(df.head())
print(df.tail())
print(df.sample(10))
print(df.info())
print(df.columns)
print(df.dtypes)
print(df.isna().sum())
print(df.duplicated().sum())
df["name"]=df["name"].str.strip().str.title()
df["age"]=pd.to_numeric(df["age"],errors="coerce")
df["age"]=np.where(df["age"]>100,np.nan,df["age"])
df["age"]=df["age"].fillna(df["age"].mean()).astype(int)
df["gender"]=df["gender"].str.strip().str.title().replace({
    "M":"Male",
    "F":"Female"
})
df["city"]=df["city"].str.strip().str.title()
df["email"]=df["email"].str.strip().str.lower().replace({
      'isha@gmail':"isha@gmail.com",
      'rahul@gmail':"rahul@gmail.com"
}).fillna("Unkonwn")
df["phone"]=df["phone"].str.strip().str.replace(" ","")
df["phone"]=pd.to_numeric(df["phone"],errors="coerce")
df["phone"]=df["phone"].fillna(df["phone"].median()).astype(int)
df["purchase_date"]=pd.to_datetime(df["purchase_date"],format="mixed")
df["quantity"]=df["quantity"].fillna(0)
df["quantity"]=np.where(df["quantity"]<0,0,df["quantity"]).astype("int")
df["price"]=df["price"].str.strip().str.replace(",","").astype("float")
df["total_amount"]=df["total_amount"].str.strip().str.replace(",","")
df["total_amount"]=pd.to_numeric(df["total_amount"],errors="coerce")
df["total_amount"]=np.where(df["total_amount"]<0,0,df["total_amount"])
df["total_amount"]=df["total_amount"].fillna(df["total_amount"].mean())
df["payment_method"]=df["payment_method"].str.strip().str.title()
df["returned"]=df["returned"].str.strip().str.title().replace({
    "N":"No",
    "Y":"Yes"
})
print(df)
df.to_excel("practice_final_17_8.xlsx",index=False)