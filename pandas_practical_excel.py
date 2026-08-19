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

# try:
#     sales=pd.read_csv("mixed2_rolling_sales.csv")
#     products=pd.read_csv("mixed2_rolling_products.csv")
#     stores=pd.read_csv("mixed2_rolling_stores.csv")
# except Exception as e:
#     print(e) 

# print(sales.info())
# print(products.info())
# print(stores.info())

# df_1=pd.merge(sales,stores,on="Store_ID",how="inner")
# df=pd.merge(df_1,products,on="Product_ID",how="inner")
# print(df.dtypes)
# print(df.columns)
# df["Average_2days_q"]=df["Quantity"].rolling(2,min_periods=1).mean()
# print(df.groupby("Department")["Quantity"].sum())
# df["City_price_mean"]=df.groupby("City")["Price"].transform("mean")
# df["Department_wise_price_rank"]=df.groupby("Department")["Price"].rank(ascending=False,method="dense")
# print(df.pivot_table(index="City",columns="Department",values="Price",aggfunc="mean"))
# print(df.groupby("Store_ID")["Price"].mean()) #not rolling done
# df["Total_Sale"]=df["Price"]*df["Quantity"]
# df["Product_wise_sale_rank"]=df.groupby("Product_Name")["Total_Sale"].rank(ascending=False,method="dense")
# print(df.groupby("Department")["Total_Sale"].mean())
# print(df)
# df.to_excel("mixed2_rolling_final.xlsx")

# mixed3
# try:
#     excel=pd.read_excel("mixed3_rolling_input.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#    print(e) 

# north=excel["Region_North"]
# south=excel["Region_South"]

# print(north.info())
# print(south.info())
# df=pd.concat([north,south],ignore_index=True)
# df["Date"]=pd.to_datetime(df["Date"])
# df["Sales"]=df["Sales"].fillna(df["Sales"].mean())
# df["Traffic"]=df["Traffic"].fillna(df["Traffic"].mean())
# df=df.drop_duplicates(ignore_index=True)
# df_rollingreport=df["Rolling_Average_3DaySales"]=df["Sales"].rolling(3,min_periods=1).mean()
# df["Average_of_storewisesales"]=df.groupby("Store")["Sales"].transform("mean")
# df_rankingreport=df["Ranking_To_Traffic"]=df["Sales"].rank(ascending=False,method="dense")
# df["Day_Name"]=df["Date"].dt.day_name()
# pivot_table=df.pivot_table(index="Day_Name",columns="Store",values="Traffic",aggfunc="mean")
# print(df)
# print(pivot_table)
# with pd.ExcelWriter("mixed3_rolling_final.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Clean Data", index=False)
#     df_rollingreport.to_excel(writer, sheet_name="Rolling Report", index=False)
#     df_rankingreport.to_excel(writer, sheet_name="Ranking Report", index=False)
#     pivot_table.to_excel(writer, sheet_name="Dashboard Data", index=False)


#interview question

# try:
#     df=pd.read_csv("Interview_Challenge_rolling.csv")
# except Exception as e:
#    print(e) 

# print(df.info())
# df["Date"]=pd.to_datetime(df["Date"])
# df["Day"]=df["Date"].dt.day
# df["Day_name"]=df["Date"].dt.day_name()
# df["Sale_average_7days"]=df["Sales"].rolling(7,min_periods=1).mean()
# df["Profits_sum_7days"]=df["Profit"].rolling(7,min_periods=1).sum()
# print(df.nlargest(1,"Sale_average_7days")[["Day","Day_name","Sales","Sale_average_7days"]])
# df["Rank_by_totalsale"]=df.groupby("Store")["Sales"].transform("sum").rank(ascending=False,method="dense")
# print(df)
# each_store_total_con=df.groupby("Store")["Sales"].sum()
# print(each_store_total_con/df["Sales"].sum()*100)

# pivot_table=df.pivot_table(index="Store",columns="Product",values="Sales",aggfunc="mean",fill_value=0)
# print(pivot_table)
# df.to_excel("Interview_Challenge_rolling_final.xlsx",index=False)

#mentor

# try:
#     df=pd.read_excel("Interview_Challenge_rolling_final.xlsx")
# except Exception as e:
#    print(e) 
# df["Sales_Growth"]=df["Sales"].diff()
# print(df.groupby("Store")["Sales"].mean())
# df["Sales_Category"]=pd.cut(
#     df["Sales"],
#     bins=[114,530,750,float("inf")],
#     labels=["Low","Medium","High"]
# )
# df["Sales_Quartile"]=pd.qcut(df["Sales"],q=4,labels=["Q1","Q2","Q3","Q4"])
# print(df)
# df.to_excel("Mentor_Challenge_rolling_final.xlsx",index=False)

#---------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     "Experience":[1,2,3,4,5,6,7,8],
#     "Salary":[30000,40000,45000,55000,65000,72000,80000,90000],
#     "Rating":[3.1,3.3,3.5,3.9,4.1,4.3,4.6,4.9],
#     "Projects":[1,2,2,3,4,5,5,6]
# })
# print(df.corr(numeric_only=True))
# print(df["Salary"].corr(df["Experience"]))
# print(df["Salary"].corr(df["Rating"]))
# print(df.cov(numeric_only=True))
# corr_matrix = df.corr(numeric_only=True)

# print(corr_matrix)
# print(df["Experience"].corr(df["Rating"])) #yes with : 0.9971874713008774 high positive 
# print(df.sort_values("Salary",ascending=True).corr(numeric_only=True)[["Experience","Rating","Projects"]])
# #i do not understand the 8 
# print(df["Salary"].corr(df["Experience"])) # There is an almost perfect positive linear relationship between two business variables.
# # If Experience increases, so salary also would be increase for the positive coreationship


# #bonus1

# # df = pd.DataFrame({
# #     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
# #     "Experience":[1,3,5,7,4,8],
# #     "Salary":[30000,50000,70000,90000,65000,110000],
# #     "Projects":[1,2,4,5,3,6],
# #     "Rating":[3.2,3.8,4.2,4.8,4.0,4.9]
# # })
# # print(df.corr(numeric_only=True))
# # print(df.cov(numeric_only=True))
# # print(df["Salary"].corr(df["Experience"]))
# # print(df["Salary"].corr(df["Projects"]))
# # print(df["Salary"].corr(df["Rating"]))
# # corr_matrix = df.corr(numeric_only=True)
# # corr_matrix=corr_matrix["Salary"].drop("Salary")
# # print(corr_matrix.nlargest(1))
# # print(corr_matrix.nsmallest(1))
# # print(corr_matrix.sort_values(ascending=False))#the sort order high to low
# # print(df["Experience"].corr(df["Projects"]))  
# # 0.99369440545299
# # Employee experience and project completion are deeply linked, meaning team members with more tenure almost always manage a higher volume of projects.

# #bonus2
# import pandas as pd

# df = pd.DataFrame({
#     "Advertisement":[20,25,30,40,50,60,70,80],
#     "Sales":[120,150,180,240,290,350,400,470],
#     "Discount":[40,35,30,28,25,20,15,10],
#     "Profit":[60,80,95,120,150,180,220,260]
# })

# print(df.corr(numeric_only=True))
# print(df.cov(numeric_only=True))
# print(df["Advertisement"].corr(df["Sales"]))
# print(df["Discount"].corr(df["Profit"])) #that is low negitive realtion 
# corr_matrix=df.corr(numeric_only=True)
# print(corr_matrix)
# corr_matrix = df.corr(numeric_only=True)
# corr_matrix=corr_matrix["Profit"].drop("Profit")
# print(corr_matrix.sort_values())
# print(df["Advertisement"].corr(df["Profit"]))
# 0.9970596552486798
# Your marketing budget is a near-perfect predictor of company profitability, meaning ad investments directly translate into bottom-line growth.

# mixed1

