import numpy as np
import pandas as pd

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

#1

# try:
#     df=pd.read_excel("employees.xlsx")
# except Exception as e:
#     print(e)
#
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
#
# #2
# df=pd.read_excel("employees.xlsx"
#                  ,usecols=["Employee ID","First Name","Last Name","Salary"])
# print(df)
#
# #3
# df=pd.read_excel("employees.xlsx",nrows=5)
# print(df)

#4

# df = pd.read_excel("workbook_1.xlsx", sheet_name="salary")
# print(df)

#5

# df=pd.ExcelFile("workbook_1.xlsx")
# print(df.sheet_names)

#6
# df = pd.read_excel("workbook_1.xlsx", sheet_name=None)
# print(df.keys())
# employees=df["employees"]
# salary=df["salary"]
# print(df["Performance"])

#7
# print(employees)
# print(salary)
# df=pd.merge(employees,salary,on="Emp ID",how="inner")
# print(df)
#8
# print(df.isna().sum())
# print(df.dtypes)
# df["Basic Salary"]=df["Basic Salary"].str.replace("₹","").str.replace(",","").astype(float)
#
# print(df.dtypes)
# df["Basic Salary"]=df["Basic Salary"].fillna(df["Basic Salary"].median())
# df["Bonus"]=df["Basic Salary"]*10/100
# df["Final Salary"]=df["Bonus"]+df["Basic Salary"]
# print(df)
#9
# print(df.groupby("Department")["Basic Salary"].agg(["mean","max","min","count"]))
# 10
# df.to_excel("employee_analysis.xlsx",index=False,sheet_name=cleandata)

#bonus 1

# try:
#     excelsheet=pd.read_excel('monthly_sales.xlsx',sheet_name=None)
#     print(excelsheet.keys())
# except Exception as e:
#     print(e)

# jan=excelsheet["January"]
# feb=excelsheet["February"]
# mar=excelsheet["March"]

# print(jan)
# print(feb)
# print(mar)

# df=pd.concat([jan,feb,mar],ignore_index=True)
# print(df)

# print(df.isna().sum())

# df["Sales"]=df["Sales"].fillna(0) #i fill with zero(0) because of some sales are high and low so not accurate median or mean 
# print(df)

# total_sales=df["Sales"].sum()
# print(total_sales)

# av_sales=df["Sales"].mean()
# print(av_sales)

# top_5_sales=df.sort_values("Sales",ascending=False).head()
# print(top_5_sales)

# category_wise_sales=df.groupby("Category")["Sales"].sum()
# print(category_wise_sales)

# city_sales=df.groupby("City")["Sales"].mean()
# print(city_sales)

# pivot_table1=df.pivot_table(index="Category", columns="City",values="Sales")
# print(pivot_table1)

# summary_df = pd.DataFrame({
#     "Metric": [
#         "Total Sales", 
#         "Average Sales", 
#         "Top 5 Sales", 
#         "Category-wise Total Sales", 
#         "City-wise Average Sales",  
#         "Pivot Table Layout"
#     ],
#     "Result": [
#         total_sales, 
#         av_sales, 
#         str(top_5_sales),   
#         str(category_wise_sales), 
#         str(city_sales), 
#         "See 'Pivot Sheet' below" 
#     ]
# })
# with pd.ExcelWriter("sales_analysis.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Clean Data", index=False)
#     summary_df.to_excel(writer, sheet_name="Summary", index=False)
    
#     pivot_table1.to_excel(writer, sheet_name="Pivot Analysis")


#bonus2

# try:
#     excel_sheets=pd.read_excel("company.xlsx",sheet_name=None)
#     print(excel_sheets.keys())
# except Exception as e:
#     print(e)

# employees=excel_sheets["Employees"]
# salary=excel_sheets["Salary"]
# performance=excel_sheets["Performance"]
# print(employees.info())
# print(salary.info())
# print(performance.info())

# df_1=pd.merge(employees,salary,on="Employee ID",how="inner")
# df=pd.merge(df_1,performance,on="Employee ID",how="inner")
# print(df)

# df["Bonus"]=df["Salary"]*10/100
# df["Final Salary"]=df["Salary"]+df["Bonus"]
# mapping={
#     5:"Excellent",
#     4:"Very Good",
#     3:"Good",
#     2:"Average",
#     1:"Poor"
# }
# df["Performance Category"]=df["Performance"].map(mapping)
# print(df)
# department_wise_Data=df.groupby("Department")["Salary"].agg(["mean","max","min","count","sum"])
# print(department_wise_Data)

# with pd.ExcelWriter("company_final_report.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Employee Report", index=False)
#     department_wise_Data.to_excel(writer, sheet_name="Summary", index=False)

#mixed1

# try:
#     df=pd.read_excel("dirty_source_data.xlsx")
# except Exception as e:
#     print(e)

# print(df.info())

# df=df.rename(columns={
#     "old_store_id":"store_id",
#     "Transaction Date":"transaction_date",
#     "revenue_amount":"amount",
#     "Category_Name":"category_name",
# })

# print(df.columns)

# print(df)
# print(df.dtypes)

# df["store_id"]=df["store_id"].str.strip().str.upper()
# df["transaction_date"]=pd.to_datetime(df["transaction_date"],format="mixed")
# df["category_name"]=df["category_name"].str.strip()
# print(df)
# print(df.dtypes)
# print(df.isna().sum())
# df["transaction_date"]=df["transaction_date"].fillna("Not Found")
# print(df.isna().sum())
# print(df.groupby("category_name")["amount"].agg(["mean","max","min","sum","count"]))
# df.to_excel("good_source_data.xlsx",index=False)

#mixed2

# try:
#     excel=pd.read_excel("workbook_2.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)

# customers=excel["Customers"]
# orders=excel["Orders"]

# print(customers.info())
# print(orders.info())

# df=pd.merge(customers,orders,on="CustomerID",how="inner")
# print(df.info())
# df["Discount%"]=df["Membership"].apply(lambda x:10 if x=="Gold" else(5 if x=="Silver" else 3))
# df["Discount Amount"]=df["Price"]*df["Discount%"]/100
# df["Final Price"]=df["Price"]-df["Discount Amount"]
# print(df)
# print(df["City"].value_counts())
# print(df["City"].unique())
# print(df["City"].nunique())
# print(df["Membership"].unique())
# print(df["Membership"].nunique())

# print(df.sort_values(["Membership","City"]))
# print(df.pivot_table(values="Final Price",index="City",columns="Membership",fill_value=0,aggfunc="sum"))

# df.to_excel("workbook_2_clean.xlsx",index=False)

#mixed3

# try:
#     excel=pd.read_excel("workbook_3.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)


# jan=excel["January"]
# feb=excel["February"]
# mar=excel["March"]

# df=pd.concat([jan,feb,mar],ignore_index=True)
# print(df.info())
# #no needs to change the date and time

# groupby_product_Quantity=df.groupby("Product")["Quantity"].agg(["min","max","mean","sum","count"])
# print(groupby_product_Quantity)

# groupby_product_UnitPrice=df.groupby("Product")["Unit Price"].agg(["min","max","mean","sum","count"])
# print(groupby_product_UnitPrice)

