import numpy as np

# print(np.__version__)
# arr=np.array([10,20,30,40,50])
# print(arr)

# # print(type(arr))

# print(arr*2)  #This is called Vectorization.

# arr1=np.array([10,2,3,4,5])
# print(arr1-1)
# print(arr1+1)
# print(arr1*2)
# print(arr1/2)

# arr2=np.array([20,40,60,80])
# print(arr2.shape)
# print(arr2.size)
# print(arr2.dtype)

#1

# arr=np.array([5, 10, 15, 20])
# print(arr)
# print(type(arr))
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)

#2
# arr=np.array([2,4,6,8])

# print(arr+2)
# print(arr*3)
# print(arr-1)
# print(arr/2)

#3
# list_number=[1,2,3,4,5]
# print(type(list_number))

# arr=np.array([1,2,3,4,5])
# print(type(arr))

#bonus
# sales = np.array([1200,1500,1800,900])

# print(sales*1.10)
# print(sales+100)
# print(sales-50)


#1

# arr=np.array([5,10,15,20,25])
# print(arr[0])
# print(arr[4])
# print(arr[2])

#2
# arr=np.array([5,10,15,20,25])
# arr[2]=150
# print(arr)

#3
# arr=np.array([[1,2,3],
#              [4,5,6],
#              [7,8,9]])

# print(arr[1][1])
# print(arr[2][2])
# print(arr[0][0])

#4
# arr=np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# arr[1][1]=500
# print(arr)

#bonus
# marks = np.array([
#  [90,85,88],
#  [75,80,79],
#  [60,70,65]
# ])
# print(marks[0][1])
# print(marks[1][2])
# print(marks[2][0])


#1
# arr=np.array([5,10,15,20,25,30])
# print(arr[:3])
# print(arr[3:])
# print(arr)
# print(arr[::-1])

#2
# arr=np.array([
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
#     ])

# print(arr[0:1])
# print(arr[2:])

# print(arr[:,0])
# print(arr[:,2])

#3
# arr=np.array([
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
#     ])
# print(arr[1:,1:])

#bonus

# sales = np.array([
#  [1200,1500,1800],
#  [900,1100,1300],
#  [2000,2200,2500]
# ])
# print(sales[:2])
# print(sales[1:])
# print(sales[:,0:2])
# print(sales[0:,2:])
# print(sales[1:,:2])

#1
# arr=np.array([10,20,30,40,50])
# print(arr[arr>25])
# print(arr[arr<=30])

#2
# marks = np.array([35,48,62,77,29,91])
# print(marks[marks>=50])
# print(marks[marks<50])

#3
# salary=np.array([25000,45000,60000,80000,30000])
# print(salary[salary>40000])
# print(salary[(salary>=30000) & (salary<=70000)])

#4
# number=np.array([1,2,3,4,5,6,7,8,9,10])
# print(number[number%2==0])
# print(number[number%2!=0])

#Bonus
# sales = np.array([
#     1200,
#     800,
#     2500,
#     1700,
#     900,
#     3000
# ])
# print(sales[sales>1500])
# print(sales[(sales>=1000) & (sales<=2500)])
# print(sales[sales!=900])

#1
# sales=np.array([1200,1500,1800,900])
# print(np.sum(sales))
# print(np.mean(sales))
# print(np.max(sales))
# print(np.min(sales))

#2
# marks=np.array([75,80,90,65,85])
# print(np.mean(marks))
# print(np.median(marks))
# print(np.std(marks))

#3
# arr=np.array([[10,20],
#               [30,40]
#               ])
# print(np.sum(arr))
# print(np.sum(arr,axis=0))
# print(np.sum(arr,axis=1))

#bonus
# salary=np.array([35000,50000,45000,70000,60000])

# print(np.sum(salary))
# print(np.mean(salary))
# print(np.max(salary))
# print(np.min(salary))
# print(np.std(salary))
# print(np.median(salary))

#1
# arr=np.array([1,2,3,4,5,6])
# print(arr.reshape(3,2))
# print(arr.reshape(2,3))

#2
# arr=np.array([1,2,3,4,5,6])
# print(arr.reshape(-1,2))
# print(arr.reshape(2,-1))

#3
# arr=np.array([[1,2,3],
#               [4,5,6]
#               ])
# print(arr.flatten())
# print(arr.ravel())

#bonus
# sales = np.array([
#  [1200,1500],
#  [1800,900],
#  [2200,1700]
# ])
# print(sales.shape)

# print(sales.flatten())
# print(sales.reshape(2,3))

# print(sales.reshape(-1,3))

#1
# print(np.random.randint(1,50))
# print(np.random.randint(10,100,size=5))

#2
# print(np.random.rand(5))
# print(np.random.rand(2,3))

#3
# np.random.seed(100)
# print(np.random.randint(1,20,size=5))
#answer of Observe : both or more time values are same , i have a questions why we used this seed(100) or seed(42)
#what that's meaning 