# try:
#     df=pd.read_csv("mixed1_corr.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# df=df.rename(columns={
#     "experience_(years)":"experience",
# })
# print(df.columns)
# df["joining_date"]=pd.to_datetime(df["joining_date"],format='mixed')
# print(df.dtypes)
# df["salary"]=df["salary"].fillna(df["salary"].median())
# df["experience"]=df["experience"].fillna(df["experience"].mean())
# print(df.isna().sum())
# print(df.duplicated().sum())
# df["department"]=df["department"].replace({
#     "IT Dept":"IT",
# })
# print(df["department"].unique())
# df["total_compensation"]=df["salary"]+df["bonus"]
# df["salary_category"]=pd.cut(df["salary"],
#     bins=[45000,75000,120000,float("inf")],
#     labels=["Low","Medium","High"] ,
#     include_lowest=True)
# df["salary_quartile"]=pd.qcut(df["salary"],
#     q=4,
#     labels=["Q1","Q2","Q3","Q4"])
# print(df.corr(numeric_only=True))
# numeric_df = df.select_dtypes(include=['number'])
# print(numeric_df.cov())
# correlations = df.corr(numeric_only=True)['salary']
# most_correlated = correlations.drop('salary').idxmax()
# print(f"The most correlated feature is: {most_correlated}")
# df["rank_salary_department"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# df["department_average_salary"]=df.groupby("department")["salary"].transform("mean")
# df["salary_gap"]=df["salary"]-df["department_average_salary"]
# print(df)
# print(df.groupby("department")["salary"].mean())
# print(df.pivot_table(index="department",columns="city",values="salary",aggfunc="mean",fill_value=0))
# df.to_csv("mixed1_corr_final.csv")

#mixed2
# try:
#     emp=pd.read_csv("mixed2_corr_emp.csv")
#     salary=pd.read_csv("mixed2_corr_salary.csv")
#     performance=pd.read_csv("mixed2_corr_per.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(salary.info())
# print(performance.info())
# emp.columns=emp.columns.str.strip().str.lower().str.replace(" ","_")
# salary.columns=salary.columns.str.strip().str.lower().str.replace(" ","_")
# performance.columns=performance.columns.str.strip().str.lower().str.replace(" ","_")
# print(emp.columns)
# print(salary.columns)
# print(performance.columns)
# salary=salary.rename(columns={"emp_id":"employee_id"})
# performance=performance.rename(columns={"id":"employee_id"})
# df_1=pd.merge(emp,salary,on="employee_id",how="inner")
# df=pd.merge(df_1,performance,on="employee_id",how="inner")
# df["joining_date"]=pd.to_datetime(df["joining_date"])
# df["days_present"]=df["days_present"].fillna(df["days_present"].mean()).astype(int)
# df["base_salary"]=df["base_salary"].fillna(df["base_salary"].median())
# df["bonus"]=df["bonus"].fillna(df["bonus"].mean())
# df["rating"]=df["rating"].fillna(df["rating"].mean())
# print(df.columns)
# print(df.info())
# print(df.isna().sum())
# df=df.drop_duplicates()
# print(df.duplicated().sum())
# print(df.corr(numeric_only=True))
# correlations = df.corr(numeric_only=True)['base_salary']
# most_correlated = correlations.drop('base_salary').sort_values()
# print(most_correlated)
# df["attendance_%"]=df["days_present"]/df["total_work_days"]*100
# df["total_compensation"]=df["base_salary"]+df["bonus"]
# df["performance_level"]=pd.cut(df["rating"],
# bins=[0,3,4,float("inf")],
# labels=["Poor","Average","Excellent"])
# df["rank_salary_department"]=df.groupby("department")["base_salary"].rank(ascending=False,method="dense")
# df["department_av_salary"]=df.groupby("department")["base_salary"].transform("mean")
# print(df)
# print(df.groupby("department")[["base_salary","rating"]].max())
# print(df.pivot_table(index="city",columns="department",values="base_salary",fill_value=0,aggfunc="mean"))
# df.to_excel("mixed2_corr_final.xlsx",index=False)

#-----------------------------------------------------------------------------------------------

# import pandas as pd

# df = pd.DataFrame({
#     "Day":[1,2,3,4,5,6,7,8,9,10],
#     "Sales":[120,150,180,170,200,240,220,260,280,300],
#     "Profit":[20,30,35,32,40,45,43,48,52,55]
# })
# df["Previous_Sales"]=df["Sales"].shift(1)
# df["Next_Sales"]=df["Sales"].shift(-1)
# df["Sales_Difference"]=df["Sales"]-df["Previous_Sales"]
# df["Sales_Growth_%"]=df["Sales"].pct_change()*100
# df["Profit_Growth_%"]=df["Profit"].pct_change()*100
# print(df.nlargest(1,"Sales_Growth_%")["Day"])
# print(df.nsmallest(1,"Sales_Growth_%")["Day"])
# df["Previous_Profit"]=df["Profit"].shift(1)
# df=df.sort_values("Sales_Growth_%",ascending=False,ignore_index=True)
#bonus1
# df["Growth_Type"]=df["Sales_Growth_%"].apply(lambda x:"Excellent Growth" if x>15 else("Positive Growth" if x>0 else"Negative Growth"))
#bonus2
# df["Sales_vs_Previous"] = df.apply(
#     lambda row: "Increase" if row["Sales"] > row["Previous_Sales"] 
#     else ("No Change" if row["Sales"] == row["Previous_Sales"] else "Decrease"), 
#     axis=1
# )
# print(df)

#mixed1
# try:
#     df=pd.read_csv("mixed1_shift_pct.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# df=df.rename(columns={
#     'employee_name':"name",
#     'dept':"department",
#     'join_date':"joining_date"
# })

# df["joining_date"]=pd.to_datetime(df["joining_date"])
# print(df.columns)
# print(df.dtypes)
# df["sales"]=df["sales"].fillna(df["sales"].mean())
# df["salary"]=df["salary"].fillna(df["salary"].median())
# print(df.isna().sum())
# df=df.drop_duplicates()
# print(df.duplicated().sum())
# df["department"]=df["department"].replace({
#     "Engneering":"Engineering"
# })
# print(df.query("salary>100000"))
# department_wise_average_sales=df.groupby("department")["sales"].mean()
# print(department_wise_average_sales)
# df["d_average_sales"]=df.groupby("department")["sales"].transform("mean")
# df["salary_category"]=pd.cut(df["salary"],
# bins=[60000,80000,100000,float("inf")],
#     labels=["Low","Mideum","High"])
# df["quantile_salary"]=pd.qcut(df["salary"],
#                               q=4,
#                               labels=["Q1","Q2","Q3","Q4"])
# df["city_wise_sales_rank"]=df.groupby("city")["sales"].rank(ascending=False,method="dense")
# df["7days_sales_rolling_average"]=df["sales"].rolling(7,min_periods=1).mean()
# df["next_sales"]=df["sales"].shift(-1)
# # print(df[["sales","previous_sales","next_sales"]])
# df["different_sales"]=df["previous_sales"]-df["sales"]
# df['joining_date'] = pd.to_datetime(df['joining_date'])
# df = df.sort_values('joining_date').reset_index(drop=True)

# df["sales_growth%"]=df["sales"].pct_change()*100
# print(df[["sales","previous_sales","different_sales","sales_growth%"]])
# print(df.pivot_table(index="city",columns="department",values="sales",aggfunc="count",fill_value=0))
# print(df.nlargest(1,"sales_growth%"))
# print(df.groupby("department")["sales_growth%"].mean().idxmax())
# print(df.groupby("city")["salary"].mean())
# print(df.columns) #Employee whose salary increased the most and Top 5 salary growth employees I  HAVE not parameter for couting
# df.to_csv("mixed1_shift_final.csv")

