# print(dir())

# def add(a,b):
#     return a+b


# print(dir())

# name_student=["MANTHAN","KHUSHBU","TIYA","TIRTH"]
# print(dir(name_student))


class emp:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno


    def infos(self):
        print(self.name)
        print(self.rollno)



e1=emp("manthan",2252)
print(e1.infos())

print(e1.__dict__)
# print(emp.__dict__)

new_dic={}
new_dic=e1.__dict__
print(new_dic)
print(list(new_dic))


print(help(e1))