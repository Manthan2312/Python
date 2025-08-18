# name="Manthan"
# age=20

# print(name)
# print(age)


# print(f"My name is {name} and I am {age} years old")


# a=int(4)
# b=int(4)


# print(f"The sum of {a} and {b} : {a+b}" )



#practice

# number=int(input("Enter the number\n"))
# if number%2==0:
#     print("Even")
# else:
#     print("Odd")

# facto=1
# i=1
# while(i<=number):
#     facto=facto*i
#     i=i+1


# print(facto)

# sent="eye"
# sent=sent.lower()

# sent1 ="".join(reversed(sent))
# if(sent==sent1):
#     print("palindrome")
# else:
#     print("not palindrome")


# list1=[1,2,3,4,5]
# sum=0
# i=0
# while(i<=len(list1)):
#     sum=sum+i
#     i=i+1


# print(sum)
# print(sum(list1))


# string="Manthankhushbu"
# vowels="aeiouAEIOU"
# count=0

# for i in string:
#     if i in vowels:
#         count+=1



# print(count)



# def Fibonacci(number):
#         i=0
#         a=0
#         b=1
#         ans=0
#         while(i<number): 
#             print(a)
           
#             ans=a+b
#             a=b
#             b=ans
#             i=i+1


# number=int(input("Enter the number\n"))
# Fibonacci(number)



# list2=[1,2,3]
# maxn=list2[0]
# i=0
# while(i<len(list2)):
#     if list2[i]>maxn:
#         maxn=list2[i]
#     i=i+1

# print(maxn)


# print(max(list2))


# list3=[1,2,4,1,4]
# un=[]
# i=0
# while(i<len(list3)):
#     if list3[i] not in un:
#         un.append(list3[i])
#     i=i+1


# print(un)



# list4=[1,2,3,4,5]

# if list4==sorted(list4):
#     print("sorted")
# else:
#     print("unsorted")



# def sum_arr(list1):
#     '''This function do the thing sum of the list with help of the for loop'''
#     total=0
#     for i in list1:
#         total+=i


#     print(total)




# sum_arr([891,1,1,1,1])
# print(sum_arr.__doc__)


def febbo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return febbo(n - 1) + febbo(n - 2)


     
     
for i in range(10):
    print(f"febbo({i}) = {febbo(i)}")


