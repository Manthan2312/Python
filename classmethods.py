class students:
    school_name="SNVV"

    def __init__(self,Name,RollNo,Age):
        self.name=Name
        self.rollno=RollNo
        self.age=Age

    def infodetails(self):
        print(self.name)
        print(self.rollno)
        print(self.age)
        print(self.school_name)

    # @classmethod
    def changesninfo(cls, schoolname):
        cls.school_name = schoolname


s1=students("Manthan",2252,20)
s1.changesninfo("Ambika school")
s1.infodetails()
s2=students("Khushbu",2251,20)
s2.infodetails()