# groupby_product_sales=df.groupby("Product")["Sales"].agg(["min","max","mean","sum","count"])
# print(groupby_product_sales)

# groupby_city_sales=df.groupby("City")["Sales"].agg(["min","max","mean","sum","count"])
# print(groupby_city_sales)

# groupby_category_sales=df.groupby("Category")["Sales"].agg(["min","max","mean","sum","count"])
# print(groupby_category_sales)

# groupby_paymentmode_sales=df.groupby("Payment Mode")["Sales"].agg(["min","max","mean","sum","count"])
# print(groupby_paymentmode_sales)

# print(df)
# crosstab_sales=pd.crosstab(index=df["City"],columns=df["Payment Mode"])
# print(crosstab_sales)

# pivot_table_sales=df.pivot_table(index="Category",columns="Product",values="Sales",aggfunc="mean",fill_value=0)
# print(pivot_table_sales)

# nlargest_sales=df["Sales"].nlargest(5)
# print(nlargest_sales)

# summary_df=pd.DataFrame({
#     "Top 5 Sales":nlargest_sales
# })

# with pd.ExcelWriter("sales_final_report.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Clean Sales", index=False)
#     summary_df.to_excel(writer, sheet_name="Sales Summary", index=False)


# # Interview Challenge
# import numpy as np
# try:
#     excel=pd.read_excel("company_data.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)

# employees=excel["Employees"]
# salary=excel["Salary"]
# performance=excel["Performance"]

# # print(employees.info())
# # print(salary.info())
# # print(performance.info())

# df_1=pd.merge(employees,salary,on="EmpID",how="inner")
# df=pd.merge(df_1,performance,on="EmpID",how="inner")
# print(df)
# df.columns=df.columns.str.strip().str.lower()
# df["name"]=df["name"].str.strip().str.title()
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["joiningdate"]=pd.to_datetime(df["joiningdate"])
# df["joiningyear"]=df["joiningdate"].dt.year
# df["bonus"]=df["salary"]*10/100
# df["final salary"]=df["salary"]+df["bonus"]
# df["performance"]=np.random.randint(1,6,15)
# mapping={
#     5:"Excellent",
#     4:"Good",
#     3:"Average",
#     2:"Low",
#     1:"Poor"
# }
# df["grades"]=df["performance"].map(mapping)
# print(df)
# print(df.groupby("department")["salary"].mean())

# top_5_highestpaid_employees=df[['name', 'salary']].sort_values(by='salary', ascending=False).head(5)
# print(top_5_highestpaid_employees)

# department_city_wise_average_salary=df.pivot_table(values="salary",index="department",columns="city",aggfunc="mean",fill_value=0)
# print(department_city_wise_average_salary)

# Department_PerformanceGrade_crosstable=pd.crosstab(index=df["department"],columns=df["grades"])
# print(Department_PerformanceGrade_crosstable)

# summary_df = pd.DataFrame({
#     "Top 5 Highest Paid Employees": [top_5_highestpaid_employees]
# })
# with pd.ExcelWriter("company_analysis.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Clean Employee Data", index=False)
#     summary_df.to_excel(writer, sheet_name="Summary", index=False)
#     department_city_wise_average_salary.to_excel(writer, sheet_name="Department Summary", index=False)
#     Department_PerformanceGrade_crosstable.to_excel(writer, sheet_name="Department Summary1", index=False)

#mentor

# try:
#     excel=pd.read_excel("ecommerce_2026.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)

# customers=excel['Customers']
# products=excel["Products"]
# o_q1=excel["Orders_Q1"]
# o_q2=excel["Orders_Q2"]

# # print(o_q1.info())
# # print(o_q2.info())
# # print(customers.info())
# # print(products.info())

# orders=pd.concat([o_q1,o_q2])
# df_1=pd.merge(customers,orders,how="inner")
# df=pd.merge(df_1,products,how="inner")
# print(df)
# print(df.columns)
# print(df.dtypes)

# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.columns)
# #no needs to clean our customer name and no needs to rename columns and no needs to change the datatypes and no needs to chnage date datatype
# print(df.isna().sum()) #no needs to fill any values
# print(df.dtypes)
# df["total_amount"]=df["quantity"]*df["unit_price"]
# df["discount_amount"]=df["total_amount"]*df["discount%"]/100
# df["net_sales"]=df["total_amount"]-df["discount_amount"]
# df["month_name"]=df["join_date"].dt.month_name()
# df["quarter"]=df["join_date"].dt.quarter
# print(df)
# print(df.groupby("city")["total_amount"].agg(["mean","max","min","sum","count"]))
# print(df.groupby("category")["total_amount"].agg(["mean","max","min","sum","count"]))
# print(df.groupby("payment_mode")["total_amount"].agg(["mean","max","min","sum","count"]))
# print(df.columns)
# top_customerd=df["total_amount"].idxmax()
# top_customer=df.loc[top_customerd]
# print(top_customer)
# top_product=df.groupby("product_name")["total_amount"].sum().idxmax()
# print(top_product)
# print(df["city"].value_counts())
# print(df["product_name"].unique())
# print(df["state"].nunique())
# print(df.pivot_table(values="total_amount",index="state",columns="city",aggfunc="sum",fill_value=0))
# print(pd.crosstab(index=df["city"],columns=df["product_name"]))

# summary_df=pd.DataFrame({
#     "Top_customer":[top_customer],
#     "Top_product":top_product
# })
# #i did not answer the 5 5 business questions and not 
# with pd.ExcelWriter("ecommerce_2026_analysis.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Clean Data", index=False)
#     summary_df.to_excel(writer, sheet_name="Summary", index=False)

#-----------------------------------------------------------------
# df = pd.DataFrame({
#     "EmpID":[101,102,103,104,105,106],
#     "Name":["Rahul","Neha","Amit","Priya","Manthan","Karan"],
#     "Department":["IT","HR","IT","Sales","Finance","HR"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Rajkot","Vadodara","Surat"],
#     "Salary":[50000,60000,55000,70000,65000,62000],
#     "Temp_Code":["A","B","C","D","E","F"],
#     "Internal_ID":[9001,9002,9003,9004,9005,9006]
# })
#1
# df=df.drop(columns="Temp_Code")
# print(df)
#2
# df=df.drop(columns=["Temp_Code","Internal_ID"])
# print(df)
#3
# df=df.drop(index=2)
# print(df)
#4
# df=df.drop(index=[1,4])
# print(df)
#5
# df=df.drop("City",axis=1)
# print(df)
#6
# df=df.drop(3,axis=0)
# print(df)
#7
# df.drop(columns="Internal_ID",inplace=True)
# print(df)
#8
# df=df.drop(columns="Email",errors="ignore") #remove the errors so program give the errors because email can not exists
# print(df)
#9
# print(df[df["Salary"]>55000].reset_index())
#10
# df=df.drop(columns="Temp_Code")
# df=df.sort_values("Salary",ascending=False)
# print(df)

#bonus1
# data = {
#     "CustomerID": [101, 102, 103, 104, 105],
#     "CustomerName": ["Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince", "Evan Wright"],
#     "Email": ["alice@email.com", "bob@email.com", "charlie@email.com", "diana@email.com", "evan@email.com"],
#     "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"],
#     "Purchase": [9300, 7500, 4000, 6000, 1200],
#     "Internal_Code": ["INT-001", "INT-002", "INT-003", "INT-004", "INT-005"],
#     "Temporary_Flag": [True, False, False, True, False]
# }

