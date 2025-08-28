# class math:
#     def __init__(self,num):
#         self.number=num

#     def addtonum(self,n):
#         self.number+=n

#     @staticmethod
#     def sub(a,b):
#         return a-b

# m1=math(1)
# print(m1.number)
# m1.addtonum(343)
# print(m1.number)
# print(m1.sub(32.453,34.42))

class bankaccount:
    def __init__(self,accn,balance):
        if not bankaccount.checkan(accn):  
            raise ValueError("Invalid account number!")
        self.accountnumber=accn
        self.balance=balance
  

    def deposit(self,inb):
        self.balance+=inb


    @staticmethod
    def checkan(accn):
        """Account number must be 10 digits long."""
        return len(str(accn)) == 12

    def info(self):
        print(self.accountnumber)
        print(self.balance)



b1=bankaccount(123456781219,5000)
b1.info()
b1.deposit(123)
b1.info()
