class emp:
    Name="Manthan"
    Position="Php developer"
    Age=20
    Salary=40000

    def info(self):
        print(f"The Name of that employee is {self.Name}")
        print(f"The Age of that employee is {self.Age}")
        print(f"The Position of that employee is {self.Position}")
        print(f"The salary of that employee is {self.Salary}")

e1 = emp()
e1.info()
print("--------------------")
e2= emp()
e2.Name="Khushubu"
e2.Age="20"
e2.Position="HR"
e2.Salary=50000
e2.info()


      