class emp:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print(self.id)
        print(self.name)
    
class empIT(emp):
    def __init__(self,id,name, programming_lang):
        super().__init__(id, name)
        self.pl = programming_lang
        print(self.pl)    



e1=emp(2252,"Manthan")
e2 = empIT(2253, "Khushbu", "C++")



# class student:
#     def __init__(self,name,rollno,cd):
#         self.name=name
#         self.rollno=rollno
#         self.class_Division=cd

#     def info(self):
#         print(self.name)
#         print(self.rollno)
#         print(self.class_Division)

# class StudentMarks(student):
#     def __init__(self, name, rollno, cd, marks):
#         super().__init__(name, rollno, cd)
#         self.marks = marks

#     def infosm(self):
#         super().info()
#         print(self.marks)



# s1=StudentMarks("Manthan",2252,"12-B",560)
# s1.infosm()