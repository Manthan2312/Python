x=22
print(f"The global variable {x}")


def my_function():
    y=12
    x=5
    print(f"The local variable {x}")


my_function()
#print(y) #THROWING THE ERROR BECAUSE OF Y IS IN THE FUNCTION SO THAT IS 
#CONSIDER AS A LOCAL SCOPE VARIABLE


name="Manthan"

def my_name():
    name1="Orange"
    print(name1)

# name="Rakesh"
print(name)
# print(name1) #THROWING THE ERROR BECAUSE OF name1 IS IN THE
my_name()





count=0

def increment():
    # global count  #if we use global keyword that
    count+=1
    
    print(count) #THROWING THE ERROR BECAUSE OF count IS IN THE GLOBAL SCOPE


increment()



