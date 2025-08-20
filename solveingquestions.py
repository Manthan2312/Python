# # Find the second largest number in a list (without using max() twice).
# number_list=[11,411,432,717,84]
# number_list.sort()
# print(number_list[len(number_list)-2])

# maxn=number_list[0]
# # print(number_list[0])
# for i in number_list:
#     if i>maxn:
#         maxn=i
# print(maxn)
# number_list.remove(maxn)
# maxn=number_list[0]
# for j in number_list:
#     if j>maxn:
#         maxn=j
# print(number_list)
# print(maxn)

# maxn=number_list[0]
# new_list=[]

# for i in number_list:
#     if i>maxn:
#         maxn=i

# for j in number_list:
#     if j==maxn:
#         continue
#     new_list.append(j)


# maxn=new_list[0]
# for k in new_list:
#     if k>maxn:
#         maxn=k

# print(maxn)






# 👉 Find all pairs in a list whose sum is equal to a given target.

numbers = [2, 4, 4, 1, 5, 1]
target = 6

# pairs = set()

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             pairs.add(tuple(sorted((numbers[i], numbers[j]))))

# print(pairs)

i=0

pairs = set()
while(i<len(numbers)-1):
    if numbers[i]+numbers[i+1]==target:
        # print((numbers[i],numbers[i+1]))
        pairs.add(tuple(sorted((numbers[i], numbers[i+1]))))
    i+=1

print(pairs)
        