#mixed2
# try:
#     emp=pd.read_csv("mixed2_shift_pct_emp.csv")
#     attendance=pd.read_csv("mixed2_shift_pct_attendance.csv")
#     salary=pd.read_csv("mixed2_shift_pct_salary.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(attendance.info())
# print(salary.info())
# me=pd.merge(emp,attendance,on="emp_id",how="inner")
# df=pd.merge(me,salary,on="emp_id",how="inner")
# print(df.info())
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# df=df.rename(columns={
#     "emp_id":"employee_id",
#     "emp_name":"name",
#     "hire_date":"hiring_date",
#     "month_x":"month_attendance",
#     "month_y":"month_salary",
#     "base_salary":"salary"
# })
# print(df.columns)
# df["hiring_date"]=pd.to_datetime(df["hiring_date"],format="mixed")
# df["bonus"]=pd.to_numeric(df["bonus"],errors="coerce")
# df["bonus"]=df["bonus"].fillna(df["bonus"].mean()).astype(int)
# print(df.dtypes)
# print(df.isna().sum())
# print(df.duplicated().sum())
# df["attendance_%"]=df["days_present"]/df["total_working_days"]*100
# print(df.query("`attendance_%`<80"))
# print(df.groupby("name")["bonus"].mean())
# df["salary_average_by_employee"]=df.groupby("employee_id")["salary"].transform("mean")
# df["rank_by_attendance"]=df.groupby("department")["attendance_%"].rank(ascending=False,method="dense")
# print(df)
# print(pd.crosstab(index=df["department"],columns=df["employee_id"],values=df["salary"],aggfunc="mean"))
# #i can not do all questions because some are repeats

#----------------------------------------------------------------------------

# df = pd.DataFrame({
#     "Date":[
#         "2026-01-01","2026-01-02","2026-01-03",
#         "2026-01-10","2026-01-15",
#         "2026-02-01","2026-02-05",
#         "2026-02-20",
#         "2026-03-01","2026-03-15"
#     ],
#     "Sales":[1200,1500,1400,1800,2000,2200,2100,2500,2700,3000],
#     "Profit":[250,300,280,360,400,420,410,500,550,600]
# })
#
# print(df.info())
# df["Date"]=pd.to_datetime(df["Date"])
# print(df.dtypes)
# df=df.set_index("Date")
# print(df.resample("ME")["Sales"].sum())
# print(df.resample("ME")["Sales"].mean())
# print(df.resample("ME")["Sales"].max())
#
# print(df.resample("W")["Sales"].mean())
# print(df.resample("YE")["Sales"].sum())
# print(df.resample("ME")["Profit"].count())
#
# custom_summary = df.resample('ME').agg({
#     'Sales': 'sum',
#     'Profit': 'sum',
# })
# print(custom_summary)
# print(df.resample("ME")["Sales"].sum().idxmax())
#
# monthly_df = df.resample("ME")[["Sales"]].sum()
# monthly_df["Monthly_Growth_%"] = monthly_df["Sales"].pct_change() * 100
#
# print(monthly_df)
#
# Monthly_Profit_Margin=df.resample("ME")["Profit"].sum()/df.resample("ME")["Sales"].sum()*100
# print(Monthly_Profit_Margin)

#mixed1
# try:
#     df=pd.read_csv('mixed1_resample.csv')
# except Exception as e:
#     print(e)

# print(df.info())
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# df=df.rename(columns={
#     "emp_name":"name",
#     "dept_name":"department",
#     "revenue_amount":"revenue"
# })
# print(df.columns)
# df["date"]=pd.to_datetime(df["date"],format="mixed")
# print(df.dtypes)
# df["date"]=df["date"].fillna(df["date"].mean())
# df["revenue"]=df["revenue"].fillna(df["revenue"].mean())
# print(df.isna().sum())
# df=df.drop_duplicates()
# print(df.duplicated().sum())
# print(df)#no needs to astype
# df=df.set_index("date",drop=True)
# print(df)
# print(df.query("revenue>500"))
# print(df.groupby("department")["revenue"].mean())
# df["unit_sold_average_by_department"]=df.groupby("department")["units_sold"].transform("mean")
# df["department_revenue_rank"]=df.groupby("department")["revenue"].rank(ascending=False,method="dense")
# df["units_category"]=pd.cut(df["units_sold"],
#                             bins=[0,5,10,float("inf")],
#                             labels=["Low","Mideum","High"])
# df["quantile_revenue"]=pd.qcut(df["revenue"],
#                                q=5,
#                               labels= ["Q1","Q2","Q3","Q4","Q5"])
# df["3days_rolling_average_revenue"]=df["revenue"].rolling(3,min_periods=1).mean()
# df["previous_revenue"]=df["revenue"].shift(1)
# df["revenue_%"]=df["revenue"]-df["previous_revenue"].pct_change()*100
# print(df)
# print(df["units_sold"].resample("ME").sum())
# print(df.pivot_table(index="department",columns="name",values="units_sold",aggfunc="sum",fill_value=0))
# df=df.reset_index()
# df["month_name"]=df["date"].dt.month_name()
# df["sales"]=df["revenue"]*df["units_sold"]
# df["quarterly"]=df["date"].dt.quarter
# print(df.groupby("month_name")["sales"].mean().idxmax())
# print(df.groupby("quarterly")["sales"].mean().idxmax())
# df=df.set_index("date")
# monthly_revenue = df.groupby(["department", "month_name"])["revenue"].sum()
# highest_pair = monthly_revenue.idxmax()
# highest_value = monthly_revenue.max()

# print(f"Highest: {highest_pair} with {highest_value}")

# df["monthly_growth%"]=df["revenue"]/df["previous_revenue"]*100
# print(df)

# top_emp = df.groupby(["name", "month_name"])["revenue"].sum()
# highest_pair = top_emp.idxmax()
# highest_value = top_emp.max()

# print(f"Highest: {highest_pair} with {highest_value}")
# df.to_csv("mixed1_resample_final.csv",index=False)

#mixed2

# try:
#     emp=pd.read_csv("mixed2_resample_emp.csv")
#     sales=pd.read_csv("mixed2_resample_sales.csv")
#     attendance=pd.read_csv("mixed2_resample_attendance.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(sales.info())
# print(attendance.info())

# me=pd.merge(emp,sales,on="EmployeeID",how="inner")
# df=pd.merge(me,attendance,on="EmployeeID",how="inner")
# print(df.info())
# print(df.columns)
# df["JoinDate"]=pd.to_datetime(df["JoinDate"])
# df["SaleDate"]=pd.to_datetime(df["SaleDate"])
# df["Date"]=pd.to_datetime(df["Date"])
# print(df.dtypes)
# print(df.isna().sum())
# print(df.duplicated().sum())
# print(df.query("Salary>60000"))
# print(df.groupby("Department")["Salary"].mean())
# df["Employee_By_Sale_Average"]=df.groupby("EmployeeID")["Amount"].transform("mean")
# df["3Days_rolling_sale_rage"]=df["Amount"].rolling(3,min_periods=1).mean()
# df["Previous_Sales"]=df["Amount"].shift(1)
# df["Sales_Growth%"]=df["Amount"].pct_change()*100
# df=df.set_index("JoinDate")
# print(df.resample("ME")["Salary"].sum())
# df=df.reset_index(drop=True)
# print(df.corr(numeric_only=True))
# df["Department_Wise_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(df)
# print(df.query("Department_Wise_Salary_Rank==1"))
# print(df.pivot_table(index="Name",columns="Department",values="Salary",aggfunc="mean",fill_value=0))
# print(pd.crosstab(index=df["Department"],columns=df["Status"],normalize=True)*100)
# #i have any parameter to count the : Monthly attendance
# df=df.set_index("Date")
# print(df.resample("ME")["Salary"].sum())
# print(df.resample("ME")["Bonus"].mean())
# df.to_excel("employee_monthly_dashboard.xlsx",index=False)