# df=pd.DataFrame(data)
# df=df.drop(columns=["Internal_Code","Temporary_Flag"])

# df=df.sort_values("Purchase",ascending=False)
# print(df)
# try:
#     df.to_csv("bonus_1_drop.csv")
#     print("Done")
# except Exception as e:
#     print(e)

#bonus2
# try:
#     df=pd.read_csv("bonus_2_drop_question.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# df=df.drop(columns=["Temp_ID","Internal_Remark"])
# df["Bonus"]=df["Salary"]*10/100
# df["Final Salary"]=df["Bonus"]+df["Salary"]
# print(df)
# department_wise_average_salary=df.groupby("Department")["Salary"].mean()
# print(department_wise_average_salary)
# summary_df=pd.DataFrame({
#     "Department Wise Average Salary":[department_wise_average_salary]
# })

# with pd.ExcelWriter("bonus_2_drop_final.xlsx") as writer:
#      df.to_excel(writer, sheet_name="Clean Data", index=False)
#      summary_df.to_excel(writer, sheet_name="Summary", index=False)

#mixed1

# try:
#     df=pd.read_csv("mixed_1_drop_question.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# df=df.drop(columns=["Temp_ID","Internal_Remark"])
# df.columns=df.columns.str.strip().str.lower()

# print(df.isna().sum())
# df["department"]=df["department"].fillna("Not Found")
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["city"]=df["city"].fillna("Not Found")
# print(df)
# #no needs to astype()
# print(df.groupby(["city","department"])["salary"].sum())
# df=df.sort_values("salary",ascending=False)
# df.to_csv("mixed_1_dropfinal.csv")

#mixed2
# try:
#     excel=pd.read_excel("workbook_4.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)

# orders=excel["Orders"]
# customers=excel["Customers"]

# df=pd.merge(orders,customers,on="CustomerID",how="inner")
# print(df)   #i can not cannot because data is not like use for concat
# df=df.drop(columns=["Internal_Tracking_ID","Internal_Risk_Score"])
# print(df)
# print(df.columns)
# print(df.dtypes) #no needs to change the datetime and datatype
# df["Amount Category"]=df["Amount"].apply(lambda x:"High" if x>1000 else("Average" if x>=500  else "Low"))
# print(df)
# print(df["Region"].value_counts())
# print(df.pivot_table(index="CustomerName",columns="Region",values="Amount",aggfunc="sum",fill_value=0))
# df.to_excel("workbook_4_final.xlsx")

#mixed3

# try:
#     excel=pd.read_excel("workbook_5.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)

# jan=excel["January"]
# feb=excel["February"]
# mar=excel["March"]

# df=pd.concat([jan,feb,mar],ignore_index=True)
# df=df.drop(columns=["Internal_Tracking_ID","Remarks"])
# print(df)
# print(df.groupby("Product")["Amount"].mean())
# print(pd.crosstab(index=df["Product"],columns=df["Month"],values=df["Amount"],aggfunc="sum"))
# print(df.pivot_table(index="Month",columns="Product",values="Amount",aggfunc="mean"))

# Interview Challenge

# try:
#     df=pd.read_csv("employee_analysis.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# print(df.columns)
# print(df.dtypes)

# df.columns=df.columns.str.strip().str.lower()
# print(df.columns)
# df["name"]=df["name"].str.strip().str.title()
# print(df)
# print(df.dtypes)
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["joiningdate"]=pd.to_datetime(df["joiningdate"])
# print(df.dtypes)
# df=df.drop(columns=["internal_code","temporary_id","admin_remark"])
# df["bonus"]=df["salary"]*10/100
# df["final_salary"]=df["salary"]+df["bonus"]
# performancemapping={
#     "Excellent":1,
#     "Good":2,
#     "Average":3
# }
# df["Performance Grade"]=df["performance"].map(performancemapping)
# print(df)
# print(df.sort_values("final_salary", ascending=False)[["name", "salary"]].head(5).reset_index(drop=True))
# print(df.groupby("department")["salary"].mean())
# print(df.pivot_table(index="department",values="salary",columns="city",aggfunc="mean",fill_value=0))
# df.to_csv("Interview_Challenge_final_drop.csv")


# #mentor challenge
#
# try:
#     customer=pd.read_csv("customers_drop.csv")
#     product=pd.read_csv("products_drop.csv")
#     order=pd.read_csv("orders_drop.csv")
# except Exception as e:
#     print(e)
#
# # print(customer.info())
# # print(product.info())
# # print(order.info())
#
# # print(customer.describe())
# # print(product.describe())
# # print(order.describe())
#
# # print(customer.columns)
# # print(product.columns)
# # print(order.columns)
#
#
# df_1=pd.merge(customer,order,on="customer_id",how="inner")
# df=pd.merge(df_1,product,on="product_id",how="inner")
#
# print(df.columns)
#
# df=df.drop_duplicates()
#
# df=df.drop(columns=["internal_code","temp_col","internal_id"])
# df["gender"]=df["gender"].fillna("Not defined")
# df["signup_date"]=pd.to_datetime(df["signup_date"],format='mixed',errors='coerce')
# df["signup_date"]=df["signup_date"].fillna(df["signup_date"].mean())
# df["age"]= pd.to_numeric(df["age"], errors="coerce")
# df["age"]=df["age"].fillna(df["age"].mean()).astype(int)
# df["email"]=df["email"].fillna("Not Found")
# df["quantity"]=df["quantity"].fillna(df["quantity"].mean()).astype(int)
# df["order_date"]=pd.to_datetime(df["order_date"],format='mixed',errors='coerce')
# df["order_date"]=df["order_date"].fillna(df["order_date"].mean())
# df["status"]=df["status"].fillna("Not Found")
# df["price"]= pd.to_numeric(df["price"], errors="coerce")
# df["price"]=df["price"].fillna(df["price"].mean())
# df["stock"]=df["stock"].fillna(df["stock"].mean()).astype(int)
# print(df.dtypes)
# print(df.isna().sum())
# df.columns=df.columns.str.strip().str.title()
# print(df.columns)
# df["Full_Name"]=df["Full_Name"].str.strip().str.title()
# df["Product_Name"]=df["Product_Name"].str.strip().str.title()
# df["Order_Amount"]=df["Quantity"]*df["Price"]
# marks_gender_mapping={
#     "Female":0,
#     "Male":1,
#     "Not defined":-1
# }
# df["Gender Marks"]=df["Gender"].map(marks_gender_mapping)
# df["Order Value"]=df["Order_Amount"].apply(lambda x:"High" if x>400 else "low")
# print(df)
# order_value_by_city=df["City"].value_counts()
# print(order_value_by_city)
# df["Category"]=df["Category"].str.strip().str.title()
# unique_category=df["Category"].unique()
# print(unique_category)
# count_of_payment_mode=df["Payment_Method"].nunique()
# print(count_of_payment_mode)
# print(df.groupby("Category")["Order_Amount"].sum())
# print(df.sort_values("Stock"))
# paymentmode_category_pivot_table=df.pivot_table(index="Payment_Method",columns="Category",values="Order_Amount",aggfunc="sum",fill_value=0,margins=True,margins_name="Total")
# print(paymentmode_category_pivot_table)
# print(pd.crosstab(index=df["City"],columns=df["Gender"]))
# df=df.set_index("Customer_Id")
# df=df.reset_index()
# print(df)
# highest_order_amount=df.loc[df["Order_Amount"].argmax()]
# print(highest_order_amount)
# lowest_order_amount=df.loc[df["Order_Amount"].argmin()]
# print(lowest_order_amount)
# print(df.iloc[df["Customer_Id"]==102])
# print(df.iloc[:,[1,3]])
#
# summary_df = pd.DataFrame({
#     "Metric Name": [
#         "ORDER COUNT BY CITIES",
#         "NAME OF UNIQUE CATEGORY",
#         "COUNT OF UNIQUE PAYMENT MODE"
#     ],
#     "Value": [
#         order_value_by_city,
#         unique_category,
#         count_of_payment_mode
#     ]
# })
#
#
#
# try:
#         with pd.ExcelWriter("ecommerce_clean_report_drop.xlsx") as writer:
#             df.to_excel(writer, sheet_name="Clean Data", index=False)
#             summary_df.to_excel(writer, sheet_name="Summary", index=False)
#             paymentmode_category_pivot_table.to_excel(writer, sheet_name="Pivot_table", index=False)
# except Exception as e:
#     print(e)


