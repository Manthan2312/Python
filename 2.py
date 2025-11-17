# a=1
# print(a)
# b="Manthan"
# print(b)
# c="K"
# print(c)
# d=12.5
# print(type(d))
# e=-23
# print(e)
# f=True
# print(type(f))
# g=None
# print(type(g))
# h=complex(1,21)
# print(h)


# list=["Manthan","Khushbu",[12,1,11.2,-23],"Hello",False]
# print(list)

# tuple=("Manthan","Khushbu",(12,1,11.22,-22),"go",True)#tuples are unmutable;
# print(tuple)

# dis={"Manthan":"Patel","Khushbu":"Shah","Tiya":"Shah","Tirth":"Dabhi","Age":20,"Nationalityisindian":False}
# print(dis);


# print(type(range(3)))


# x=[1,3,2]
# y=x
# y.append(4)
# print(x)


# Input= [1, 2, 3, 4, 5,6]

# total=0

# for i in Input:
#     if i%2==0:
#         total+=i

# print(total)




# def is_palindrome(word):
#     word=word.lower()
#     if word==word[::-1]:
#         return True
#     else:
#         return False
    
# print(is_palindrome("Level"))
# print(is_palindrome("Python"))




# Input: "python is fun and python is easy"
# Output: {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'easy': 1}



sente="python is fun and python is easy"
sente=sente.split()
word_count = {}

for word in sente:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


from collections import Counter

sente = "python is fun and python is easy"
word_count = Counter(sente.split())

# print(word_count)
print(dict(word_count))

   


        




    