#----------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# sales = pd.DataFrame({
#     "Time":[
#         "2026-01-01 09:05",
#         "2026-01-01 09:20",
#         "2026-01-01 09:45",
#         "2026-01-01 10:10",
#         "2026-01-01 10:40"
#     ],
#     "Product":[
#         "Laptop","Mouse","Keyboard","Laptop","Monitor"
#     ],
#     "Quantity":[2,1,3,2,1]
# })
#
# prices = pd.DataFrame({
#     "Time":[
#         "2026-01-01 09:00",
#         "2026-01-01 09:30",
#         "2026-01-01 10:00",
#         "2026-01-01 10:30"
#     ],
#     "UnitPrice":[
#         50000,
#         700,
#         51000,
#         12000
#     ]
# })
# print(sales.info())
# print(prices.info())
# sales["Time"]=pd.to_datetime(sales["Time"])
# prices["Time"]=pd.to_datetime(prices["Time"])
# print(sales.dtypes)
# print(prices.dtypes)
# sales=sales.sort_values(by="Time")
# prices=prices.sort_values(by="Time")
# print(sales)
# print(prices)
# # df=pd.merge_asof(sales,prices,on="Time")
# # df=pd.merge_asof(sales,prices,on="Time",direction="forward")
# df=pd.merge_asof(sales,prices,on="Time",direction="nearest")
# # df=pd.merge_asof(sales,prices,on="Time",tolerance=pd.Timedelta("20min"))
# df["TotalSale"]=df["Quantity"]*df["UnitPrice"]
# print(df)
# print(df.groupby("Product")["TotalSale"].sum())
# print(df.groupby("Product")["TotalSale"].sum().idxmax())
# df.to_excel("merge_asof_practice.xlsx",index=False)

#bonus1
# try:
#     df=pd.read_excel('merge_asof_practice.xlsx')
# except Exception as e:
#     print(e)
#
# print(df.info())
# df["Price_Change"]=df["UnitPrice"].diff()
# print(df)
# print(df["Price_Change"].max())
# print(df["Price_Change"].min())
# #bonus2
# df["Price_Growth_%"]=df["UnitPrice"].pct_change()*100
# df["Price_Classify"]=df["Price_Growth_%"].apply(lambda x:"Increasing" if x>0 else("Decreasing" if x<0 else "Stable"))
# print(df)

#mixed1

# try:
#     df=pd.read_csv("mixed1_mergeasof.csv")
# except Exception as e:
#     print(e)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.columns)
# df["sale_date"]=pd.to_datetime(df["sale_date"])
# print(df.dtypes)
# df["sales"]=df["sales"].fillna(df["sales"].mean())
# df["bonus"]=df["bonus"].fillna(df["bonus"].mean())
# print(df.isna().sum())
# df=df.drop_duplicates()
# print(df.duplicated().sum())
# #no needs to lean column names rename(),replace()
# df=df.sort_values("price",ascending=False)
# # i have not two files of can not use the merge_asof()
# print(df.query("department=='Electronics'"))
# print(df.groupby("department")["revenue"].mean())
# df["average_sales_by_department"]=df.groupby("department")["sales"].transform("mean")
# df["rank_by_department_salary"]=df.groupby("department")["revenue"].rank(ascending=True,method="dense")
# df["3day_rolling_average_sale"]=df["sales"].rolling(3,min_periods=1).mean()
# df["previous_sales"]=df["sales"].shift(1)
# df["sales_growth%"]=df["sales"].pct_change()*100
# print(df)
# print(df.pivot_table(index="department",columns="city",values="bonus",aggfunc="mean",fill_value=0))
# # Business Questions:
# print(df.nlargest(1,"sales")[["employee_id","employee_name","department","city","sale_date","sales"]])
# print(df.groupby("department")["revenue"].sum().idxmax())
# print(df.groupby("city")["sales"].sum())
# df["pervious_price"]=df["sales"].shift(1)
# df["price_growth%"]=df["sales"].pct_change()*100
# print(df.nlargest(1,"price_growth%"))
# print(df.sort_values("revenue",ascending=False).head(3))
# df.to_csv("mixed1_merge_asof_final.csv",index=False)

# mixed2

# try:
#     orders=pd.read_csv("mixed2_mergeaosf_order.csv")
#     history_order=pd.read_csv("mixed2_mergeaosf_price_history.csv")
#     customers=pd.read_csv("mixed2_mergeasof_customers.csv")
# except Exception as e:
#     print(e)

# print(orders.info())
# print(history_order.info())
# print(customers.info())
# me=pd.merge(orders,customers,on="customer_id",how="inner")
# df=pd.merge(me,history_order,on="product_id",how="inner")
# print(df)
# print(df.columns)
# df["order_date"]=pd.to_datetime(df["order_date"])
# df["price_date"]=pd.to_datetime(df["price_date"])
# print(df.dtypes)
# df["city"]=df["city"].fillna("Unknown")
# df["price"]=df["price"].fillna(df["price"].mean())
# print(df.isna().sum())
# df=df.drop_duplicates()
# print(df.duplicated().sum())
# #i can't use the mergeasof becuase of only two table have the date data 
# print(df.query("city=='Ahmedabad' and price>500"))
# print(df.groupby("segment")["price"].mean())
# print(df.columns)
# df["city_average_price"]=df.groupby("city")["price"].transform("mean")
# df["quantity_category"]=pd.cut(df["quantity"],
# bins=[1,3,4,float("inf")],
# labels=["Low","Medium","High"],
# include_lowest=True)
# df["quantile_price"]=pd.qcut(df["price"],
# q=4,
# labels=["Q1","Q2","Q3","Q4"])
# print(df)
# # I DO NOT DO THIS ALL BECAUSE I COMEPELETED ALREADY ABOVE rank()
# # corr()
# # rolling()
# # pct_change()
# # # pivot_table()
# print(pd.crosstab(index=df["city"],columns="cutomer_id",normalize=True)*100)
# # Business Questions:
# df["previous_price"]=df["price"].shift(1)
# print(df)
# df["revenue"]=df["quantity"]*df["price"]
# print(df.groupby("customer_name")["revenue"].sum())
# print(df.groupby("product_id")["revenue"].sum())
# print(df.columns)
# df=df.set_index("order_date")
# print(df)
# print(df.resample("ME")["price_date"].count())
# #thier are no growth because of the answer is the : order_date
# # 2024-01-31    12
# # 2024-02-29    12
# # 2024-03-31    12
# # 2024-04-30    12
# # 2024-05-31    12

# print(df.sort_values("revenue",ascending=False).head(1))
# print(df.groupby("customer_id")["price"].sum())
# df.to_csv("customer_price_analysis.xlsx",index=False)

#mixed3

# try:
#     excel=pd.read_excel("sales_logs.xlsx",sheet_name=None)
#     print(excel.keys())
# except Exception as e:
#     print(e)

# orders=excel["Orders"]
# price_history=excel["PriceHistory"]  
# emp=excel["Employees"]

# print(orders.info())
# print(price_history.info())
# print(emp.info())

# me=pd.merge(orders,price_history,on="ProductID",how="inner")
# df=pd.merge(me,emp,on="EmployeeID",how="inner")
# print(df)
# print(df.columns)
# print(df.dtypes)
# i do not do more because of all things are above 

#----------------------------------------------------------------------------

# import pandas as pd
#
# df = pd.DataFrame({
#     "Day":[1,2,3,4,5,6,7,8],
#     "Sales":[100,120,150,180,200,220,250,300],
#     "Profit":[20,25,30,40,45,50,60,70]
# })
#
# df["Running_Total_Sales"]=df["Sales"].expanding().sum()
# df["Running_Average_Sales"]=df["Sales"].expanding().mean()
# df["Running_Max_Sales"]=df["Sales"].expanding().max()
# df["Running_Min_Sales"]=df["Sales"].expanding().min()
# df["Running_STD_Sales"]=df["Sales"].expanding().std()
# df["Running_Total_Profit"]=df["Profit"].expanding().sum()
# print(df.nlargest(1,"Running_Total_Sales")[["Day","Running_Total_Sales"]])
# print(df.nlargest(1,"Running_Average_Sales")[["Day","Running_Average_Sales"]])
# df["Profit_Percentage"]=df["Profit"]/df["Sales"]*100
# # df.to_excel("expanding_analysis.xlsx",index=False)
#
# #bonus1
# df["Sales_Growth"]=df["Sales"].diff()
# df["Running_Average_Growth"]=df["Sales_Growth"].expanding().mean()
# # Business Question:
# # Is average daily growth increasing over time?answer is yes
# #bonus2
# df["Running_Profit_Margin"]=df["Running_Total_Profit"]/df["Running_Total_Sales"]*100
# df["Category_Of_Running_profit_Margin"]=df["Running_Profit_Margin"].apply(lambda x:"Excellent" if x>=25 else("Good" if x>=20 else "Average"))
# print(df)

