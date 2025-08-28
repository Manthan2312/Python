# class country:
#     name=""
#     independenceyear=0

#     def infogetter(self,name,india):
#         self.name=name
#         self.independenceyear=inde

#     def infosetter(self):
#         print(f"{self.name}")
#         print(f"{self.independenceyear}")


# c1=country()
# c1.infogetter("india",1947)
# c1.infosetter()


# class country:
#     def __init__(self,name,ind=0):
#         self.name=name
#         self.indepedence=ind
       
#     @property
#     def indp(self):
#         return self.indepedence,self.name
     
    

#     @indp.setter
#     def indp(self,year,name):
#         self.indepedence=year
#         self.name=name

    

# c1= country("india",1947)

# print(c1.indepedence)
# c1.indepedence=1950
# print(c1.indepedence)



# class Country:
#     def __init__(self, name, year):
#         self.name = name
#         self.independenceyear = year


# c1 = Country("India", 1947)
# print(c1.name)               # direct access
# print(c1.independenceyear)

# c1.independenceyear = 1950   # direct update
# print(c1.independenceyear)




# class Country:
#     def __init__(self, name, year):
#         self._name = name
#         self._independenceyear = year

#     @property
#     def independenceyear(self):         # getter
#         return self._independenceyear

#     @independenceyear.setter
#     def independenceyear(self, year):   # setter with validation
#         if year < 0:
#             raise ValueError("Year cannot be negative!")
#         self._independenceyear = year


# c1 = Country("India", 1947)

# print(c1.independenceyear)   # still works like before
# c1.independenceyear = 1950   # still works
# print(c1.independenceyear)

# c1.independenceyear = -100   # ❌ raises error now




class Emp:
    def __init__(self, name, age, salary, position):
        self.name = name
        self._age = age       # use private attributes (_age, _salary)
        self._salary = salary
        self.position = position

    # ------- Age Property -------
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Age must be a number")
            if value < 0:
                raise ValueError("Please enter a valid age")
            elif value < 20 or value > 60:
                raise ValueError("Invalid age for company rules")
            self._age = value
            print("Age updated successfully!")
        except Exception as e:
            print("Error:", e)

    # ------- Salary Property -------
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Salary must be a number")
            if value < 20000 or value > 200000:
                raise ValueError("Not valid salary")
            self._salary = value
            print("Salary updated successfully!")
        except Exception as e:
            print("Error:", e)

    # ------- Info Property -------
    @property
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Position: {self.position}"


# Example usage
e1 = Emp("Manthan", 25, 150000, "Rust Developer")

print(e1.info)     # display employee info

e1.age = 18        # invalid age (too young)
e1.age = 61        # invalid age (too old)
e1.age = 30        # valid

e1.salary = 15000  # invalid salary
e1.salary = 250000 # invalid salary
e1.salary = 75000  # valid

print(e1.info)     # updated employee info

