# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Department":["IT","HR","IT","HR","Finance","Finance","IT","HR"],
#     "Sales":[500,1200,-300,1800,2500,700,3200,900],
#     "Target":[1000,1000,500,1500,2000,1000,3000,1200],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,65000],
#     "Rating":[3.2,4.1,2.8,4.5,4.7,4.9,4.2,3.5]
# })
# print(df)
# df["Valid_Sales"]=df["Sales"].where(df["Sales"]>=0,0)
# df["Sales_Above_Target"] = df["Sales"].where(df["Sales"] >= df["Target"], 0)
# df["Invalid_Sales"]=df["Sales"].mask(df["Sales"]<0)
# df["Rating_Cleaning"] = df["Rating"].where((df["Rating"] >= 3) & (df["Rating"] <= 5))
# df["Salary_Range"]=df["Salary"].where((df["Salary"]>=60000) & (df["Salary"]<=100000),0)
# df["Target_Status"] = np.where(df["Sales_Above_Target"] > 0, "Achieved", "Below Target")
# df["Department_Average_Sales"]=df.groupby("Department")["Sales"].transform("mean")
# df["Department_Average_Above_Sales"]=df["Sales"].where(df["Department_Average_Sales"]<df["Sales"],0)
# df["High_Performer_Sales"]=df["Rating"].mask(df["Rating"]<4,0)
# df["Valid_Sales_Range"]=df["Sales"].where((df["Sales"]>=500)&(df["Sales"]<=3000))
# df["Business_Flag"]=np.where((df["Department_Average_Above_Sales"]>0)&(df["Rating"]>=4),"Eligible","Not Eligible")
# #bonus1
# df["Department_Performance"]=np.where(df["Department_Average_Above_Sales"]>0,"Above Average","Below Average")
# print(df[df["Department_Performance"] == "Above Average"].value_counts())

# #bonus2
# # Sales < 0
# df["Sales"]=df["Sales"].mask(df["Sales"]<0)
# df["Rating"]=df["Rating"].mask((df["Rating"]<0)|(df["Rating"]>5))
# df["Salary"]=df["Salary"].mask(df["Salary"]<0)
# df["Target"]=df["Target"].mask(df["Target"]<0)
# print(df[["Sales","Rating","Salary","Target"]])
# print(df.isna().sum())

#mixed1
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Jay","Riya"],
#     "Department":["IT","HR","IT","HR","Finance","Finance","IT","HR"],
#     "Sales":[500,1200,-300,1800,2500,700,3200,900],
#     "Target":[1000,1000,500,1500,2000,1000,3000,1200],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,65000],
#     "Rating":[3.2,4.1,2.8,4.5,4.7,4.9,4.2,3.5],
#     "Performance":["Average","Good","Poor","Excellent",
#                    "Excellent","Excellent","Good","Average"]
# })
# print(df.isna().sum())
# df["Sales"]=df["Sales"].where(df["Sales"]>0,0)
# df["Achievement"]=np.where(df["Sales"]>df["Target"],"Achievement","Not Achievement")
# df["department_average_sales"]=df.groupby("Department")["Sales"].transform("mean")
# df["Sales_Above_Department"]=df["Sales"].where(df["Sales"]>df["department_average_sales"],0)
# df["Salary_Rank_Department"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# score_mapping={
#     "Poor":1,
#     "Average":2,
#     "Good":3,
#     "Excellent":4
# }
# df["Performance Score"]=df["Performance"].map(score_mapping)
# print(df)
# print(df.nlargest(1,"Sales"))
# print(df.nlargest(1,"Salary"))
# print(df.pivot_table(index="Department",columns="Performance",values="Salary",aggfunc="mean",fill_value=0))
# print(df.groupby("Department")["Sales"].mean().idxmax())

#mixed2
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F","G","H"],
#     "Department":["IT","IT","HR","HR","Finance","Finance","Sales","Sales"],
#     "Sales":[1000,2500,800,1800,3000,-500,2200,700],
#     "Target":[1200,2000,1000,1600,2500,1000,2000,1000],
#     "Profit":[100,500,80,350,700,-100,400,50],
#     "Rating":[3.5,4.8,3.2,4.4,4.9,2.5,4.2,3.1]
# })
# print(df)
# df["Sales"]=df["Sales"].where(df["Sales"]>0,0)
# df["Profit"]=df["Profit"].where(df["Profit"]>0,0)
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Achieved_Targets"]=np.where(df["Achievement_%"]>=100,"Achieved","Not Achieved")
# df["Profit_Status"]=pd.cut(df["Profit"],bins=[0,275,500,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df["department_sales_average"]=df.groupby("Department")["Sales"].transform("mean")
# df["Sales_Above_Avearge"]=df["Sales"].where(df["Sales"]>df["department_sales_average"],0)
# df["Sales_Growth%"]=df["Sales"].pct_change()*100
# df["Running_Average_Sales"]=df["Sales"].expanding().mean()
# df["3days_Average_Rolling_Sales"]=df["Sales"].rolling(3,min_periods=1).mean()
# print(df)
# print(df.groupby("Department")["Sales"].sum().idxmax())
# print(df.nlargest(1,"Profit"))

#mixed3
# import pandas as pd
# import numpy as np

# employees = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105,106],
#     "Name":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","HR","IT","Finance","Finance","HR"],
#     "Salary":[60000,80000,55000,90000,110000,70000]
# })

# sales = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105,106],
#     "Sales":[100000,130000,-5000,120000,180000,95000],
#     "Target":[90000,140000,100000,100000,150000,100000]
# })

