class emp:
    def __init__(self, name, age, salary, position):
        print("The Employees Details")
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

    def info(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.salary}")
        print(f"{self.position}")


e1=emp("Manthan",23,20000,"php developer")
e1.info()
e2=emp("Khushbu",23,100000,"The Good Girl")
e2.info()
