

class rec:
    def __call__(self, x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y
    
    # def area(self,name):
    #     self.name=name
    #     print("How are you?",self.name)

class circle(rec):
    def __call__(self,x):
        self.x=x

    def area(self):
        return 3.14*self.x*self.x

e1=rec()
e1(5, 10)  # Example arguments for x and y
print(e1.area())
# e1.area("manthan")

e2=circle()
e2(5)  # Example arguments for x and y
print(e2.area())
        