class students:
    def __init__(self,Name,Age,div):
        self.name=Name
        self.age=Age
        self.divandclass=div

    def info(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.divandclass}")


class marks(students):
    def __init__(self,math,sci,eng,ss,computer):
        self.math=math
        self.sci=sci
        self.eng=eng
        self.ss=ss
        self.computer=computer

    def marksinfo(self):
        total=self.math+self.sci+self.eng+self.ss+self.computer
        pr=(total/500)*100
        print(f"you got {pr}")

s2=students("Manthan",20,"imscit-c")

s2.info()

s2=marks(42,56,63,55,88)
s2.marksinfo()