#practicalreal

# try:
#     df=pd.read_excel('employee1.xlsx')
# except Exception as e:
#     print(e)

# print(df.info())
# print(df.columns)
# print(df.dtypes)

# df["Name"]=df["Name"].str.strip().str.title().str.replace(",","")
# df["Years"]=df["Years"].fillna(df["Years"].median()).astype(int)

# mapping_gender={
#     "M":"Male",
#     "W":"Female"
# }

# df["Gender"]=df["Gender"].map(mapping_gender)
# mapping_department={
#     "ADMN":"Admin",
#     "SALE":"Sales",
#     "FINC":"Finance",
#     "MKTG":"Marketing",
#     "ACCT":"Accounting",
# }
# df["Dept"]=df["Dept"].map(mapping_department)
# df=df.rename(columns={
#     "Dept":"Department",
#     "JobSat":"Job Status"
# })
# df["Department"]=df["Department"].fillna("Unknown")
# print(df.columns)
# print(df.isna().sum())
# print(df.dtypes)
# print(df["Salary"])
# df["Job Status"]=df["Job Status"].str.strip().str.title().fillna("Unknown")
# print(df["Job Status"])
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df)
# df.to_excel("employee1_final.xlsx",index=False)

#------------------------------------------------------------------------------------
# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Karan","Riya"],
#     "Department":["IT","HR","Information Tech","Sales","Human Resource","IT"],
#     "City":["Ahd","Surat","Ahmedabad","Mum","Mumbai","Ahd"],
#     "Gender":["M","F","M","F","Unknown","M"],
#     "Status":[1,1,0,1,0,1],
#     "Salary":[50000,60000,55000,70000,65000,58000]
# })
# df["City"]=df["City"].replace({
#         "Ahd":"Ahmedabad",
#          "Mum":"Mumbai"
# })
# df["Department"]=df["Department"].replace({
#         "Information Tech":"IT",
#         "Human Resource":"HR"
# })
# df["Gender"]=df["Gender"].replace({
#         "M":"Male",
#         "F":"Female"
# })
# df["Status"]=df["Status"].replace({
#     1 :"Active",
#     0 :"Inactive"
# })
# # department_mapping={
# #      "Information Tech":"IT",
# #      "Human Resource":"HR",
# # }
# # df["Department"]=df["Department"].map(department_mapping) #observation says other options are become Nan
# # print(df)

# print(df["Department"].count)
# print(df["Department"].nunique())

# Bonus 1

# df = pd.DataFrame({
#     "City":[
#         "Ahd","Ahmedabad","Mum",
#         "Mumbai","Del","Delhi",
#         "Ahd","Mum"
#     ]
# })
# df["City"]=df["City"].replace({
#     "Ahd":"Ahmedabad",
#     "Mum":"Mumbai",
#     "Del":"Delhi"
# })
# print(df["City"].value_counts())

# Bonus 2
# import numpy as np

# df = pd.DataFrame({
#     "Product":["Laptop","Mouse","Keyboard","Monitor"],
#     "Stock":["25","N/A","-","40"],
#     "Price":[1200,25,75,300]
# })
# df["Stock"]=df["Stock"].replace({
#     "N/A":np.nan,
#     "-":np.nan
# })
# print(df.dtypes)
# df["Stock"]=pd.to_numeric(df["Stock"],errors="coerce")
# df["Stock"]=df["Stock"].fillna(0).astype(int)
# print(df.dtypes)

#mixed1

# try:
#     df=pd.read_csv("mixed1_replace.csv")
# except Exception as e:
#     print(e)
# print(df.info())
# print(df.columns)
# print(df.dtypes)
# print(df.isna().sum())

# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.columns)
# df["department"]=df["department"].replace({
#     "HR":"Human Resource",
#     "IT":"Information Technology"
# })
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["age"]=df["age"].fillna(df["age"].mean()).astype(int)
# df["city"]=df["city"].fillna("Unknown")
# print(df)
# print(df.groupby("department")["salary"].sum())
# print(df.groupby("city")["salary"].mean())
# df=df.sort_values("salary",ascending=False)
# df.to_csv("mixed1_replace_final_csv")

#mixed2
# import pandas as pd

# df = pd.DataFrame({
#     "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
#     "Name": [
#         "Alice", "Bob", "Charlie", "David", "Eva", "Frank",
#         "Grace", "Helen", "Ian", "Jack", "Karen", "Leo"
#     ],
#     "Department": [
#         "HR", "hr", "Human Resources", "IT", "it", "Information Technology",
#         "Sales", "sales", "SALES", "Finance", "finance", "FIN"
#     ],
#     "City": [
#         "New York", "new york", "NY", "Chicago", "chicago", "CHICAGO",
#         "Los Angeles", "los angeles", "LA", "Houston", "houston", "HOU"
#     ],
#     "Gender": [
#         "Male", "M", "male", "Female", "F", "female",
#         "MALE", "FEMALE", "m", "f", "Male", "Female"
#     ],
#     "Salary": [
#         55000, 60000, 58000, 72000, 71000, 75000,
#         50000, 52000, 51000, 68000, 69000, 70000
#     ]
# })
# df["Department"]=df["Department"].str.strip().str.title().replace({
#     "Hr":"Human Resources",
#     "It":"Information Technology",
#     "Fin":"Finance"
# })
# df["City"]=df["City"].str.strip().str.title().replace({
#     "Ny":"New York",
#     "La":"Los Angeles",
#     "Hou":"Houston"
# })
# df["Gender"]=df["Gender"].str.strip().str.title().replace({
#     "M":"Male",
#     "F":"Female"
# })
# print(df)
# print(df["Department"].value_counts())
# print(df.groupby("City")["Salary"].sum())
# print(df.pivot_table(values="Salary",index="City",columns="Gender",margins=True,margins_name="Total",fill_value=0))