#-----------------------------------------------------------------------------------------------

# import pandas as pd
#
#
# df = pd.DataFrame({
#     "Employee":[
#         "Rahul",
#         "Neha",
#         "Amit",
#         "Priya",
#         "Manthan"
#     ],
#     "Department":[
#         "IT",
#         "HR",
#         "IT",
#         "Finance",
#         "Sales"
#     ],
#     "Skills":[
#         "Python,SQL,Excel",
#         "Excel,Power BI",
#         "Python,Pandas",
#         "Excel,Tally",
#         "Python,Excel,Power BI"
#     ]
# })
# df["Skills"] = df["Skills"].str.split(",")
# df=df.explode("Skills",ignore_index=True) # i can not use the reset_index i used the igonre_index
# print(df)
# print(df["Skills"].value_counts())
# print(df.query("Skills=='Python'"))
# print(df["Skills"].nunique())
# print(df["Skills"].value_counts().idxmax())
# print(df.pivot_table(index="Department", columns="Skills", values="Employee", aggfunc="count",fill_value=0))
# print(pd.crosstab(index=df["Department"],columns=df["Skills"],normalize=True)*100)
# df.to_excel("employee_skills_analysis.xlsx",index=False)
#
# #bonus1
# skills_level={
#     "Python":"Advanced",
#     "SQL":"Intermediate",
#     "Excel":"Basic",
#     "Power BI": "Intermediate",
#     "Pandas":"Advanced",
#     "Tally":"Basic"
# }
# df["Skill_Level"]=df["Skills"].map(skills_level)
# print(df)
# # bonus2
# # Top 3 most common skills
# # Least common skill
# # Department having the highest number of Python users
# print(df["Skills"].value_counts().nlargest(3))
# print(df["Skills"].value_counts().nsmallest(3))
# skills_df=df.query("Skills=='Python'")
# print(skills_df["Department"].value_counts().idxmax())

#mixed1

# try:
#     data=pd.read_csv("mixed1_exploed_data.csv",engine="python",on_bad_lines='skip')
#     manager=pd.read_csv("mixed1_exploed_manager.csv")
# except Exception as e:
#     print(e)
#
# data.columns=data.columns.str.strip().str.lower().str.replace(" ","_")
# data=data.rename(columns={
#     "emp_id":"employee_id"
# })
# data["joining_date"]=pd.to_datetime(data["joining_date"],format="mixed")
# data["salary"]=data["salary"].fillna(data["salary"].median())
# data["city"]=data["city"].fillna("Unknown")
# data["manager_id"]=data["manager_id"].fillna("Unknown")
# data["department"]=data["department"].replace({
#     "it":"IT"
# })
# data["skills"] = data["skills"].str.split(",")
# data=data.explode("skills")
# data["skills"]=data["skills"].str.strip().str.title()
# print(data)
#
# manager.columns=manager.columns.str.strip().str.lower().str.replace(" ","_")
# df=pd.merge(data,manager,on="manager_id",how="inner")
# print(df.query("region=='South'"))
# print(df.groupby("department")["salary"].mean())
# df["total_department_salary"]=df.groupby("department")["salary"].transform("sum")
# df["department_salary_rank"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# df["salary_category"]=pd.cut(df["salary"],
#                              bins=[45000,70000,85000,float("inf")],
#                              labels=["Low","Medium","High"],include_lowest=True)
# df["salary_q"]=pd.qcut(df["salary"],q=4,labels=["Q1","Q2","Q3","Q4"])
# print(df)
# #their no parameter to use proper : rolling()
# # expanding()
# # shift()
# # pct_change()
#
# print(df.pivot_table(index="city",columns="skills",values="salary",aggfunc="mean",fill_value=0))
# # Business Questions:
#
# print(df["skills"].value_counts().idxmax())
# python_df=df.query("skills=='Python'")
# print(python_df["department"].value_counts().idxmax())
# print(df.groupby("skills")["salary"].mean())
# # Highest paid SQL developer
# sql_df=df.query("skills=='Sql'")
# print(sql_df)
# print(sql_df.nlargest(1,"salary"))
# print(python_df["skills"].count())

#mixed2

# try:
#     emp=pd.read_csv("mixed2_explode_emp.csv")
#     project=pd.read_csv("mixed2_explode_project.csv")
# except Exception as e:
#     print(e)

# emp.columns=emp.columns.str.strip().str.lower()
# emp=emp.rename(columns={
#     'empid':"employee_id",
#     'joindate':"joining_date",
# })
# emp["joining_date"]=pd.to_datetime(emp["joining_date"])
# emp["salary"]=emp["salary"].fillna(emp["salary"].median())
# emp["projects"]=emp["projects"].fillna("Unknown")
# emp["projects"]=emp["projects"].str.split(",")
# emp=emp.explode("projects")

# print(project.info())
# project.columns=project.columns.str.strip().str.lower()
# project=project.rename(columns={
#     'projectid':"project_id",
#     "empid":"employee_id",
#     'projectname':"project_name",
#     'startdate':"start_date",
#     'enddate':"end_date"
# })
# project["start_date"]=pd.to_datetime(project["start_date"])
# project["end_date"]=pd.to_datetime(project["end_date"])
# project["end_date"]=project["end_date"].fillna(project["end_date"].mean())
# print(project.columns)
# print(project.dtypes)
# print(project.isna().sum())
# print(project.duplicated().sum())
# print(project)
# print(emp)

# df=pd.merge(emp,project,on="employee_id",how="inner")
# print(df.query("department=='IT'"))
# print(df.groupby("department")["salary"].mean())
# df["department_wise_salaryrank"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# # thier are no parameter to use this# rolling()# expanding()
# print(df.corr(numeric_only=True))
# df["department_wise_salary_avrage"]=df.groupby("department")["salary"].transform("mean")
# print(df)
# print(df.pivot_table(index="project_name",columns="status",values="salary",aggfunc="count",fill_value=0))
# print(pd.crosstab(index=df["department"],columns=df["projects"],normalize=True))

# # Business Questions:

# # Most used project technology
# print(df["projects"].value_counts().idxmax())
# # Employee working on the maximum technologies
# top_employee = df.groupby('employee_id')['projects'].nunique().idxmax()

# print(f"Top Employee ID: {top_employee}")

# print(df.groupby("department")["projects"].count())

# print(df.groupby("projects")["salary"].max())

# # Technology growth report
# # i have no parameter to find it

#----------------------------------------------------------------------------------------------

# import pandas as pd

# sales = pd.DataFrame({
#     "Date":[
#         "2026-01-01",
#         "2026-01-03",
#         "2026-01-05",
#         "2026-01-07",
#         "2026-01-10"
#     ],
#     "Department":[
#         "IT","IT","HR","HR","Sales"
#     ],
#     "Sales":[
#         1000,1500,1200,1800,2200
#     ]
# })

# targets = pd.DataFrame({
#     "Date":[
#         "2026-01-02",
#         "2026-01-04",
#         "2026-01-06",
#         "2026-01-08",
#         "2026-01-10"
#     ],
#     "Department":[
#         "IT","IT","HR","HR","Sales"
#     ],
#     "Target":[
#         1200,1600,1300,1900,2100
#     ]
# })
# sales["Date"]=pd.to_datetime(sales["Date"])
# targets["Date"]=pd.to_datetime(targets["Date"])

# print(sales.dtypes)
# print(targets.dtypes)

# df = pd.merge_ordered(
#     sales, 
#     targets,    
#     on="Date", 
#     left_by="Department", 
#     fill_method="ffill"
# )
# df=df.drop(columns=(["Department_x","Department_y"]))
# df["Target_Gap"]=df["Sales"]-df["Target"]
# print(df.nlargest(1,"Sales"))
# print(df.nlargest(1,"Target"))
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# print(df.query("`Achievement_%`>= 100"))
# # df.to_excel("merge_ordered_analysis.xlsx",index=False)

