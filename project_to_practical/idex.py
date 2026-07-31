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