#mixed3
# try:
#     df=pd.read_excel("mixed3_replace.xlsx")
# except Exception as e:
#     print(e)

# print(df.info())
# print(df.columns)
# print(df.dtypes)

# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df["category"].unique())
# df["category"]=df["category"].str.title().replace({
#     "Electronics":"Electronic",
#     "Cloth":"Clothing",
#     "Groceries":"Grocery"
# })
# print(df["category"].unique())
# print(df.isna().sum())
# df["discount"]=df["discount"].fillna(0) #because some product does not have any discount
# df["net_sales"]=df["quantity"]*df["unit_price"]-df["discount"]
# print(df)
# print(df.groupby("category")["quantity"].sum())
# print(pd.crosstab(index=df["city"],columns=df["payment_mode"],normalize=True)*100)
# df.to_excel("mixed3_replace_final.xlsx")

#-----------------------------------------------------------

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan",
#                 "Khushbu","Tirth","Aastha","Jay","Riya"],
    
#     "Department":["IT","HR","IT","Sales","Finance",
#                   "IT","HR","Finance","Sales","IT"],
    
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai","Surat",
#             "Ahmedabad","Mumbai","Ahmedabad","Surat","Mumbai"],
    
#     "Age":[25,30,28,35,24,27,32,26,29,31],
    
#     "Salary":[50000,65000,58000,72000,60000,
#               75000,55000,68000,62000,80000],
    
#     "Experience":[2,5,4,8,2,5,6,3,4,7]
# })

# print(df.query("Salary >60000"))
# print(df.query("Department=='IT'"))
# print(df.query('City=="Ahmedabad"'))
# print(df.query("Age>=25 and Age<=30"))
# print(df.query("Department=='IT' and Salary>55000 "))
# print(df.query("City=='Ahmedabad' or City=='Surat'"))
# print(df.query("Department in ['IT','Finance']"))
# print(df.query("Experience >= 5 and Salary >= 65000"))
# salary_limit = 70000
# print(df.query("Salary >=@salary_limit"))
# print(df.query("Department=='IT'").sort_values("Salary",ascending=False).head(3))

# min_age = 25
# max_age = 30
# min_salary = 55000

# print(df.query("Age >= @min_age and Age <= @max_age and Salary >= @min_salary"))

# df["Salary_Category"] = df["Salary"].apply(
#     lambda x: "High" if x >= 65000 else "Normal"
# )
# print(df)
# print(df.query("Salary_Category=='High'"))
# print(df.query("Salary_Category=='High' and City=='Ahmedabad'"))
# department_it_high=df.query("Salary_Category=='High' and Department=='IT'")
# print(department_it_high)
# print(department_it_high.sort_values("Salary",ascending=False))

#mixed1

# try:
#     df=pd.read_csv("mixed1_query.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# print(df.columns)
# print(df.dtypes)

# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.columns)
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["city"]=df["city"].fillna("Unknown")
# print(df.isna().sum())
# #do not needs to change the astype
# print(df["department"].unique())
# df["department"]=df["department"].replace({
#     "Information Technology":"IT",
#     "Human Resources":"HR"
# })
# print(df["department"].unique())
# print(df)
# print(df.query("department !='Finance'"))
# print(df.groupby("department")["salary"].sum())
# minimum_salary=70000
# print(df.query("salary >=@minimum_salary").sort_values("salary",ascending=False))
# print(df.query("salary>60000").groupby("department")["salary"].mean())

#mixed2

# try:
#     emp=pd.read_csv("mixed2_query_emp.csv")
#     salary=pd.read_csv("mixed2_query_salary.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(salary.info())

# df=pd.merge(emp,salary,on="EmpID",how="inner")
# print(df)

# df["City"]=df["City"].fillna("Unknown")
# df["Salary"]=df["Salary"].fillna(df["Salary"].median())
# df["Bonus"]=df["Bonus"].fillna(0) # if some dispiut bonus not given
# print(df.isna().sum())
# print(df.query("Bonus>5000"))
# print(df["City"].value_counts())
# print(df.groupby("Department")["Salary"].sum())
# print(df.pivot_table(values="Salary",index="City",columns="Department",aggfunc="mean",fill_value=0))
# print(df.query("Salary>60000"))
# print(df.query("Experience>=3"))
# print(df.query("Salary>60000 and Experience>=3"))

# #mixed3
# try:
#     df=pd.read_excel("mixed3_query.xlsx")
# except Exception as e:
#     print(e)
#
# print(df.info())
# print(df.columns)
# print(df.dtypes)
# df["OrderDate"]=pd.to_datetime(df["OrderDate"],format="mixed")
# print(df.dtypes)
# df["Discount"]=df["Discount"].fillna(0)
# df["PaymentMode"]=df["PaymentMode"].fillna("Unknown")
# print(df)
# print(df["OrderStatus"].unique())
# df["OrderStatus"]=df["OrderStatus"].replace({
#     "Complete":"Completed"
# })
# print(df["OrderStatus"].unique())
# print(df.query("PaymentMode=='UPI'"))
# print(df.groupby("Category")["NetSales"].sum())
# print(df.pivot_table(values="NetSales",index="Region",columns="Category",aggfunc=sum,fill_value=0))
# print(pd.crosstab(df["Region"],df["Category"],values=df["NetSales"],normalize=True,aggfunc=sum)*100)
# print(df.query("OrderStatus=='Completed'"))
# df.to_excel("mixed3_query_final.xlsx")
# print(df.query("NetSales>1000"))
# print(df.query("OrderStatus=='Completed' and NetSales>1000"))

#interview Challenge
# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","HR","IT","Sales","Finance","IT"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai","Ahmedabad","Ahmedabad"],
#     "Salary":[50000,65000,70000,80000,60000,75000],
#     "Experience":[2,5,4,8,3,6]
# })
#
# employees_eligible=df.query("Salary >= 65000 and Experience >= 4 and Department == 'IT' or Department=='HR'")
# print(employees_eligible)
# print(df)
# sort_desc_salary=employees_eligible.sort_values("Salary",ascending=False)
# print(sort_desc_salary)
# high_e_salary_emp=sort_desc_salary.head(1)
# print(high_e_salary_emp)
# print(sort_desc_salary.groupby("Department")["Salary"].mean())
# print(sort_desc_salary["City"].value_counts())
# df.to_csv("salary_review.csv")