# #bonus1
# df["Sales_Growth_%"]=df["Sales"].pct_change()*100
# print(df.nlargest(1,"Sales_Growth_%"))
# #bonus2
# df["Performance"]=df["Achievement_%"].apply(lambda x:"Target Achieved" if x>=100 else "Below Target")
# print(df)
# print(df.query("Performance=='Target Achieved'")["Performance"].value_counts())
# print(df.query("Performance=='Below Target'")["Performance"].value_counts())
# #if you both show together
# print(df["Performance"].value_counts())
# # Target achievement percentage
# print(df.query("Performance=='Target Achieved'")["Performance"].value_counts()/df["Performance"].count()*100)

# print(df["Performance"].value_counts()/df["Performance"].count()*100)

#mixed1:
# try:
#     df=pd.read_csv("mixed1_merge_ordered.csv")
# except Exception as e:
#     print(e)

# print(df.info())
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# df=df.rename(columns={
#     'employee':"employee_name",
#     'salary_($)':"salary",
#     'sales_amount':"sales"
# })
# print(df.columns)
# df["date"]=pd.to_datetime(df["date"],format="mixed")
# df["salary"]=df["salary"].str.strip().str.replace(",","").str.replace("₹","")
# df["salary"]=pd.to_numeric(df["salary"])
# df["salary"]=df["salary"].fillna(df["salary"].median())
# print(df.dtypes)
# print(df.isna().sum())
# print(df.duplicated().sum())
# df["department"]=df["department"].str.strip().str.title()
# df["skills"]=df["skills"].str.split(";")
# df=df.explode("skills")
# df["skills"]=df["skills"].str.strip().str.title().replace({
#     'Sql':"SQL",
#     'Power Bi':"Power BI",
#     'Seo':"SEO"
# })
# print(df.query("department=='Sales' and sales>150000"))
# print(df.groupby("department")["sales"].mean())
# df=df.sort_values("date")
# df["sales_average_by_department"]=df.groupby("department")["sales"].transform("mean")
# df["rank_by_sale"]=df["sales"].rank(ascending=False,method="dense")
# df["sales_category"]=pd.cut(df["sales"],
# bins=[54000,200000,400000,float("inf")],
# labels=["Low","Medium","High"],include_lowest=True)
# df["salary_q"]=pd.qcut(df["salary"],q=4,labels=["Q1","Q2","Q3","Q4"])
# df["rolling_3days_average_sale"]=df["sales"].rolling(3,min_periods=1).mean()
# df["previous_day_sale"]=df["sales"].shift(1)
# df["sales_different"]=df["sales"].diff()
# df["sales_growth%"]=df["sales"].pct_change()*100
# df["running_sale_mean"]=df["sales"].expanding().mean()
# print(df)
# print(df["sales"].corr(df["target"])) #0.33393828915676244 low positive realtion
# print(df.pivot_table(index="department",columns="skills",values="salary",aggfunc="mean",fill_value=0))
# df = df.reset_index(drop=True)
# print(pd.crosstab(df["employee_name"], df["department"], normalize=True)*100)
# # merge_ordered() i can not use this because no extra file
# # Business questions:
# print(df.nlargest(1,"sales")[["employee_name","department","sales","target"]])
# print(df.groupby("department")[["sales","target"]].mean().idxmax())
# print(df.nlargest(1,"salary")[["employee_name","department","salary","sales","target"]])

# # Most common skill
# print(df["skills"].value_counts().idxmax())
# # Best target achievement
# df["achievement_%"]=df["sales"]/df["target"]*100
# df["performance"]=df["achievement_%"].apply(lambda x:"Target Achieved" if x>=100 else "Below Target")
# print(df.query("performance=='Target Achieved'").nlargest(1,"achievement_%"))

# # Highest sales-growth day
# print(df.nlargest(1,"sales_growth%"))
# print(df.columns)

# try:
#     emp=pd.read_csv("mixed2_mereg_ordered_emp.csv")
#     sales=pd.read_csv("mixed2_mereg_ordered_sales.csv")
#     target=pd.read_csv("mixed2_mereg_ordered_target.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(sales.info())
# print(target.info())

# df=pd.merge(emp,sales,on="employee_id",how="inner")
# df=pd.merge(df,target,on="employee_id",how="inner")
# df["target_date"]=pd.to_datetime(df["target_date"])
# df["sale_date"]=pd.to_datetime(df["sale_date"])
# df["sales_amount"]=df["sales_amount"].fillna(df["sales_amount"].mean())
# df["monthly_target"]=df["monthly_target"].fillna(df["monthly_target"].mean())
# df=df.drop_duplicates()
# #no needs to merge_ordered()
# df["skills"]=df["skills"].str.split(";")
# df=df.explode("skills")
# print(df.groupby("region")["sales_amount"].mean())
# df["sale_average_by_region"]=df.groupby("region")["sales_amount"].transform("mean")
# df["salary_rank"]=df["salary"].rank(ascending=False,method="dense")
# df=df.sort_values("sale_date")
# df["3days_average_rolling_sale"]=df["sales_amount"].rolling(3,min_periods=1).mean()
# df["running_mean_sale"]=df["sales_amount"].expanding().mean()
# df["previous_sale"]=df["sales_amount"].shift(1)
# df["sale_growth%"]=df["sales_amount"].pct_change()*100
# print(df)
# print(df.corr(numeric_only=True))
# print(df.pivot_table(index="region",columns="skills",values="salary",aggfunc="mean",fill_value=0))
# # Business questions:

# # Department-wise sales
# print(df.groupby("department")["sales_amount"].mean())
# # Employee salary rank done above
# # Target achievement
# print(df.columns)
# print(df[["sale_date","sales_amount","target_date","monthly_target"]])
# # df["sale_month_name"]=df["sale_date"].dt.month_name() thier are only 1 month so i could not find it proper
# # 7-day rolling sales 
# df["7day_rolling_total_sale"]=df["sales_amount"].rolling(7,min_periods=1).sum()
# # Running sales total above done
# # Sales growth above done 
# # Salary vs sales correlation
# # print(df["salary"].corr(df["sales_amount"])) 0.2481425523407544

#--------------------------------------------------------------------------------------------

# import pandas as pd

# df = pd.DataFrame({
#     "Department":["IT","HR","Finance","Sales"],
#     "Ahmedabad":[50000,60000,70000,65000],
#     "Surat":[55000,62000,75000,68000],
#     "Mumbai":[58000,64000,72000,70000]
# })


# df=df.set_index("Department")
# df=df.stack()
# print(df)
# df=df.unstack()
# print(df)
# df_stacked = df.stack()
# df_long = df_stacked.reset_index()
# df_long.columns = ["Department", "City", "Salary"]

# print(df_long)

# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Sales":[50000,55000,60000,65000]
# })
# df=df.set_index(["Department","City"])
# print(df)
# # df=df.unstack()
# # print(df)

# df=df.unstack(level="City")
# print(df)
# df=df.stack()
# print(df)

# df = pd.DataFrame({
#     "Department":["IT","HR","Finance"],
#     "Sales":[100000,80000,90000],
#     "Profit":[20000,15000,18000]
# })
# df=df.set_index("Department")
# print(df)
# df=df.stack()
# print(df)
# df=df.unstack()
# print(df.groupby("Department")["Sales"].sum().idxmax())
# print(df.nlargest(1,"Profit"))

# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Sales":[50000,55000,60000,65000]
# })

# df_pivot_table=df.pivot_table(index="Department",columns="City")
# print(df_pivot_table)
# df_stack=df_pivot_table.stack()
# print(df_stack)
# df_unstack=df_stack.unstack()
# print(df_unstack)

# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR","Finance","Finance"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Sales":[50000,55000,60000,65000,70000,75000]
# })
# df=df.set_index(["Department","City"])
# print(df)
# print(df.nlargest(1,"Sales"))
# df=df.unstack()
# print(df)
# df=df.stack()
# print(df)
# df.to_excel("stack_unstack_analysis.xlsx",index=False)

#bonus1
# df = pd.DataFrame({
#     "Department":["IT","HR","Finance"],
#     "Ahmedabad":[50000,60000,70000],
#     "Surat":[55000,65000,75000],
#     "Mumbai":[58000,62000,72000]
# })
# df = df.set_index("Department") 
# df_stacked = df.stack() 
# df_long = df_stacked.reset_index() 
# df_long.columns = ["Department", "City", "Salary"]
# print(df_stacked)
#bonus2
# print(df_long.groupby("City")["Salary"].mean().idxmax())  
# print(df_long.groupby("Department")["Salary"].sum().idxmax())  
# print(df_long.nlargest(1,"Salary"))
# print(df.unstack())
#mixed1
# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","IT","HR","HR","Finance","Finance"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai","Ahmedabad","Surat"],
#     "Salary":[50000,70000,60000,80000,90000,110000],
#     "Rating":[4.2,4.8,3.9,4.7,4.5,4.9]
# })
# print(df)
# print(df.groupby("Department")["Salary"].mean())
# df["Department_wise_Salary_rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# df["Salary_Category"]=pd.cut(df["Salary"],
# bins=[50000,70000,90000,float("inf")],
# labels=["Low","Medium","High"],include_lowest=True)
# df["Salary_Quartile"]=pd.qcut(df["Salary"],q=4,labels=["Q1","Q2","Q3","Q4"])
# print(df)
# pivot_table_salary=df.pivot_table(index="Department",columns="City",values="Salary",aggfunc="sum",fill_value=0)
# print(pivot_table_salary)
# pivot_table_salary=pivot_table_salary.stack()
# print(pivot_table_salary)
# pivot_table_salary=pivot_table_salary.unstack()
# print(pivot_table_salary)
# print(df.nlargest(1,"Salary"))
# print(df.groupby("Department")["Salary"].mean().idxmax())

#mixed2
# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR","Finance","Finance"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Sales":[50000,60000,55000,70000,80000,90000],
#     "Profit":[10000,12000,11000,15000,18000,20000]
# })

# df["Profit_%"]=df["Profit"].pct_change()*100
# print(df.groupby("Department")["Sales"].mean())
# print(df.groupby("Department")["Profit"].mean())
# df["Rank_Sale_Department"]=df.groupby("Department")["Sales"].rank(ascending=False,method="dense")
# print(df)
# pivot_table_sales=df.pivot_table(index="Department",columns="City",values="Sales",aggfunc="sum")
# print(pivot_table_sales)
# pivot_table_sales=pivot_table_sales.stack()
# print(pivot_table_sales)
# pivot_table_sales=pivot_table_sales.unstack()
# print(pivot_table_sales)
# print(df.nlargest(1,"Sales"))
# print(df.nlargest(1,"Profit"))
# print(df.groupby("Department")["Sales"].mean())

#mixed3
# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR","Sales","Sales"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Sales":[120000,135000,90000,95000,150000,165000],
#     "Quantity":[20,25,15,18,30,35],
#     "Profit":[24000,27000,18000,19000,30000,33000]
# })
# pivot_sale=df.pivot_table(index="Department",columns="City",values="Sales",aggfunc="sum")
# print(pivot_sale)
# pivot_profit=df.pivot_table(index="Department",columns="City",values="Profit",aggfunc="sum")
# print(pivot_profit)
# pivot_quantity=df.pivot_table(index="Department",columns="City",values="Quantity",aggfunc="sum")
# print(pivot_quantity)
# print(df.groupby("Department")["Sales"].sum().idxmax())
# print(df.groupby("City")["Sales"].sum().idxmax())
# print(df.groupby("Department")["Profit"].sum().idxmax())
# print(df.groupby("City")["Quantity"].sum().idxmax())
# print(df.nlargest(1,"Sales"))
# print(df.groupby("Department")["Sales"].mean().idxmax())
# print(df.groupby("Department")["Profit"].mean().idxmax())

#--------------------------------------------------------------------------------------

# import pandas as pd

# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR","Finance","Finance"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Salary":[50000,70000,60000,80000,90000,110000],
#     "Sales":[100000,120000,90000,95000,130000,150000]
# })
# print(df)
# df=df.set_index(["Department","City"])
# print(df)
# print(df.loc["IT"])
# print(df.loc[("IT","Ahmedabad")])   
# df=df.reset_index()
# print(df)
# df=df.set_index(["Department","City"])
# print(df)
# df=df.sort_index()
# print(df)
# cities = df.index.get_level_values("City")
# print(cities)
# groupby_department_city=df.groupby(["Department","City"])["Salary"].mean()
# print(groupby_department_city)
# unstack_city=df.unstack(level="City")
# print(unstack_city)
# ahmedabad_employees = df.xs("Ahmedabad", level="City")
# print(ahmedabad_employees)
# print(df.groupby(["Department","City"])["Salary"].mean().idxmax())
# print(df.groupby(["Department","City"])["Sales"].mean().idxmax())

# #bonus1
# groupby_department_city=df.groupby(["Department","City"])["Sales"].agg(["sum","max","min","mean"])
# print(groupby_department_city)
# groupby_department_city_normal=groupby_department_city.reset_index()
# print(groupby_department_city_normal)
# #bonus2
# groupby_sales_salary=df.groupby(["Department","City"])[["Sales","Salary"]].agg(["mean","max"])
# print(groupby_sales_salary)
# print(df.index)
# print(df.columns)
# print(groupby_sales_salary.index)
# print(groupby_sales_salary.columns)
# print(groupby_sales_salary["Salary"])
# print(groupby_sales_salary["Salary","mean"])
# df.columns = ['_'.join(col).strip() for col in df.columns.values]
# print(df.columns)

# mixed1
# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR","Finance","Finance"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Salary":[50000,70000,60000,80000,90000,110000],
#     "Sales":[100000,120000,90000,95000,130000,150000]
# })
# print(df)
# df=df.set_index(["Department","City"]).sort_index()
# print(df)
# print(df.loc["IT"])
# average_salary_by_department_city=df.groupby(["Department","City"])["Salary"].mean()
# print(average_salary_by_department_city)
# salary_rank_department=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(salary_rank_department)
# department_wise_average_salary=df.groupby("Department")["Salary"].transform("mean")
# print(department_wise_average_salary)
# pivot_table_department_city_salary=df.pivot_table(index="Department",columns="City",values="Salary",aggfunc="sum")
# print(pivot_table_department_city_salary)
# pivot_table_department_city_salary_stack=pivot_table_department_city_salary.stack()
# print(pivot_table_department_city_salary_stack)
# pivot_table_department_city_salary_unstack=pivot_table_department_city_salary_stack.unstack()
# print(pivot_table_department_city_salary_unstack)
# pivot_table_department_city_salary_normal=pivot_table_department_city_salary_unstack.reset_index()
# print(pivot_table_department_city_salary_normal)
# df=df.reset_index()
# print(df)

#mixed2

# df = pd.DataFrame({
#     "Department":["IT","IT","HR","HR","Finance","Finance"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Surat","Ahmedabad","Surat"],
#     "Sales":[100000,120000,90000,95000,130000,150000],
#     "Profit":[20000,25000,18000,22000,30000,35000],
#     "Employees":[5,6,4,5,7,8]
# })
# df=df.set_index(["Department","City"])
# df["Profit_%"]=df["Sales"]/df["Profit"]*100
# print(df)
# groupby_department_city=df.groupby(["Department","City"])
# average_sale_profit=groupby_department_city[["Sales","Profit"]].mean()
# print(average_sale_profit)
# print(average_sale_profit["Sales"].nlargest(1))
# print(average_sale_profit["Profit"].nlargest(1))
# department_city_profit_pivot_table=df.pivot_table(index="Department",columns="City",values="Profit",aggfunc=(["mean","max","min","sum","count"]))
# print(department_city_profit_pivot_table)
# department_city_profit_pivot_table_stack=department_city_profit_pivot_table.stack()
# print(department_city_profit_pivot_table_stack)
# print(department_city_profit_pivot_table_stack.xs("Ahmedabad",level="City"))
# print(df)
# df=df.reset_index()
# print(df)
# df.to_excel("mixed2_multiindex_final.xlsx",index=False)

