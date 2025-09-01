class student:
    school_name="Snvv"       # class variable 
    numberofst=0
    def __init__(self,name,age,rollno):
        self.name=name                        # instance variable
        self.age=age                                      # instance variable
        self.rollno=rollno                               # instance variable
        student.numberofst+=1


    def  infoofs(self):
        print(self.name)
        print(self.age)
        print(self.rollno)
        print(student.school_name)
        print(student.numberofst)



s1=student("Manthan",20,2252)
s1.infoofs()
s2=student("Het",15,17)
s2.school_name="Navsarjan"
s2.infoofs()
        