#mentor
# try:
#     df=pd.read_csv("mentor_challenge_query.csv")
# except Exception as e:
#     print(e)
#
# print(df.info())
# print(df.columns)
# print(df.dtypes)
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.columns)
# print(df)
# df["employee_name"]=df["employee_name"].str.strip().str.title()
# print(df)
#
# df["department"]=df["department"].str.strip().str.title().replace({
#     "Hr":"HR",
#     "Fin":"Finance",
#     "It":"IT"
# })
# df["city"]=df["city"].str.strip().str.title()
# df["gender"]=df["gender"].str.strip().str.title().replace({
#     "M":"Male",
#     "F":"Female"
# })
# df["age"]=df["age"].fillna(df["age"].mean()).astype(int)
#
# df["experience"]=df["experience"].fillna(df["experience"].mean()).astype(int)
# df["salary_category"]=df["salary"].apply(lambda x:"High" if x>70000 else "Low")
# print(df)
#
# # Active employees earning at least 60,000 with at least 3 years of experience
# eligible_emp=df.query("status=='Active' and salary>=60000 and experience>=3")
# print(eligible_emp)
# emp_departmentg=df.groupby("department")["salary"].agg(["sum","max","min","mean","count"])
# print(emp_departmentg)
# top_5_emp_eligible=eligible_emp.head()
# print(top_5_emp_eligible)
# emp_pivot_table=df.pivot_table(index="department",columns="city",values="salary",aggfunc=sum,fill_value=0)
# print(emp_pivot_table)
# try:
#     with pd.ExcelWriter("mentor_challenge_query_final.xlsx") as writer:
#         df.to_excel(writer, sheet_name="Clean Data", index=False)
#         eligible_emp.to_excel(writer, sheet_name="eligible-employee analysis", index=False)
#         emp_pivot_table.to_excel(writer, sheet_name="pivot_table")
#
# except Exception as e:
#     print(e)

#--------------------------------------------------------------------------------------------------------------------
# df = pd.DataFrame({
#     "OrderID":[
#         "O101","O102","O102","O103",
#         "O104","O104","O105","O106"
#     ],
#     "Customer":[
#         "Rahul","Neha","Neha","Amit",
#         "Priya","Priya","Manthan","Khushbu"
#     ],
#     "Product":[
#         "Laptop","Mouse","Mouse","Keyboard",
#         "Monitor","Monitor","Laptop","Mouse"
#     ],
#     "Sales":[
#         1200,50,50,100,
#         300,350,1500,60
#     ]
# })
# print(df.duplicated().sum())
# print(df[df.duplicated()])
# print(df.duplicated("OrderID"))
# print(
#     df[df.duplicated(
#         subset="OrderID"
#     )]
# )
# print(df.drop_duplicates(subset="OrderID"))
# print(df)
# print(df.drop_duplicates(subset="OrderID",keep="first"))
# print(df.drop_duplicates(subset="OrderID",keep="last"))
# print(df.drop_duplicates(subset="OrderID",keep=False))
# print(df.duplicated(subset=["Customer" , "Product"]))
# print(df[df.duplicated(subset=["Customer" , "Product"])])
# print(df.drop_duplicates(subset="OrderID",keep="first",ignore_index=True))

#bonus1
#
# data = {
#     'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
#                    102, 111, 112, 113, 114, 105, 115, 116, 117, 118,
#                    119, 120, 102, 121, 122, 123, 124, 114, 125, 126],
#     'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR', 'Finance', 'Marketing', 'Sales',
#                    'IT', 'HR', 'Finance', 'Marketing', 'Sales', 'Sales', 'IT', 'HR', 'Finance', 'Marketing',
#                    'Sales', 'IT', 'IT', 'HR', 'Finance', 'Marketing', 'Sales', 'Sales', 'IT', 'HR'],
#     'City': ['New York', 'Chicago', 'San Francisco', 'Los Angeles', 'Houston', 'New York', 'Chicago', 'San Francisco', 'Los Angeles', 'Houston',
#              'Austin', 'New York', 'Chicago', 'San Francisco', 'Los Angeles', 'Miami', 'New York', 'Chicago', 'San Francisco', 'Los Angeles',
#              'Houston', 'New York', 'Seattle', 'Chicago', 'San Francisco', 'Los Angeles', 'Houston', 'Dallas', 'New York', 'Chicago'],
#     'Salary': [65000, 85000, 95000, 70000, 75000, 88000, 67000, 98000, 72000, 78000,
#                87000, 66000, 96000, 71000, 76000, 79000, 90000, 68000, 99000, 73000,
#                80000, 92000, 89000, 69000, 97000, 74000, 81000, 82000, 93000, 70000]
# }
#
# df = pd.DataFrame(data)
# print(df.info())
# print(df.duplicated(subset="EmployeeID").sum())
# print(df[df.duplicated(subset="EmployeeID")]["EmployeeID"])
# print(df[df.duplicated(subset="EmployeeID")])
# print(df.drop_duplicates(subset="EmployeeID",keep="last").sort_values(by="EmployeeID",ignore_index=True))

#bonus2
# i am using the CustomerID + ProductID + TransactionDate because of the customerid and product id transactiondate if same so that is duplicates for TransactionID if this is use for the only only payment options and this is totally creates new every time so this is not good for the find duplicates

#Mixed1
# try:
#     df=pd.read_csv("mixed1_duplicates.csv")
# except Exception as e:
#     print(e)
# print(df.info())
# print(df.columns)
# print(df.dtypes)
# df=df.rename(columns={
#   "dept":"department",
#     "full name":"full_name"
# })
# print(df["is_active"].unique())
# df["is_active"]=df["is_active"].replace({
#     "True":"Active",
#     "False":"Inactive",
#     "Yes":"Active"
# })
# print(df)
# print(df["department"].unique())
# df["department"]=df["department"].str.strip().replace({
#     "hr":"HR"
# }).fillna("Unknown")
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["is_active"]=df["is_active"].fillna("Unknown")
# print(df.isna().sum())
# print(df.dtypes) #no needs to change the astypes
# print(df.duplicated().sum())
# print(df[df.duplicated()])
# print(df.drop_duplicates(keep="first",ignore_index=True))
# print(df.query("salary>70000").groupby("department")["salary"].sum())
# print(df.groupby("department")["salary"].sum())
# try:
#     df.to_csv("mixed1_duplicates_final.csv")
# except Exception as e:
#     print(e)

# #mixed2
# try:
#     customers=pd.read_csv("mixed2_duplicates_customers.csv")
#     orders=pd.read_csv("mixed2_duplicates_orders.csv")
# except Exception as e:
#     print(e)
#
# print(customers.info())
# print(orders.info())
# customers.columns=customers.columns.str.strip().str.lower().str.replace(" ","_")
# orders.columns=orders.columns.str.strip().str.lower().str.replace(" ","_")
# customers["customer_id"]=customers["customer_id"].str.strip()
# orders["customer_id"]=orders["customer_id"].str.strip()
# df=pd.merge(customers,orders,how="inner",on="customer_id")
# print(df)
#
# df["signup_date"]=pd.to_datetime(df["signup_date"],format="mixed")
# df["order_date"]=pd.to_datetime(df["order_date"],format="mixed")
# print(df.dtypes)
# print(df.duplicated())
# print(df.duplicated().sum())
# print(df[df.duplicated()])
# df=df.drop_duplicates()
# print(df.duplicated().sum())
# print(df["country"].value_counts())
# print(df.groupby("country")["spend"].mean())
# print(df.pivot_table(index="country",columns="product_category",values="spend",aggfunc=sum,fill_value=0))
# df.to_csv("mixed2_duplicates_final.csv",index=False)

# #mixed3
# try:
#     df=pd.read_excel('mixed3_dupliucates.xlsx',sheet_name=None)
#     print(df.keys())
# except Exception as e:
#     print(e)
# print(df["North_Region"])
# print(df["South_Region"])
#
# df_con=pd.concat([df["North_Region"],df["South_Region"]])
# print(df_con)
# print(df_con.columns)#nothings to do drop
# print(df_con["Product"].unique())
# print(df_con["Sales_Channel"].unique())
# df_con["Sales_Channel"]=df_con["Sales_Channel"].str.strip().str.title()#no needs to replace
# print(df_con)
# print(df_con.duplicated())
# print(df_con.duplicated().sum())
# df_con=df_con.drop_duplicates()
# print(df_con.duplicated().sum()) #this is compeleted already so i donot repeat more so please i do not do more practical of this topic

