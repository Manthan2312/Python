# class students:
#     school_name="SNVV"

#     def __init__(self,Name,RollNo,Age):
#         self.name=Name
#         self.rollno=RollNo
#         self.age=Age

#     def infodetails(self):
#         print(self.name)
#         print(self.rollno)
#         print(self.age)
#         print(self.school_name)

#     # @classmethod
#     def changesninfo(cls, schoolname):
#         cls.school_name = schoolname


# s1=students("Manthan",2252,20)
# # s1.changesninfo("Ambika school")
# s1.infodetails()
# s2=students("Khushbu",2251,20)
# s2.infodetails()


class emp:
    company_name="Apple"

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def info(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print(self.company_name)





e1=emp("Manthan",20,30000)
e1.company_name="Microsoft"
e1.info()
e2=emp("Tirth",20,50000)
e2.info()


        


