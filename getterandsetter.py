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



class Country:
    def __init__(self, name, year):
        self.name = name
        self.independenceyear = year


c1 = Country("India", 1947)
print(c1.name)               # direct access
print(c1.independenceyear)

c1.independenceyear = 1950   # direct update
print(c1.independenceyear)




class Country:
    def __init__(self, name, year):
        self._name = name
        self._independenceyear = year

    @property
    def independenceyear(self):         # getter
        return self._independenceyear

    @independenceyear.setter
    def independenceyear(self, year):   # setter with validation
        if year < 0:
            raise ValueError("Year cannot be negative!")
        self._independenceyear = year


c1 = Country("India", 1947)

print(c1.independenceyear)   # still works like before
c1.independenceyear = 1950   # still works
print(c1.independenceyear)

c1.independenceyear = -100   # ❌ raises error now
