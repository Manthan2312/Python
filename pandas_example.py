import pandas as pd

# a= pd.Series([11,12,13,14,15,16] ,index=['a','b','c','d','e','f'])
# print(a)



# Dictionary of lists
# data = {
#     'Name': ['Manthan', 'Raj', 'Priya'],
#     'Age': [25, 30, 22],
#     'City': ['Vadnagar', 'Ahmedabad', 'Surat']
# }

# df = pd.DataFrame(data)
# print(df)








# Load the dataset
df = pd.read_csv("products_practice.csv")

# print full file details
print(df)

#print only first 5 data
# print(df.head())

# print(df["Quantity"].mean())


# list_example=[]
# for i in df["Quantity"]:
#     list_example.append(i)


# print(list_example)
# avg = sum(list_example) / len(list_example)
# print(avg)

# print(df["Price"].min())
# print(df["Price"].max())


# print(df["Product"])
# print(df["Store"])



# print(df["Price"].sum())

# print(df.describe())
# for i in df:
#     print(df)


# Total quantity sold per store
# print(df.groupby("Store")["Quantity"].sum())

# print(df.groupby("Category")["Price"].sum())

# print(df.sort_values("Quantity",ascending=False))

# print(df["Price"].idxmin())
# print(df["Price"].idxmax())


print(df.loc[df["Price"].idxmax()])

print("----------------------------------------------")
print(df.loc[df["Quantity"].idxmax()])
print(df.groupby("Store"))
