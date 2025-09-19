# single inheritance

# class employees:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id

#     def infodetails(self):
#         print(self.name)
#         print(self.age)
#         print(self.id)

# class employeesstatus(employees):

#     def __init__(self, name, age, id,department,salary):
#         super().__init__(name, age, id)
#         self.department=department
#         self.salary=salary

#     def infodetails(self):
#         super().infodetails()
#         print(self.department)
#         print(self.salary)

# e1=employeesstatus("Manthan",20,"EMPNO101","IT",800000)
# e1.infodetails()

# multiple inheritance

# class employees:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id

#     def infodetails(self):
#         print(self.name)
#         print(self.age)
#         print(self.id)

# class hobbyofemployees:
#     def __init__(self, hobby):
#         self.hobby = hobby

#     def infodetails(self):
#         print(self.hobby)



# class fulldetailsemp(employees, hobbyofemployees):

#     def __init__(self, name, age, id, hobby):
#         employees.__init__(self, name, age, id)
#         hobbyofemployees.__init__(self, hobby)

#     def infodetails(self):
#         employees.infodetails(self)
#         hobbyofemployees.infodetails(self)




# e1 = fulldetailsemp("Manthan", 20, "EMPNO101", "Playing Cricket")
# e1.infodetails()


# multilevel inheritance
# class employees:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id

#     def infodetails(self):
#         print(self.name)
#         print(self.age)
#         print(self.id)

# class employeesstatus(employees):

#     def __init__(self, name, age, id,department,salary):
#         super().__init__(name, age, id)
#         self.department=department
#         self.salary=salary

#     def infodetails(self):
#         super().infodetails()
#         print(self.department)
#         print(self.salary)

# class fulldetailsemp(employeesstatus):

#     def __init__(self, name, age, id, department, salary,hobby):
#         super().__init__(name, age, id, department, salary)
#         self.hobby=hobby
    
#     def infodetails(self):
#         super().infodetails()
#         print(self.hobby)



# e1=fulldetailsemp("Manthan",20,"EMPNO001","IT","600000","POLITICS")
# e1.infodetails()



# # Create a dictionary
# employee = {
#     "name": "Manthan",
#     "age": 20,
#     "id": "EMPNO001",
#     "department": "IT",
#     "salary": 600000,
#     "hobby": "Politics"
# }

# # Access values
# print(employee["name"])       # Manthan
# print(employee["department"]) # IT

# # Add new key-value
# employee["location"] = "Ahmedabad"

# # Update value
# employee["salary"] = 700000

# # Loop through dictionary
# for key, value in employee.items():
#     print(key, ":", value)
    

# hybrid inheritance
# class A:
#     def function_A(self):
#         print("I AM CLASS A")

# class B(A):
#      def function_B(self):
#         print("I AM CLASS B")


# class C:
#      def function_C(self):
#         print("I AM CLASS C")


# class D(B,C):
#      def function_D(self):
#         print("I AM CLASS D")


# d1=D()
# d1.function_A()
# d1.function_B()
# d1.function_C()
# d1.function_D()


# hierarchical inheritance
class A:
    def function_A(self):
        print("I AM CLASS A")

class B(A):
     def function_B(self):
        print("I AM CLASS B")


class C(A):
     def function_C(self):
        print("I AM CLASS C")


class D(A):
     def function_D(self):
        print("I AM CLASS D")

class E(B):
    def function_E(self):
        print("I AM CLASS E")

d1 = D()
d1.function_A()   # Works (from A)
d1.function_D()   # Works (from D)

e1 = E()
e1.function_A()   # Works (from A via B)
e1.function_B()   # Works (from B)
e1.function_E()   # Works (from E)