# attendance = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105,106],
#     "WorkingDays":[22,22,22,22,22,22],
#     "PresentDays":[21,20,18,22,21,19]
# })
# df=pd.merge(employees,sales,on="EmployeeID",how="inner")
# df=pd.merge(df,attendance,on="EmployeeID",how="inner")
# print(df.isna().sum())
# df["Sales"]=df["Sales"].where(df["Sales"]>0,0)
# df["Attendance_%"]=df["PresentDays"]/df["WorkingDays"]*100
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Target_Status"]=np.where(df["Achievement_%"]>=100,"Achieved","Not Achieved")
# df["Department_Average_Sales"]=df.groupby("Department")["Sales"].transform("mean")
# df["Sale_Above_Department"]=df["Sales"].where(df["Sales"]>df["Department_Average_Sales"],0)
# df["Salary_Rank_Department"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[55000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# print(df)
# print(df.pivot_table(index="Department",columns="Target_Status",values="Sales",aggfunc="sum",fill_value=0))
# print(df.nlargest(1,"Sales"))
# print(df.groupby("Department")["Sales"].sum().idxmax())
# df.to_excel("mixed3_where_mask_final.xlsx",index=False)

#----------------------------------------------------------------------------------------------

# # import pandas as pd

# # df = pd.DataFrame({
# #     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
# #     "Department":["IT","HR","Finance","IT","HR","Finance"],
# #     "City":["Ahmedabad","Surat","Mumbai","Ahmedabad","Mumbai","Surat"],
# #     "Performance":["Good","Excellent","Average","Poor","Good","Excellent"],
# #     "Salary":[50000,70000,90000,60000,80000,110000]
# # })
# # print(df)
# # # df=pd.get_dummies(df,columns=["Department"])
# # # df=pd.get_dummies(df,columns=["Department","City"],dtype="int")
# # # df=pd.get_dummies(df,columns=["Performance"],dtype="int")
# # # df=pd.get_dummies(df,columns=["Department"],prefix="Dept")
# # # df=pd.get_dummies(df,columns=["City"],prefix="Location",prefix_sep="-",dtype="int")
# # # df=pd.get_dummies(df,columns=["Department"],prefix="Dept",drop_first=True)
# # df["Salary_Band"]=pd.cut(df["Salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# # df=pd.get_dummies(df,columns=["Salary_Band"],dtype="int")
# # print(df)
# # # df=pd.get_dummies(df,columns=["Department"],dtype="int")
# # # print(df.query("Department_IT==1"))
# # # df=pd.get_dummies(df,columns=["City"],prefix="City",dtype="int")
# # # print(df)
# # # print(df.query("`City_Ahmedabad`==1").groupby("City_Ahmedabad")["Salary"].mean())
# # # One-hot encode Department and Performance together using dtype=int.
# # df=pd.get_dummies(df,columns=["Department","Performance"],dtype="int")
# # print(df)

# #bonus1
# # import pandas as pd

# # df = pd.DataFrame({
# #     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
# #     "Department":["IT","HR","Finance","IT","HR","Finance"],
# #     "City":["Ahmedabad","Surat","Mumbai","Ahmedabad","Mumbai","Surat"],
# #     "Performance":["Good","Excellent","Average","Poor","Good","Excellent"],
# #     "Salary":[50000,70000,90000,60000,80000,110000],
# #     "Sales":[1200,2100,1500,900,2200,1700]
# # })
# # print(df)
# # df["Salary_Band"]=pd.cut(df["Salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# # df=pd.get_dummies(df,columns=["Department"],dtype="int")
# # df=pd.get_dummies(df,columns=["City"],dtype="int")
# # df=pd.get_dummies(df,columns=["Salary_Band"],dtype="int")
# # df=pd.get_dummies(df,columns=["Performance"],dtype="int")
# # print(df)
# # df.to_excel("bonus1_get_dummins_final.xlsx",index=False)

# #bonus2
# import pandas as pd

# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F"],
#     "Department":["IT","HR","IT","Finance","HR","IT"],
#     "Experience":[1,3,5,7,4,8],
#     "Salary":[40000,60000,80000,90000,70000,110000]
# })
# print(df)
# # df=pd.get_dummies(df,columns=["Department"])
# df=pd.get_dummies(df,columns=["Department"],dtype="int")
# print(df)
# print(df.query("Department_IT==1").groupby("Department_IT")["Salary"].mean())
# print(df.query("Department_IT==1").nlargest(1,"Salary"))