#4
# sales = np.random.randint(1000,5000,size=10)
# print(sales)
# print("Totol sale",np.sum(sales))
# print("Average sale",np.mean(sales))
# print("Highest sale",np.max(sales))
# print("Lowest sale",np.min(sales))

#bonus
# marks = np.random.randint(35,100,size=20)
# print(marks)
# print("Average Marks",np.mean(marks))
# print("Highest Marks",np.max(marks))
# print("Lowest Marks",np.min(marks))
# print(marks[marks>=75])

#1
# a=np.array([10,20,30])
# b=np.array([40,50,60])

# print(np.concatenate((a,b)))
# print(np.hstack((a,b)))

#2
# a=np.array([
#     [1,2],
#     [3,4]
# ])

# b=np.array([
#     [5,6],
#     [7,8]
# ])

# print(np.concatenate((a,b),axis=0))
# print(np.concatenate((a,b),axis=1))

#Bonus
# q1 = np.array([1200, 1500, 1800])
# q2 = np.array([2000, 2200, 2500])

# sales=np.hstack((q1,q2))

# print(np.sum(sales))
# print(np.mean(sales))
# print(sales[sales>1800])

#1
# arr=np.array([10,20,30,40,50,60])
# sarr=np.split(arr,3)
# print(sarr)

# for i in sarr:
#     print(i)

#2
# arr=np.array([1,2,3,4,5])
# print(np.array_split(arr,2))
# print(np.array_split(arr,3))
# array can we divided into the 2 parts first have 3 elements and second have 2 elements 
# array can we divided into the 3 parts first have 2 elements ,second also have 2 elements and third have 1 element

#3
# arr=np.array([
#     [10,20],
#     [30,40],
#     [50,60],
#     [70,80]
# ])

# print(np.split(arr,2))
# print(np.split(arr,2,axis=1))

#Bonus
# sales = np.array([
# 1200,1300,1400,
# 1500,1600,1700,
# 1800,1900,2000,
# 2100,2200,2300
# ])

# qu_4=np.split(sales,4)

# for i in qu_4:
#     print(i)
#     print(np.sum(i))


#1
# arr = np.array([50,10,40,20,30])
# print("ORIGINAL ARRAY:",arr)
# print("SORTED ARRAY:",np.sort(arr))

#2
# arr = np.array([50,10,40,20,30])
# print("DESCENDING SORTED ARRAY:",np.sort(arr)[::-1])

#3
# names = np.array([
#     "Rahul",
#     "Manthan",
#     "Amit",
#     "Neha",
#     "Priya"
# ])
# print(np.sort(names))

#4
# arr = np.array([
#     [30,10],
#     [40,20]
# ])

# print(np.sort(arr))

#5
# arr = np.array([
#     [30,10],
#     [40,20]
# ])

# print(np.sort(arr,axis=0))
# #output is same because of the already shorted by columns

#6
# sales=np.random.randint(1000,5000,15)
# print("Original:",sales)
# print("Sorted ascending:",np.sort(sales))
# print("Sorted descending:",np.sort(sales)[::-1])

#7
# marks=np.random.randint(35,100,20)
# print(marks)
# sort_marks=np.sort(marks)
# print("sorted marks:",sort_marks)
# print("Higheht marks:",sort_marks[19])
# print("Lowest marks:",sort_marks[0])

# # or 
# print("sorted marks:",np.sort(marks))
# print("Higheht marks:",np.max(np.sort(marks)))
# print("Lowest marks:",np.min(np.sort(marks)))

#8
# salary = np.array([
# 45000,
# 32000,
# 60000,
# 28000,
# 52000
# ])

# print("Salaries sorted ascending:",np.sort(salary))
# print("Salaries sorted descending:",np.sort(salary)[::-1])

#Bonus 1
# profits = np.random.randint(10000,50000,12)
# print("original profits:",profits)
# sorted_profits=np.sort(profits)
# print("sorted profits:",sorted_profits)
# dsorted_profits=np.sort(profits)[::-1]
# print("Top 3 Profits",dsorted_profits[0],dsorted_profits[1],dsorted_profits[2])
# print("Lowest 3 profits",sorted_profits[0],sorted_profits[1],sorted_profits[2])

#Bonus2
# ages=np.random.randint(18,60,30)
# print(ages)

# print("Sorted Ages:",np.sort(ages))
# print("Ages greater than 40",ages[ages>40])
# print("Average age:",np.mean(ages))
# print("Median age:",np.median(ages))

#1

# arr = np.array([10,20,30,20,40])
# print(np.where(arr==20))
# print(np.where(arr>25))
#if values wants
# print(arr[arr>25])

#2
# marks = np.array([45,67,82,91,58])
# print(np.where(marks>=60))
# print(marks[marks>=60])

#3
# sales = np.array([1200,1800,1500,2500])
# print(np.max(sales))
# print(np.argmax(sales))
# print(np.min(sales))
# print(np.argmin(sales))

#4
# arr = np.array([
#     [10,20],
#     [30,20]
# ])