#-------------------------------------------------------------------------------------------
#
# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Age":[22,27,35,42,29,51,24,61],
#     "Salary":[35000,52000,68000,95000,48000,125000,72000,160000]
# })
#
# df["Salary_Category"]=pd.cut(
#     df["Salary"],
#     bins=[0,50001,100000,float("inf")],
#     labels=["Low","Medium","High"]
# )
# print(df)
# df["Age_Groups"]=pd.cut(
#     df["Age"],
#     bins=[0,19,30,51,100],
#     labels=["Teen","Young Adult","Adult","Senior"]
# )
# print(df)
# print(df["Salary_Category"].value_counts())
# print((df["Age_Groups"].value_counts()))
# df["Salary_q"]=pd.qcut(
#     df["Salary"],
#     q=4,
#     labels=["q1","q2","q3","q4"]
# )
# print(df)
# print(df["Salary_q"].value_counts())
# print(df.groupby("Salary_Category")["Salary"].mean())
# print(df.groupby("Salary_Category")["Age"].mean())
# usort = df.sort_values("Salary")["Salary_Category"]
# print(usort)
# df.to_excel("employee_salary_bands.xlsx",index=False)

#--------------------------------------------------------------------------------------
#
# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Department":["IT","IT","HR","HR","Finance","Finance","IT","HR"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai","Ahmedabad","Surat","Mumbai","Ahmedabad"],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,65000]
# })
# print(df)
# average_Salary_dep=df.groupby("Department")["Salary"]
# df["Salary_mean"]=average_Salary_dep.transform("mean")
# df["Salary_max"]=average_Salary_dep.transform("max")
# df["Salary_min"]=average_Salary_dep.transform("min")
# df["Salary_sum"]=average_Salary_dep.transform("sum")
# df["Salary_count"]=average_Salary_dep.transform("count")
# df["Contribution_%"] = (
#     df["Salary"] /
#     df["Salary_sum"]
# ) * 100
# print(df)
# print(df.groupby("Department")["Contribution_%"].sum())
# df["Different"]=df["Salary"]-df["Salary_mean"]
# print(df)
# print(df.query("Salary>Salary_mean"))
# df=df.sort_values(by=["Department","Salary"],ascending=[True,False])
# print(df)
# df.to_excel("transform_analysis.xlsx",index=False)

#------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Department":["IT","IT","HR","HR","Finance","Finance","IT","HR"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai","Ahmedabad","Surat","Mumbai","Ahmedabad"],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,65000],
#     "Rating":[4.2,4.8,3.9,4.7,4.5,4.9,4.6,4.0]
# })
# df["Rank_S"]=df["Salary"].rank(ascending=False)
# df["Rank_dense_S"]=df["Salary"].rank(ascending=False,method="dense")
# df["Rank_min_S"]=df["Salary"].rank(ascending=False,method="min")
# df["Rank_first_S"]=df["Salary"].rank(ascending=False,method="first")
# df["Rank_Rating"]=df["Rating"].rank()
# print(df)
# df["department_g_salary"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(df[df["Rank_S"]<=3])
# print(df[df["department_g_salary"]<=2])
# df=df.sort_values(["Department","department_g_salary"],ascending=[True,False])
# print(df)
# df.to_excel("employee_rank_analysis.xlsx")

#bonus1
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Department":["IT","IT","HR","HR","Finance","Finance","IT","HR"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai","Ahmedabad","Surat","Mumbai","Ahmedabad"],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,65000],
#     "Rating":[4.2,4.8,3.9,4.7,4.5,4.9,4.6,4.0]
# })
# highest_salary_in_department=df.groupby("Department")["Salary"].transform("max")
# df["Salary_Gap"]=highest_salary_in_department-df["Salary"]
# #bonus2
# df["Department_Wise_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False)
# conditions = [
#     df['Department_Wise_Rank'] == 1,
#     df['Department_Wise_Rank'] == 2,
#     df['Department_Wise_Rank'] == 3
# ]
# choices = ['Gold', 'Silver', 'Regular']
# df['Top_Performer'] = np.select(conditions, choices, default='Unknown')
# print(df)

#mixed1
# try:
#     df=pd.read_csv("Mixed1_rank.csv")
# except Exception as e:
#     print(e)
#
# print(df.info())
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# df=df.rename(columns={
#     "emp_id":'employee_id',
#     "dept":"department",
#     "salary_($)":"salary",
#     "experience_yrs":"experience_years",
# })
# df["department"]=df["department"].replace({
#     "IT":"Information Technology",
#     "HR":"Human Resources",
# })
# print(df.columns)
# print(df.dtypes)
# df["salary"]=pd.to_numeric(df["salary"],errors="coerce")
# df["salary"]=df["salary"].fillna(df["salary"].median()).astype(int)
# df["experience_years"]=pd.to_numeric(df["experience_years"],errors="coerce")
# df["experience_years"]=df["experience_years"].fillna(df["experience_years"].mean())
# df["rating"]=pd.to_numeric(df["rating"],errors="coerce")
# df["rating"]=df["salary"].rank(ascending=False,method='first')
# print(df.query("department=='Information Technology' and salary>100000"))
# df["salary_category"]=pd.cut(
#     df["salary"],
#     bins=[80000,95000,110000,float("inf")],
#     labels=["Low","Medium","High"]
# )
# print(df)
# print(df.groupby("department")["salary"].mean())
# df["salary_department_wise_average"]=df.groupby("department")["salary"].transform("mean")
# df["salary_gap"]=df["salary"]-df["salary_department_wise_average"]
# print(df)
# df["salary_rank"] = df.groupby("department")["salary"].rank(ascending=False, method="dense")
#
# top_earners = df.query("salary_rank <= 3")
# print(top_earners)

#mixed2
# try:
#     emp=pd.read_csv("mixed2_rank_emp.csv")
#     attendance=pd.read_csv("mixed2_rank_attendance.csv")
#     performance=pd.read_csv("mixed2_rank_performance.csv")
# except Exception as e:
#     print(e)
#
# print(emp.info())
# print(attendance.info())
# print(performance.info())
#
# df_1=pd.merge(emp,attendance,on="Emp_ID",how="inner")
# df=pd.merge(df_1,performance,on="Emp_ID",how="inner")
# print(df)
# print(df.query("Projects_Completed>=5")[["Name","Department","Projects_Completed"]])
# group_department_salary_total=df.groupby("Department")["Salary"].sum()
# print(group_department_salary_total)
# df["Department_Wise_Ave_Salary"]=df.groupby("Department")["Salary"].transform("mean")
# df["Department_Wise_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method='dense')
# department_pivot_table=df.pivot_table(index="Department",columns="Department_Wise_Salary_Rank",values="Salary",aggfunc='max',fill_value=0)
# print(department_pivot_table)
# department_crosstable=pd.crosstab(index=df["Department"],columns=df["Department_Wise_Salary_Rank"],normalize=True)*100
# print(department_crosstable)
# df["Attendance %"]=df["Days_Present"]/df["Total_Days"]*100
# conditions = [
#     df['Department_Wise_Salary_Rank'] == 1,
#     df['Department_Wise_Salary_Rank'] == 2,
#     df['Department_Wise_Salary_Rank'] == 3
# ]
# choices = ['Gold', 'Silver', 'Regular']
# df['Top_Performer'] = np.select(conditions, choices, default='Unknown')
# df["Salary_Category"]=pd.cut(df["Salary"],
#                              bins=[84000,90000,100000,float("inf")],
#                              labels=["Low","Medium","High"]
#                              )
# print(df)
# df.to_excel("mixed2_rank_final.xlsx")

