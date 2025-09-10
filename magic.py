class employees:
    name = "Manthan"
    # len_of_name = len(name)  # you can use this way

    def __len__(self):
        # return len(self.name)
        i=0
        for c in self.name:
            i+=1
        return i

    def __str__(self):
        return f"My name is:{self.name}"
    
    def __repr__(self):
        return f"My good name is:{self.name}"
e1 = employees()
print(e1.name)
# print(e1.len_of_name)
# print(len(e1)) # this line will not throw error now
print(len(e1))
print(e1)
print(repr(e1))