# print(np.where(arr==20))

#5
# ages=np.random.randint(18,60,20)
# print(ages)
# print(np.where(ages>40))
# print(ages[ages>40])

#6
# np.random.seed(42)
# salary=np.random.randint(18000,60000,15)
# print(salary)
# print(np.max(salary))
# print(np.argmax(salary))

#7
# np.random.seed(42)
# marks=np.random.randint(35,100,15)
# print(marks)
# print(np.min(marks))
# print(np.argmin(marks))

#8
# np.random.seed(42)
# numbers=np.random.randint(1,100,25)
# print(numbers)
# print(numbers[numbers>50])
# print(np.where(numbers>50))

#bonus
# np.random.seed(42)
# sales=np.random.randint(1000,10000,50)
# print(sales)
# print(np.max(sales))
# print(np.min(sales))
# print(np.argmax(sales)," ",np.argmin(sales))
# avgs=np.mean(sales)
# print(sales[sales>avgs])
# print(np.where(sales>avgs))

#bonus
# employee_ids = np.array([101,102,103,104,105])
# salary = np.array([45000,52000,41000,61000,48000])

# salaryup=np.where(salary>50000)
# print(salaryup)
# print(employee_ids[salaryup])


# indices = np.where(salary > 50000)[0]

# print(indices)

# print(employee_ids[indices])

#1

# arr=np.array([10,20,30,40,50])
# print(arr[[0,2,4]])

#2

# arr=np.array([10,20,30,40,50])
# print(arr[[1,1,4]])

#3

# arr=np.array([10,20,30,40,50])
# arr[[1,3]]=100
# print(arr)

#4

# names = np.array([
# "Rahul",
# "Manthan",
# "Amit",
# "Neha",
# "Priya"
# ])

# print(names[[0,3]])

#5

# salary = np.array([
# 45000,
# 52000,
# 41000,
# 61000,
# 48000
# ])
# print(salary[[1,4]])

#6
# np.random.seed(42)
# marks = np.random.randint(35,100,15)
# print(marks)
# print(marks[[2,5,10]])

#7

# arr = np.array([
# [10,20],
# [30,40],
# [50,60]
# ])

# print(arr[[0,2]])

#8

# arr = np.array([
# [10,20,30],
# [40,50,60],
# [70,80,90]
# ])

# print(arr[[0,2],[0,2]])

#9
# np.random.seed(1)
# salary=np.random.randint(10000,80000,20)
# print(salary)
# print(salary[[0,4,8,15]])

#10
# np.random.seed(1)
# ages=np.random.randint(10,80,30)
# print(ages)
# print(ages[[2,7,12,18,25]])

#bonus
# np.random.seed(42)
# sales = np.random.randint(1000,10000,20)
# print(np.sort(sales))
# top5value=np.argsort(sales)[-5:][::-1]
# print(sales[top5value])

#bonus
# employee_ids = np.array([101,102,103,104,105])
# names = np.array(["Rahul","Manthan","Amit","Neha","Priya"])
# salary = np.array([45000,52000,41000,61000,48000])
# selected = [1,3]
# print(employee_ids[selected],
#       names[selected],
#       salary[selected])


# arr = np.array([80,50,90,40])
# #0123 first do 
# #  3 1 0 2  second 
# #40,50,80,90 last 
# idx = np.argsort(arr)

# print(idx)

# print(arr[idx])

#1
# arr = np.array([1,2,2,3,4,4,5])
# print(np.unique(arr))

#2
# marks = np.array([-10,25,60,120,80])
# print(np.clip(marks,0,100))

#3
# print(np.linspace(0,30,6))

#4
# print(np.arange(0,20,5))

#5
# print(np.zeros(5))
# print(np.ones(5))
# print(np.full(5,99))

#6
# print(np.zeros((3,4)))
# print(np.ones((2,5)))

#7
# np.random.seed(42)
# ages=np.random.randint(10,100,20)
# print(ages)
# unique_ages=np.unique(ages)
# print(unique_ages)
# print(np.sort(unique_ages))

#8
# np.random.seed(1)
# marks=np.random.randint(35,100,30)
# print(marks)
# print(np.clip(marks,40,90))

#9
# print(np.linspace(100,500,10))

#10
# print(np.full((3,3),7))

#bonus
 # np.random.seed(1)
# sales = np.random.randint(1000,10000,50)
# print(sales)
# unique_Sale=np.unique(sales)
# print(unique_Sale)
# print(len(unique_Sale))
# print(np.max(unique_Sale))
# print(np.min(unique_Sale))

#bonus
# np.random.seed(1)
# temperatures = np.random.randint(-20,150,30)
# print(temperatures)
# print(np.mean(temperatures))
# ct=np.clip(temperatures,0,100)
# print(ct)
# print(np.mean(ct))

# arr = np.arange(0,10,5)

# print((arr))

# arr=np.linspace(0,10,5)
# print(arr)

# print(np.arange(0,11,5))