# #mixed3
# try:
#     excel=pd.read_excel('mixed3_rank.xlsx',sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)
#
# emp=excel["emp"]
# salary=excel["salary"]
# attendance=excel["attendance"]
# department=excel["departments"]
# print(emp.info())
# print(salary.info())
# print(attendance.info())
# print(department.info())
#
# df_1=pd.merge(emp,salary,on="Employee_ID",how="inner")
# df_2=pd.merge(df_1,attendance,on="Employee_ID",how="inner")
# df=pd.merge(df_2,department,on="Department_ID",how="inner")
# print(df.duplicated().sum())
# df=df.drop_duplicates().reset_index(drop=True)
# print(df.columns)
# print(df.dtypes)
# df["City"]=df["City"].fillna("Unknown")
# df["Performance_Rating"]=df["Performance_Rating"].fillna(df["Performance_Rating"].mean())
# df["Current_Salary"]=df["Current_Salary"].fillna(df["Current_Salary"].median())
# df["Bonus"]=df["Bonus"].fillna(df["Bonus"].mean())
# print(df.isna().sum())
# df["Salary_Category"]=pd.cut(df["Current_Salary"],
#                              bins=[58000,65000,80000,float("inf")],
#                              labels=["Low","Medium","High"],include_lowest=True
#                              )
# df["Salary_Quartile"]=pd.qcut(df["Current_Salary"],
#                               q=4,
#                               labels=["Q1","Q2","Q3","Q4"])
#
# df["Department_Wise_Average_Salary"]=df.groupby("Department_Name")["Current_Salary"].transform("mean")
# df["Employees_Rank_In_Department"]=df["Department_Wise_Average_Salary"].rank(ascending=False,method='dense')
# print(df)
#
# df_Top5_Emp=df.sort_values("Current_Salary",ascending=False,ignore_index=True).head()
# print(df_Top5_Emp)
#
# department_wise_pivot_table=df.pivot_table(index="Department_Name",columns="City",values="Current_Salary",aggfunc=sum,fill_value=0)
# print(department_wise_pivot_table)
#
# crosstable_department_city=pd.crosstab(index=df["Department_Name"],columns=df["City"],normalize=True)*100
# print(crosstable_department_city)
#
#
# with pd.ExcelWriter("mixed3_rank_final.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Clean Employee Data", index=False)
#     df_Top5_Emp.to_excel(writer, sheet_name="Top_Employees", index=False)
#     department_wise_pivot_table.to_excel(writer, sheet_name="Pivot_Report", index=False)
#     crosstable_department_city.to_excel(writer, sheet_name="Dashboard_Data", index=False)

#------------------------------------------------------------------------------------------------

import pandas as pd

# df = pd.DataFrame({
#     "Day":[1,2,3,4,5,6,7,8,9,10],
#     "Sales":[100,120,90,130,140,150,170,160,180,190],
#     "Profit":[20,25,18,30,35,40,45,42,48,50]
# })
# df["3_day_averagesale"]=df["Sales"].rolling(3).mean()
# df["3_day_sumsale"]=df["Sales"].rolling(3).sum()
# df["3_day_maxsale"]=df["Sales"].rolling(3).max()
# df["3_day_minsale"]=df["Sales"].rolling(3).min()
# df["3_day_stdsale"]=df["Sales"].rolling(3).std()
# df["3_day_averageprofit"]=df["Profit"].rolling(3).mean()
# df["3_day_averagesalewithminp"]=df["Sales"].rolling(3,min_periods=1).mean()
# print(df.sort_values("3_day_averagesalewithminp",ascending=False).head(1)["Day"])
# print(df.nlargest(1, "3_day_averagesalewithminp")["Day"])
# df=df.sort_values("3_day_averagesalewithminp",ascending=False,ignore_index=True)
# print(df)
# df.to_excel("rolling_analysis.xlsx",index=False)

#bonus1

# df = pd.DataFrame({
#     "Day":[1,2,3,4,5,6,7,8,9,10],
#     "Sales":[100,120,90,130,140,150,170,160,180,190],
#     "Profit":[20,25,18,30,35,40,45,42,48,50]
# })
# df["Sales_Growth"]=df["Sales"].diff()
# print(df)
# print(df.nlargest(1,"Sales_Growth"))
# print(df.nlargest(1,"Sales_Growth")["Day"])
# print(df.nsmallest(1,"Sales_Growth"))
# print(df.nsmallest(1,"Sales_Growth")["Day"])
# Bonus 2
# 3-Day Rolling Mean − Overall Average Sales

# df["Rolling_Growth"]=df["Sales"].rolling(3,min_periods=1).mean()-df["Sales"].mean()
# df["Classification_Of_Average"]=np.where( df["Rolling_Growth"] > df["Sales"].mean(), "Above Average","Below Average")
# print(df)

#mixed1

# try:
#     df=pd.read_csv("mixed1_rolling.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# df["date"]=pd.to_datetime(df["date"])
# print(df.duplicated().sum())
# df["sales"]=df["sales"].fillna(df["sales"].mean())
# df["quantity"]=df["quantity"].fillna(df["quantity"].mean())
# print(df.isna().sum())
# #no needs to replace
# df["7days_averagesale"]=df["sales"].rolling(7,min_periods=1).mean()
# df["Sales_Difference"]=df["sales"].diff()
# print(df)
# print(df.query("sales>1500"))
# print(df.groupby("region")["sales"].mean())

#mixed2

try:
    sales=pd.read_csv("mixed2_rolling_sales.csv")
    products=pd.read_csv("mixed2_rolling_products.csv")
    stores=pd.read_csv("mixed2_rolling_stores.csv")
except Exception as e:
    print(e) 

print(sales.info())
print(products.info())
print(stores.info())

df_1=pd.merge(sales,stores,on="Store_ID",how="inner")
df=pd.merge(df_1,products,on="Product_ID",how="inner")
print(df.dtypes)
print(df.columns)
df["Average_2days_q"]=df["Quantity"].rolling(2,min_periods=1).mean()
print(df.groupby("Department")["Quantity"].sum())
df["City_price_mean"]=df.groupby("City")["Price"].transform("mean")
df["Department_wise_price_rank"]=df.groupby("Department")["Price"].rank(ascending=False,method="dense")
print(df.pivot_table(index="City",columns="Department",values="Price",aggfunc="mean"))
# df["Store_wise_rolling_average"]=df.groupby("Store_ID")["Price"]
print(df)