#mixed1
# import pandas as pd

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","HR","IT","Finance","HR","Finance"],
#     "City":["Ahmedabad","Surat","Mumbai","Ahmedabad","Mumbai","Surat"],
#     "Sales":[100000,120000,90000,150000,130000,110000],
#     "Salary":[50000,70000,60000,90000,80000,110000],
#     "Rating":[4.2,4.5,3.5,4.8,4.1,4.9]
# })
# print(df)
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df["Department_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# df=pd.get_dummies(df,columns=["Department","Salary_Band"],dtype="int")
# print(df)
# print(df.nlargest(1,"Sales"))
# # print(df.groupby("Department")["Salary"].mean())
# # print(df.groupby("Department")["Salary"].mean().idxmax())
# df.to_excel("mixed1_get_dummies_final.xlsx",index=False)

#mixed2
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F","G","H"],
#     "Department":["IT","IT","HR","HR","Finance","Finance","Sales","Sales"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai",
#             "Surat","Ahmedabad","Mumbai","Surat"],
#     "Sales":[1000,2500,800,1800,3000,2200,1500,2800],
#     "Target":[1200,2000,1000,1600,2500,2000,1800,2500],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,95000]
# })
# print(df)
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Target_Status"]=np.where(df["Sales"]>=df["Target"],"Achievement","Not Achievement")
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df["Department_Average_Sale"]=df.groupby("Department")["Sales"].transform("mean")
# df=pd.get_dummies(df,columns=["Department","City"],dtype="int")
# # df["Above_Department_Average"]=df["Sales"].where(df["Sales"]>df["Department_Average_Sale"],0)
# print(df)
# print(df.nlargest(1,"Sales"))
# print(df.query("Target_Status=='Achievement'").nlargest(1,"Target"))
# print(df.nlargest(1,"Achievement_%"))
# df.to_excel("mixed2_get_dummies_final.xlsx",index=False)

#mixed3
# import pandas as pd
# import numpy as np
# try:
#     emp=pd.read_csv("mixed3_get_dummies_emp.csv")
#     sales=pd.read_csv("mixed3_get_dummies_sales.csv")
#     attendance=pd.read_csv("mixed3_get_dummies_attendance.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(sales.info())
# print(attendance.info())
# df=pd.merge(emp,sales,on="EmployeeID",how="inner")
# df=pd.merge(df,attendance,on="EmployeeID",how="inner")
# df.columns=df.columns.str.strip().str.lower()
# df=df.rename(columns={
#     "employeeid":"employee_id",
#     "workingdays":"working_days",
#     "presentdays":"present_days"
# })
# df["attendance_%"]=df["present_days"]/df["working_days"]*100
# df["achievement_%"]=df["sales"]/df["target"]*100
# df["target_status"]=np.where(df["achievement_%"]>=100,"Achievement","Not Achievement")
# df["salary_band"]=pd.cut(df["salary"],bins=[60000,80000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df=pd.get_dummies(df,columns=["department","city"],dtype="int")
# print(df)
# print(df.nlargest(1,"sales"))
# # print(df.groupby("department")["sales"].mean().idxmax())
# # Find employees with attendance ≥ 90%.
# print(df.query("`attendance_%`>=90"))
# try:
#     df.to_excel("mixed3_get_dummies_final.xlsx",index=False)
#     df.to_csv("mixed3_get_dummies_final.csv",index=False)
# except Exception as e:
#     print(e)

#------------------------------------------------------------------------------------------------

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","HR","IT","Finance","HR","Finance"],
#     "City":["Ahmedabad","Surat","Mumbai","Ahmedabad","Mumbai","Surat"],
#     "Performance":["Good","Excellent","Average","Poor","Good","Excellent"],
#     "Salary":[50000,70000,90000,60000,80000,110000]
# })
# print(df)
# df["Department_Code"]=pd.factorize(df["Department"])[0]
# df["City_Code"]=pd.factorize(df["City"])[0]
# df["Performance_Code"]=pd.factorize(df["Performance"])[0]
# print(df)
# codes,categories=pd.factorize(df["Department"])
# print(codes)
# print(categories)
# codes,categories=pd.factorize(df["Department"],sort=True)
# print(codes)
# print(categories)
# df_1= pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu","Aastha"],
#     "Department":["IT","HR","IT","Finance","HR","Finance",None],
#     "City":["Ahmedabad","Surat","Mumbai","Ahmedabad","Mumbai","Surat","Ahmedabad"],
#     "Performance":["Good","Excellent","Average","Poor","Good","Excellent","Good"],
#     "Salary":[50000,70000,90000,60000,80000,110000,95000]
# })
# print(df_1)
# df_1["Department_Code"]=pd.factorize(df_1["Department"])[0]
# print(df_1)
# department_salary_mean=df.groupby("Department_Code")["Salary"].mean()
# print(department_salary_mean)
# print(department_salary_mean.idxmax())
# print(df)
# df.to_excel("factorize_analysis_final.xlsx",index=False)

# bonus1
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F"],
#     "Department":["IT","HR","IT","Finance","HR","IT"],
#     "City":["Ahmedabad","Surat","Mumbai","Ahmedabad","Mumbai","Surat"],
#     "Sales":[1000,1500,1200,2000,1800,2500],
#     "Salary":[50000,60000,70000,90000,80000,75000]
# })
# df["Department_Code"]=pd.factorize(df["Department"])[0]
# df["City_Code"]=pd.factorize(df["City"])[0]
# print(df)
# print(df.groupby("Department_Code")["Sales"].mean())
# print(df.groupby("Department_Code")["Sales"].sum().idxmax())
# city_salary_average=df.groupby("City_Code")["Salary"].mean()
# print(city_salary_average)
# print(city_salary_average.idxmax())


#bonus2
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F","G"],
#     "Department":["IT","HR","IT","Finance","HR","Finance","IT"],
#     "Performance":[
#         "Good","Excellent","Average",
#         "Poor","Good","Excellent","Good"
#     ],
#     "Sales":[1000,2000,1500,800,2200,2500,3000]
# })
# df["Department_Code"]=pd.factorize(df["Department"])[0]
# df["Performance_Code"]=pd.factorize(df["Performance"])[0]
# print(df)
# print(df.groupby("Department_Code")["Sales"].mean())
# print(df.groupby("Department_Code")["Sales"].sum().idxmax())
# print(df["Performance_Code"].value_counts().idxmax())
# print(df["Performance"].unique())

#MIXED 1
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","HR","IT","Finance","HR","Finance"],
#     "City":["Ahmedabad","Surat","Mumbai","Ahmedabad","Mumbai","Surat"],
#     "Sales":[100000,120000,90000,150000,130000,110000],
#     "Salary":[50000,70000,60000,90000,80000,110000],
#     "Rating":[4.2,4.5,3.5,4.8,4.1,4.9]
# })
# df["Department_Code"]=pd.factorize(df["Department"])[0]
# df["City_Code"]=pd.factorize(df["City"])[0]
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df["Department_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(df)
# print(df.nlargest(1,"Sales"))
# department_salary_average=df.groupby("Department_Code")["Salary"].mean()
# print(department_salary_average.idxmax())
# print(df.groupby("City_Code")["Sales"].sum().idxmax())
# df.to_excel("mixed1_factorize_final.xlsx",index=False)

#mixed2
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F","G","H"],
#     "Department":["IT","IT","HR","HR","Finance","Finance","Sales","Sales"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai",
#             "Surat","Ahmedabad","Mumbai","Surat"],
#     "Sales":[1000,2500,800,1800,3000,2200,1500,2800],
#     "Target":[1200,2000,1000,1600,2500,2000,1800,2500],
#     "Salary":[50000,70000,60000,80000,90000,110000,75000,95000]
# })

# print(df)
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Target_Status"]=np.where(df["Achievement_%"]>=100,"Achievement","Not Achievement_%")
# df["Department_Code"]=pd.factorize(df["Department"])[0]
# df["City_Code"]=pd.factorize(df["City"])[0]
# print(df)
# print(df.groupby("Department")["Sales"].mean())
# df["Department_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(df)
# print(df.nlargest(1,"Sales"))
# print(df.nlargest(1,"Achievement_%"))
# print(df.groupby("Department_Code")["Sales"].mean())
# print(df.groupby("City_Code")["Sales"].sum().idxmax())

#mixed3
# import pandas as pd
# import numpy as np

# try:
#     emp=pd.read_csv("mixed3_fact_emp.csv")
#     sales=pd.read_csv("mixed3_fact_sales.csv")
#     attendance=pd.read_csv("mixed3_fact_attendance.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(sales.info())
# print(attendance.info())
# df=pd.merge(emp,sales,on="EmployeeID",how="inner")
# df=pd.merge(df,attendance,on="EmployeeID",how="inner")
# df["Attendance_%"]=df["PresentDays"]/df["WorkingDays"]*100
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Target_Status"]=np.where(df["Achievement_%"]>=100,"Achievement","Not Achievement")
# df["Department_Code"]=pd.factorize(df["Department"])[0]
# df["City_Code"]=pd.factorize(df["City"])[0]
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[60000,80000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df["Salary_Rank_Department"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(df)
# print(df.nlargest(1,"Sales"))
# print(df.groupby("Department_Code")["Sales"].mean().idxmax())
# print(df.groupby("City_Code")["Sales"].sum().idxmax())
# df.to_excel("mixed3_fact_final.xlsx",index=False)

#--------------------------------------------------------------------------------------------------------

# Q1=B Q2=B Q3=C Q4=B Q5=A Q6=B Q7=B Q8=A Q9=A Q10=C

# import pandas as pd
# import  numpy as np

# df = pd.DataFrame({
#     "Employee":[
#         "Rahul","Neha","Amit","Priya",
#         "Manthan","Khushbu","Jay","Riya"
#     ],
#     "Department":[
#         "IT","IT","HR","HR",
#         "Finance","Finance","Sales","Sales"
#     ],
#     "Sales":[
#         1000,2000,500,700,
#         3000,4000,1500,2500
#     ],
#     "Salary":[
#         60000,80000,50000,55000,
#         90000,110000,70000,90000
#     ],
#     "Rating":[
#         4.2,4.5,3.1,3.8,
#         4.8,4.9,4.0,4.4
#     ]
# })

# print(df)
# print(df.groupby("Department").filter(lambda x:x["Sales"].mean()>1500))
# print(df.groupby("Department").filter(lambda x:x["Sales"].sum()>3000))
# print(df.groupby("Department").filter(lambda x:x["Salary"].mean()>70000))
# print(df.groupby("Department").filter(lambda x:(len(x)>=1)))
# print(df.groupby("Department").filter(lambda x:x["Sales"].max()>=3000))
# print(df.groupby("Department").filter(lambda x:x["Salary"].max()>55000))
# print(df.groupby("Department").filter(lambda x:x["Rating"].mean()>=4))
# print(df.groupby("Department").filter(lambda x:x["Sales"].mean()>1500 and x["Salary"].mean()>70000))
# sales_above_2500=df.query("Sales>2500")
# print(sales_above_2500.groupby("Department").filter(lambda x:len(x)>=1))
# print(df.groupby("Department").filter(lambda x:x["Sales"].sum()>x["Sales"].mean()*2))

# #bonus1
# print(df.groupby("Department").filter(lambda x:x["Sales"].mean()>1500 and x["Rating"].mean()>=4 and len(x)>=2))
# # Use one groupby().filter().
# #bonus2
# total_sales_4000_above=df.groupby("Department").filter(lambda x:x["Sales"].sum()>4000)
# print(total_sales_4000_above.groupby("Department")["Salary"].mean())
# total_sales_4000_above["Salary_Rank_Department"]=total_sales_4000_above.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(total_sales_4000_above)
# print(total_sales_4000_above.nlargest(1,"Salary"))

#mixed1
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F","G","H"],
#     "Department":[
#         "IT","IT","HR","HR",
#         "Finance","Finance","Sales","Sales"
#     ],
#     "City":[
#         "Ahmedabad","Surat","Ahmedabad","Surat",
#         "Mumbai","Mumbai","Ahmedabad","Surat"
#     ],
#     "Sales":[
#         1200,2200,800,900,
#         3000,3500,1800,2500
#     ],
#     "Salary":[
#         60000,80000,50000,55000,
#         90000,110000,70000,90000
#     ],
#     "Target":[
#         1000,2000,1000,1200,
#         2500,3000,2000,2200
#     ]
# })
# print(df)
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# print(df.groupby("Department")["Sales"].mean())
# department_average_sale_above1800=df.groupby("Department").filter(lambda x:x["Sales"].mean()>1800)
# print(department_average_sale_above1800)
# df["Salary_Rank_Department"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[50000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# print(df)
# print(df.nlargest(1,"Sales"))
# print(df.nlargest(1,"Achievement_%"))
# print(department_average_sale_above1800.groupby("Department")["Sales"].sum())

#mixed2

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":["A","B","C","D","E","F","G","H","I","J"],
#     "Department":[
#         "IT","IT","IT",
#         "HR","HR",
#         "Finance","Finance",
#         "Sales","Sales","Sales"
#     ],
#     "Sales":[
#         1000,1800,2500,
#         600,700,
#         3000,3500,
#         1500,2200,2800
#     ],
#     "Salary":[
#         60000,70000,85000,
#         50000,55000,
#         90000,100000,
#         70000,80000,90000
#     ],
#     "Rating":[
#         4.2,4.5,4.8,
#         3.2,3.5,
#         4.7,4.9,
#         4.0,4.2,4.5
#     ]
# })

# print(df)
# print(df.groupby("Department").filter(lambda x:x["Sales"].mean()>2000))
# print(df.groupby("Department").filter(lambda x:x["Salary"].mean()>75000))
# print(df.groupby("Department").filter(lambda x:x["Rating"].mean()>4))
# df_1=df.groupby("Department").filter(lambda x:x["Sales"].mean()>2000 and x["Rating"].mean()>4)
# print(df_1)
# df["Department_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# df["Department_Average_Sale"]=df.groupby("Department")["Sales"].transform("mean")
# print(df_1.nlargest(1,"Sales"))
# print(df_1.groupby("Department")["Sales"].sum())
# df["Sales_Categories"]=pd.cut(df["Sales"],bins=[0,1000,2000,3000,float("inf")],labels=["Poor","Average","Good","Excellent"])
# print(df)
# df.to_excel("mixed2_filter_final.xlsx",index=False)

#mixed3
# import pandas as pd
# import numpy as np

# try:
#     emp=pd.read_csv("mixed3_filter_emp.csv")
#     sale=pd.read_csv("mixed3_filter_sales.csv")
#     attendance=pd.read_csv("mixed3_filter_attendance.csv")
# except Exception as e:
#     print(e)

# print(emp.info())
# print(sale.info())
# print(attendance.info())
# df=pd.merge(emp,sale,on="EmployeeID",how="inner")
# df=pd.merge(df,attendance,on="EmployeeID",how="inner")
# df["Attendance_%"]=df["PresentDays"]/df["WorkingDays"]*100
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# print(df)
# print(df.groupby("Department")["Sales"].mean())
# print(df.groupby("Department").filter(lambda x:x["Sales"].mean()>100000))
# df["Department_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(df)
# print(df.nlargest(1,"Sales"))
# print(df.groupby("Department")["Sales"].mean().idxmax())
# print(df.groupby("Department")["Attendance_%"].mean().idxmax())
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[55000,80000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# print(df)
# df.to_excel("mixed3_filter_final.xlsx",index=False)

#----------------------------------------------------------------------------------

# Q1=B Q2=B Q3=C Q4=C Q5=B Q6=B Q7=B Q8=C Q9=B Q10=B 

# import pandas as pd

# employees = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105],
#     "EmployeeName":[
#         "Rahul","Neha","Amit","Priya","Manthan"
#     ],
#     "Department":[
#         "IT","HR","IT","Finance","Sales"
#     ]
# })

# sales = pd.DataFrame({
#     "EmpID":[
#         101,101,102,103,103,104,106
#     ],
#     "Month":[
#         "Jan","Feb","Jan","Jan","Feb","Jan","Jan"
#     ],
#     "Sales":[
#         50000,60000,70000,40000,55000,90000,30000
#     ]
# })

# salary_old = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105],
#     "Salary":[60000,70000,55000,80000,90000]
# })

# salary_new = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105],
#     "Salary":[65000,72000,60000,85000,95000]
# })

# targets = pd.DataFrame({
#     "EmpID":[101,102,103,104],
#     "Month":["Jan","Jan","Jan","Jan"],
#     "Target":[45000,75000,50000,80000]
# })

# # df=pd.merge(employees,sales,left_on="EmployeeID",right_on="EmpID")
# # print(df)

# df=pd.merge(employees,sales,indicator=True,left_on="EmployeeID",right_on="EmpID")
# print(df)

# print(df.query("_merge == 'left_only'"))

# orphaned_sales = sales[~sales['EmpID'].isin(employees['EmployeeID'])]
# print(orphaned_sales)

# df=pd.merge(salary_old,salary_new,on="EmployeeID",suffixes=("_old","_new"))
# df["Salaty_Change"]=df["Salary_new"]-df["Salary_old"]
# print(df)
# print(df.nlargest(1,"Salaty_Change"))
# print(sales)
# print(targets)
# df=pd.merge(sales,targets,left_on=["EmpID","Month"],right_on=["EmpID","Month"])
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# print(df)

# # df=pd.merge(employees,sales,validate="1:1",left_on="EmployeeID",right_on="EmpID")
# # print(df)
# # 1 to 1 show the duplicates errors
# df=pd.merge(employees,sales,validate="1:m",left_on="EmployeeID",right_on="EmpID")
# print(df)
# #1 to m is correct for this 
# print(employees.duplicated().sum())
# print(employees.duplicated().value_counts())

# print(employees["EmployeeID"].nunique())
# print(sales["EmpID"].count())

# valid_sales = sales[sales['EmpID'].isin(employees['EmployeeID'])]

# print(valid_sales)

# df=employees[~employees["EmployeeID"].isin(sales["EmpID"])]
# print(df)
# df=sales[~sales["EmpID"].isin(employees["EmployeeID"])]
# print(df)

#------------------------------------------------------------------------

#Q1=B Q2=B Q3=B Q4=A Q5=B Q6=A Q7=B Q8=B Q9=A Q10=A 

# import pandas as pd
# import numpy as np

# old = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105],
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Department":["IT","HR","Finance","HR","Sales"],
#     "Salary":[60000,70000,80000,75000,90000],
#     "Rating":[4.2,4.0,4.5,3.8,4.7]
# }).set_index("EmployeeID")

# new = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105],
#     "Name":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Department":["IT","Finance","Finance","HR","IT"],
#     "Salary":[65000,70000,85000,75000,95000],
#     "Rating":[4.5,4.0,4.5,4.2,4.7]
# }).set_index("EmployeeID")

# print(old.compare(new))
# print(old.compare(new,result_names=("Old","New")))
# print(old.compare(new,keep_shape=True))
# print(old.compare(new,keep_equal=True))
# print(old.compare(new,keep_shape=True,keep_equal=True))
# print(old.compare(new,align_axis=0))

# result= old.compare(new)
# print(result["Salary"])

# print(result["Department"])

# print(result["Rating"])

# result.to_excel("compare_final.xlsx")

#------------------------------------------------------------------------

# Q1=B Q2=C Q3=B Q4=A Q5=D Q6=B Q7=C Q8=A Q9=B Q10=B

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee": ["Rahul", "Neha", "Amit", "Priya"],
#     "Department": ["IT", "HR", "Finance", "Sales"],
#     "Salary": [60000, 70000, 80000, 90000]
# }, index=[101, 102, 103, 104])

# print(df)
# df=df.reindex(index=[103,101,104,102])
# print(df)
# # df=df.reindex([101,102,103,104,105])
# # print(df)
# # index value 105 become the nan

# df=df.reindex([101,102,103,104,105],fill_value=np.nan)
# df["Salary"]=df["Salary"].fillna(0)
# df[["Employee","Department"]]=df[["Employee","Department"]].fillna("Unknown")
# print(df)
# # i used the unknown because of the in data some data is str form so i used the unknown
# df=df.reindex(columns=["Salary","Employee","Department"])
# print(df)

# df=df.reindex(columns=["Employee","Department","Salary","Rating"])
# print(df)
# # Observe : rating columns become the nan

# sales = pd.Series(
#     [100000, 150000, 200000],
#     index=["Jan", "Mar", "Apr"]
# )
# print(sales)
# sales=sales.reindex(index=["Jan","Feb","Mar","Apr","May","Jun"],fill_value=0)
# print(sales)

# sales = pd.Series(
#     [100, 200, 300],
#     index=[1, 3, 5]
# )
# sales=sales.reindex(index=[1,2,3,4,5],method="ffill")
# print(sales)


# sales_1 = pd.Series(
#     [100, 200, 300],
#     index=[1, 3, 5]
# )
# sales_1=sales_1.reindex(index=[1,2,3,4,5],method="bfill")
# print(sales_1)
# print(sales.compare(sales_1,keep_shape=True))

# df = pd.DataFrame({
#     "Employee": ["Rahul", "Neha", "Amit"],
#     "Salary": [60000, 70000, 80000],
#     "Sales": [100000, 120000, 150000]
# }, index=[101, 102, 103])

# df=df.reindex(index=[103,101,104],
#               columns=["Sales","Employee","Salary","Rating"],fill_value=np.nan)
# df["Rating"]=df["Rating"].fillna(0)
# df["Salary"]=df["Salary"].fillna(0)
# df["Sales"]=df["Sales"].fillna(0)
# df["Employee"]=df["Employee"].fillna("Unknown")
# print(df)
# #i do this because of the some values are in str so all place not works the 0 

# monthly_sales = pd.Series(
#     [120000, 150000, 180000, 200000],
#     index=["Jan", "Mar", "Apr", "Jun"]
# )
# monthly_sales=monthly_sales.reindex(index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],fill_value=0)
# print(monthly_sales)
# print(monthly_sales.sum())

# print(monthly_sales.nlargest(1))
# monthly_sales=pd.DataFrame(monthly_sales)
# monthly_sales.to_excel("final_reindex.xlsx")

#bonus1
# import pandas as pd

# df = pd.DataFrame({
#     "Employee": ["A", "B", "C", "D"],
#     "Sales": [1000, 2000, 1500, 3000],
#     "Target": [1200, 1800, 1600, 2500]
# }, index=[101, 102, 103, 104])

# df=df.reindex(index=[104,102,105,101,103])
# df["Employee"]=df["Employee"].fillna("Unknown")
# df[["Sales","Target"]]=df[["Sales","Target"]].fillna(0)
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Achievement_%"]=df["Achievement_%"].fillna(0)
# print(df)
# print(df.nlargest(1,"Achievement_%"))

# # bonus2
# import pandas as pd

# sales = pd.Series(
#     [100, 120, 150, 180],
#     index=pd.to_datetime([
#         "2026-01-01",
#         "2026-01-03",
#         "2026-01-05",
#         "2026-01-07"
#     ])
# )

# sales_0=sales.reindex(index=["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05","2026-01-06","2026-01-07"],method="ffill")
# print(sales_0)

# sales_1=sales.reindex(index=["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05","2026-01-06","2026-01-07"],fill_value=0)
# print(sales_1)
# print(sales_0.compare(sales_1,keep_shape=True,keep_equal=True))
# # ffill is more appropriate for a carried-forward business value because of the business may be have date data so ffill is more usefull than bfill

#mixed1

# import pandas as pd

# df = pd.DataFrame({
#     "EmployeeID": [101, 102, 103, 104],
#     "Employee": ["Rahul", "Neha", "Amit", "Priya"],
#     "Department": ["IT", "HR", "Finance", "Sales"],
#     "Salary": [60000, 70000, 80000, 90000],
#     "Sales": [100000, 120000, 150000, 130000]
# })
# print(df)
# df=df.set_index("EmployeeID")
# print(df)
# df=df.reindex(index=[103,105,101,104,102])
# print(df)
# df[["Employee","Department"]]=df[["Employee","Department"]].fillna("Unknown")
# df[["Salary","Sales"]]=df[["Salary","Sales"]].fillna(0)
# print(df)
# df=df.reindex(columns=["Employee","Department","Sales","Salary"])
# print(df)
# print(df["Sales"].sum())
# print(df.nlargest(1,"Sales"))
# df.to_excel("mixed1_reindex_final.xlsx",index=False)

#mixed2
# import pandas as pd

# df = pd.DataFrame({
#     "Month": ["Jan", "Feb", "Apr", "Jun", "Jul"],
#     "Sales": [100000, 120000, 150000, 180000, 200000],
#     "Target": [110000, 115000, 140000, 170000, 190000]
# })
# print(df)
# df=df.set_index("Month")
# print(df)
# df=df.reindex(index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],fill_value=0)
# print(df)
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Achievement_%"]=df["Achievement_%"].fillna(0)
# print(df)
# print(df.nlargest(1,"Sales"))
# print(df.where(df["Sales"]>df["Target"]))

#mixed3

# import pandas as pd
# import numpy as np

# employees = pd.DataFrame({
#     "EmployeeID": [101, 102, 103, 104],
#     "Name": ["Rahul", "Neha", "Amit", "Priya"],
#     "Department": ["IT", "HR", "Finance", "Sales"],
#     "Salary": [60000, 70000, 85000, 90000]
# })

# sales = pd.DataFrame({
#     "EmployeeID": [101, 103, 104],
#     "Sales": [120000, 150000, 180000]
# })
# print(employees)
# print(sales)
# df=pd.merge(employees,sales,on="EmployeeID",how="outer")
# print(df)
# df=df.set_index("EmployeeID")
# df=df.reindex(index=[104,102,105,101,103],columns=["Name","Department","Salary","Sales"])
# print(df)
# df[["Name","Department"]]=df[["Name","Department"]].fillna("Unknown")
# df[["Salary","Sales"]]=df[["Salary","Sales"]].fillna(0)
# print(df)
# print(df["Salary"].corr(df["Sales"])) #0.7095577652469335
# print(df.nlargest(1,"Sales"))
# df.to_excel("mixed3_reindex_final.xlsx",index=False)

#Debugging Challenge
#  because of the you did not given parameter index 
# df = df.reindex(
#     index=[103, 101, 104],
#     fill_value=0
# )
# # full code:
# df = pd.DataFrame({
#     "Employee": ["A", "B", "C"],
#     "Salary": [50000, 60000, 70000]
# }, index=[101, 102, 103])

# df = df.reindex(
#     index=[103, 101, 104],
#    
# )
# df["Employee"]=df["Employee"].fillna("Unknown")
# df["Salary"]=df["Salary"].fillna(0)
# print(df)

# trace 
# 1. What values will B and D receive:-100 and 200

# Thinking Question
# i used the ffill because of the stock price can not be the 0 so i used the method="ffill"

#---------------------------------------------------------------------------------

# Q1=B Q2=C Q3=D Q4=B Q5=C Q6=B Q7=A Q8=A Q9=C Q10=B

# import pandas as pd
# import numpy as np

# sales = pd.Series(
#     [100000, 150000, 200000, 250000],
#     index=["Jan", "Feb", "Apr", "May"]
# )

# target = pd.Series(
#     [120000, 140000, 180000, 220000],
#     index=["Jan", "Mar", "Apr", "May"]
# )

# print(sales)
# print(target)
# print(sales.index)
# print(target.index)

# sales_a,target_a=sales.align(target)
# print(sales_a)
# print(target_a)

# sales_i,target_i=sales.align(target,join="inner")
# print(sales_i)
# print(target_i)

# sales_l,target_l=sales.align(target,join="left")
# print(sales_l)
# print(target_l)
# # all sales months are remains

# sales_r,target_r=sales.align(target,join="right")
# print(sales_r)
# print(target_r)
# # all target months are remains

# sales_o,target_o=sales.align(target,fill_value=0)
# print(sales_o)
# print(target_o)

# gap=sales_o-target_o
# print(gap)

# Achievement=sales_o/target_o*100
# print(Achievement)

# status=np.where(Achievement>=100,"Achieved","Not Achieved")
# print(status)

# df=pd.DataFrame({
#     "Sales":sales_o,
#     "Target":target_o,
#     "Gap":gap,
#     "Achievement_%":Achievement,
#     "Status":status
# })

# print(df)

# df=df.sort_values("Achievement_%",ascending=False)
# print(df)
# print(df.head(1))
# try:
#     df.to_excel("align_pratical_final.xlsx",index=False)
# except Exception as e:
#     print(e)



# ⭐ Bonus 1 
# import pandas as pd
# import numpy as np

# sales = pd.Series(
#     [100, 200, 300, 400],
#     index=["A", "B", "D", "E"]
# )

# target = pd.Series(
#     [150, 180, 350, 450],
#     index=["A", "C", "D", "E"]
# )

# sales_i,target_i=sales.align(target,join="inner")
# print(sales_i)
# print(target_i)

# gap=sales_i-target_i
# print(gap)

# achievement=sales_i/target_i*100
# print(achievement)

# status=np.where(achievement>=100,"Achieved","Not Achieved")
# print(status)
# print(achievement.max())
# print(achievement.mean())
# i can not export the series result

# ⭐ Bonus 2 

# import pandas as pd
# import numpy as np

# sales = pd.Series(
#     [100, 150, 180, 220],
#     index=pd.to_datetime([
#         "2026-01-01",
#         "2026-01-03",
#         "2026-01-05",
#         "2026-01-07"
#     ])
# )

# target = pd.Series(
#     [120, 160, 200, 210],
#     index=pd.to_datetime([
#         "2026-01-01",
#         "2026-01-02",
#         "2026-01-05",
#         "2026-01-07"
#     ])
# )

# sales_i,target_i=sales.align(target) #i used the outer because i want to use outer insted of inner
# print(sales_i)
# print(target_i)

# df=pd.DataFrame({
#     "Sales":sales_i,
#     "Target":target_i
# })
# print(df)
# df["Sales"]=df["Sales"].fillna(df["Sales"].mean())
# df["Target"]=df["Target"].fillna(df["Sales"].mean())

# df["Gap"]=df["Sales"]-df["Target"]
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Status"]=np.where(df["Achievement_%"]>=100,"Achieved","Not Achieved")
# print(df)
# df=df.reindex(index=["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05","2026-01-06","2026-01-07"],method="ffill")
# df["3day_rolling_average"]=df["Sales"].rolling(3,min_periods=1).mean()
# print(df)
# print(df["Sales"].sum())

# 🔥 Mixed 1 

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee":[" Rahul ","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","I.T.","HR","Human Resources","Finance","FINANCE"],
#     "Sales":["100000","120000","90000","150000","180000","200000"],
#     "Target":[90000,130000,100000,140000,160000,190000],
#     "Salary":[60000,70000,55000,80000,90000,110000],
#     "Rating":[4.2,4.5,3.2,3.8,4.8,4.9]
# })


# previous_sales = pd.Series(
#     [95000,115000,85000,145000,170000,195000],
#     index=["Rahul","Neha","Amit","Priya","Manthan","Khushbu"]
# )

# current_sales = pd.Series(
#     [100000,120000,90000,150000,180000,200000],
#     index=["Rahul","Neha","Amit","Priya","Manthan","Khushbu"]
# )


# df.columns=df.columns.str.strip().str.lower()
# df=df.rename(columns={
#     "employee":"employee_name"
# })
# print(df.columns)
# print(df.dtypes)
# df["employee_name"]=df["employee_name"].str.strip().str.title()
# print(df)
# df["department"]=df["department"].str.strip().str.title().replace({
#     "It":"IT",
#     "I.T.":"IT",
#     "Hr":"HR",
#     "Human Resources":"HR"
# })
# df["sales"]=pd.to_numeric(df["sales"],errors="coerce")
# print(df.dtypes)

# previous_sales_o,current_sales_o=previous_sales.align(current_sales)
# print(previous_sales)

# sales_growth=previous_sales/current_sales*100
# print(sales_growth)

# df["achievement_%"]=df["sales"]/df["target"]*100
# df["status"]=np.where(df["achievement_%"]>=100,"Achieved","Not Achieved")
# df["department_average_sale"]=df.groupby("department")["sales"].transform("mean")
# df["salary_rank"]=df.groupby("department")["salary"].rank(ascending=False,method="dense")
# df["salary_category"]=pd.cut(df["salary"],bins=[55000,75000,100000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# print(df)
# print(df.nlargest(1,"sales"))
# print(df.groupby("department")["sales"].sum().idxmax())
# print(df.pivot_table(index="department",columns="status",values="achievement_%",aggfunc="mean",fill_value=0))


# 🔥 Mixed 2 

# import pandas as pd
# import numpy as np

# actual = pd.Series(
#     [120000,150000,180000,220000,250000],
#     index=["Jan","Feb","Apr","May","Jun"]
# )

# target = pd.Series(
#     [110000,160000,170000,210000,270000],
#     index=["Jan","Mar","Apr","May","Jun"]
# )


# employees = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105],
#     "Employee":["Rahul","Neha","Amit","Priya","Manthan"],
#     "Department":["IT","HR","IT","Finance","Sales"],
#     "Salary":[60000,70000,55000,90000,110000],
#     "Rating":[4.2,4.5,3.2,4.8,4.9]
# })

# actual_i,target_i=actual.align(target,join="inner")
# print(actual_i)
# print(target_i)
# gap=actual_i-target_i
# print(gap)
# achievement=actual_i/target_i*100
# print(achievement)
# status=np.where(achievement>=100,"Achieve","Not Achieve")
# print(status)
# print(achievement.nlargest(1))


# employees["Salary_Band"]=pd.cut(employees["Salary"],bins=[55000,69000,90000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# employees["Salary_Rank_Department"]=employees.groupby("Department")["Salary"].rank(ascending=False,method="dense")
# print(employees)
# print(employees.nlargest(1,"Salary"))
# print(employees.groupby("Department")["Salary"].mean().idxmax())
# print(employees.query("Rating>=4"))

# df=pd.DataFrame({
#     "Actual":actual_i,
#     "Target":target_i,
#     "Gap":gap,
#     "Achievement_%":achievement,
#     "Status":status
# })
# print(df)
# df.to_excel("mixed2_align_final.xlsx",index=False)

# 🔥 Mixed 3 

# import pandas as pd
# import numpy as np

# employees = pd.DataFrame({
#     "EmployeeID":[101,102,103,104,105,106],
#     "Name":["Rahul","Neha","Amit","Priya","Manthan","Khushbu"],
#     "Department":["IT","HR","IT","Finance","Finance","Sales"],
#     "City":["Ahmedabad","Surat","Ahmedabad","Mumbai","Surat","Ahmedabad"],
#     "Salary":[60000,70000,55000,90000,110000,80000],
#     "Rating":[4.2,4.5,3.2,4.8,4.9,4.1]
# })


# sales = pd.Series(
#     [100000,130000,90000,180000,200000,120000],
#     index=[101,102,103,104,105,106]
# )

# targets = pd.Series(
#     [90000,140000,100000,160000,180000,130000],
#     index=[101,102,103,104,105,106]
# )

# attendance = pd.Series(
#     [95,91,82,98,96,89],
#     index=[101,102,103,104,105,106]
# )

# sales_o,target_o=sales.align(targets)
# print(sales_o,target_o)


# employees = employees.set_index("EmployeeID")

# employees_1 = pd.DataFrame({
#     "Sales": sales_o,
#     "Target": target_o,
#     "Attendance_%":attendance
# })
# df = pd.merge(employees, employees_1, left_index=True, right_index=True, how="inner")
# df["Achievement_%"]=df["Sales"]/df["Target"]*100
# df["Status"]=np.where(df["Achievement_%"]>=100,"Achieved","Not Achieved")
# df["Salary_Band"]=pd.cut(df["Salary"],bins=[55000,75000,85000,float("inf")],labels=["Low","Medium","High"],include_lowest=True)
# df["Department_Salary_Rank"]=df.groupby("Department")["Salary"].rank(ascending=False,method="dense")

# df["Department_Average_Sales"]=df.groupby("Department")["Sales"].transform("mean")
# df["Department_Average_Salary"]=df.groupby("Department")["Salary"].transform("mean")
# print(df)

# print(df.groupby("Department").filter(lambda x:x["Sales"].mean()>12000 and x["Rating"].mean()>=4))
# print(df.nlargest(1,"Sales"))
# print(df.nlargest(1,"Achievement_%"))
# print(df.nlargest(1,"Salary"))
# print(df.nlargest(1,"Attendance_%"))
# print(df.groupby("Department")["Sales"].sum().idxmax())
# print(df.groupby("Department")["Salary"].mean().idxmax())
# print(df.query("Department_Salary_Rank==1"))

# print(df.pivot_table(index="Department",columns="City",values="Sales",aggfunc="sum",fill_value=0))

# df=df.sort_values("Achievement_%",ascending=False)

# df.to_excel("mixed3_final_align_internship_project.xlsx",index=False)