#mixed3

# try:
#     emp=pd.read_csv("mixed3_multiindex_emp.csv")
#     sales=pd.read_csv("mixed3_multiindex_sale.csv")
#     attendance=pd.read_csv("mixed3_multiindex_attendance.csv")
# except Exception as e:
#     print(e)


# emp.columns=emp.columns.str.strip().str.lower().str.replace(" ","_")
# emp["salary"]=emp["salary"].fillna(emp["salary"].median())
# emp=emp.drop_duplicates()

# sales.columns=sales.columns.str.strip().str.lower().str.replace(" ","_")
# sales["date"]=pd.to_datetime(sales["date"])
# sales["sales"]=sales["sales"].fillna(sales["sales"].mean())
# sales=sales.drop_duplicates()

# attendance.columns=attendance.columns.str.strip().str.lower().str.replace(" ","_")
# attendance["present_days"]=attendance["present_days"].fillna(attendance["present_days"].mean()).astype(int)
# attendance=attendance.drop_duplicates()

# df=pd.merge(emp,sales,on="employee_id",how="inner")
# df=pd.merge(df,attendance,on="employee_id",how="inner")

# df["attendance_%"]=df["present_days"]/df["working_days"]*100
# df=df.set_index(["department","city"])
# print(df["salary"].mean())
# print(df["sales"].sum()) 
# print(df["attendance_%"].mean()) 

# highest_selling_department_city=df.groupby(["department","city"])["sales"].sum().idxmax()
# print(highest_selling_department_city)
# highest_average_salary_department_city=df.groupby(["department","city"])["salary"].mean().idxmax()
# print(highest_average_salary_department_city)
# print(df.xs("Ahmedabad",level="city"))
# #i can not unstack because of the duplicates values contain if i drop my data is not good for analysis
# df=df.reset_index()
# print(df)

#------------------------------------------------------------------------------------------------
# import pandas as pd

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Department":["IT","HR","IT","HR","Finance","Finance","IT","HR"],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,65000],
#     "Performance":[
#         "Average","Good","Average","Excellent",
#         "Good","Excellent","Good","Average"
#     ],
#     "Status":[
#         "Active","Active","Inactive","Active",
#         "Active","Inactive","Active","Active"
#     ]
# })
# print(df.dtypes)
# print(df)
# df["Department"]=df["Department"].astype("category")
# print(df.dtypes)
# print(df["Department"].dtypes)
# print(df["Department"].cat.categories)
# print(df["Department"].unique())
# df["Performance"] = pd.Categorical(
#     df["Performance"],
#     categories=[
#         "Poor",
#         "Average",
#         "Good",
#         "Excellent"
#     ],
#     ordered=True
# )
# print(df["Performance"].cat.categories)
# df=df.sort_values("Performance")
# print(df)
# print(df[df["Performance"]>"Average"])
# df["Department"]=df["Department"].cat.add_categories(["Marketing"])
# print(df["Department"].unique())
# df["Department"]=df["Department"].cat.rename_categories({"IT":"Information Technology","HR":"Human Resources"})
# print(df)
# print(df["Performance"].value_counts())
# print(df["Performance"].value_counts().idxmax())
# print(df.groupby("Performance", observed=True)["Salary"].mean())
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[0,60000,90000,float("inf")],labels=["Low","Medium","High"])
# print(df["Salary_Band"].dtypes)
# print(df["Salary_Band"].nunique())
# print(df.groupby("Salary_Band",observed=True)["Salary"].mean())

# #bonus1
# df["Performance_Score"]=df["Performance"].apply(lambda x:1 if x=="Poor"else(2 if x=="Average" else(3 if x=="Good" else 4)) )
# print(df)
# print(df.loc[df["Performance_Score"].idxmax(), ["Employee", "Department", "Salary", "Performance_Score"]])
# print(df.query("Performance>='Good'")["Salary"].mean())

# #bonus2

# df["Status"]=df["Status"].astype("category")
# print(df["Status"].unique())
# df["Status"]=df["Status"].cat.add_categories(["On Leave"])
# print(df["Status"].unique())
# df["Status"]=df["Status"].cat.rename_categories({"Active":"Working"})
# df["Status"]=df["Status"].cat.remove_unused_categories()
# print(df["Status"].unique())

# print(df)

#mixed1

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Department":["IT","HR","IT","HR","Finance","Finance","IT","HR"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai",
#             "Ahmedabad","Surat","Mumbai","Ahmedabad"],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,65000],
#     "Sales":[100000,120000,90000,95000,130000,150000,125000,105000],
#     "Performance":[
#         "Average","Good","Average","Excellent",
#         "Good","Excellent","Good","Average"
#     ]
# })
# df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.dtypes)
# print(df.columns)

# df[["department","city"]]=df[["department","city"]].astype("category")
# print(df.dtypes)
# df["performance"]=pd.Categorical(df["performance"],
#                                  categories=[
#         "Poor",
#         "Average",
#         "Good",
#         "Excellent"
#     ],
# ordered=True)

# print(df)
# print(df.isna().sum())
# print(df.groupby("department")["salary"].mean())
# df["salary_rank_department"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# df["salary_band"]=pd.cut(df["salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df["salary_quartile"]=pd.qcut(df["salary"],q=4,labels=["Q1","Q2","Q3","Q4"])
# print(df)
# print(df.groupby("performance")["salary"].mean())
# print(df.nlargest(1,"sales"))
# print(df.pivot_table(index="department",columns="city",values="salary",aggfunc="sum",fill_value=0))

# print(df["department"].value_counts().idxmax())

# #mixed2
# df["department"]=df["department"].cat.add_categories(["Marketing"])
# print(df["salary_band"].value_counts())
# groupby_department_salaryband=df.groupby(["department","salary_band"])
# print(groupby_department_salaryband["salary"].mean())
# print(groupby_department_salaryband["sales"].mean())

# df["sales_category"]=pd.cut(df["sales"],bins=[90000,120000,135000,float("inf")],labels=["Average","Good","Excellent"],include_lowest=True)
# print(df)
# print(df.groupby("sales_category")["sales"].mean().idxmax())
# df=df.sort_values("performance")
# print(df.query("performance>'Average'"))
# print(df.pivot_table(index="department",columns="performance",values="sales",aggfunc="mean",fill_value=0))

#mixed3
# employees = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105,106],
#     "Name":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","HR","IT","Finance","Finance","HR"],
#     "Performance":["Good","Excellent","Average","Good","Excellent","Average"]
# })

# salary = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105,106],
#     "Salary":[60000,80000,55000,90000,110000,70000]
# })

# sales = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105,106],
#     "Sales":[100000,130000,80000,120000,180000,95000]
# })
# df=pd.merge(employees,salary,on="EmployeeID",how="inner")
# df=pd.merge(df,sales,on="EmployeeID",how="inner")
# df["Department"]=df["Department"].astype("category")
# print(df.dtypes)
# df["Performance"]=pd.Categorical(df["Performance"],categories=["Poor","Average","Good","Excellent"],ordered=True)
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[55000,77000,90000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# print(df.groupby("Department",observed=True)["Salary"].mean())
# print(df.groupby("Department",observed=True)["Sales"].sum())
# df["Salary_Rank_Department"]=df.groupby("Department")["Salary"].rank(ascending=True,method="dense")
# print(df.query("Performance>'Average'"))
# print(df.groupby("Department",observed=True)["Sales"].sum().idxmax())
# print(df.pivot_table(index="Department",columns="Performance",values="Sales",aggfunc="mean",fill_value=0))
# print(df.nlargest(1,"Salary"))
# df.to_excel("mixed3_categories_final.xlsx",index=False)