class emp:
        
    def __init__(self,name,age,department,salary):
        self.e_name=name
        self.e_age=age
        self.e_department=department
        self.e_salary=salary
        if self.e_salary>=0:
              self.e_salary=salary
        else:
            self.e_salary="Invalid salary amount"
          

    def showdetailsemp(self):
        print(self.e_name)
        print(self.e_age)
        print(self.e_department)
        print(self.e_salary)


    def incomtextdetails(self):
        if self.e_salary==str(self.e_salary):
            exit()
        elif self.e_salary>1200000:
            self.afterincometax=self.e_salary/100*12
            print("Your Taxable Amount:",self.afterincometax)
        elif self.e_salary<=1200000 and self.e_salary>800000:
            self.afterincometax=self.e_salary/100*10
            print("Your Taxable Amount:",self.afterincometax)
        elif self.e_salary<=800000 and self.e_salary>500000:
            self.afterincometax=self.e_salary/100*8
            print("Your Taxable Amount:",self.afterincometax)
        else :
            print("You have no tax")

        self.e_salary=self.e_salary-self.afterincometax
        print("AFTER INCOME TAX SALARY:",self.e_salary)


    def investment(self):
        while True:
            print("1.Press 1 For Bond that have 12% return")
            print("2.Press 2 For FD that have 7% return")
            print("3.Press 3 For LIC that have 10% return")
            print("4.Press 4 For Exit")
            
            cinve=int(input("Enter Your Invetment chooise\n"))
            match cinve:
                case 1:
                        investment_amount=self.afterincometax/100*12
                        print(investment_amount)
                case 2:
                        investment_amount=self.afterincometax/100*7
                        print(investment_amount)
                case 3:
                        investment_amount=self.afterincometax/100*10
                        print(investment_amount)
                case 4:
                        break
                      
                case __:
                        print("Invalid Choice")
                    
            try:
                self.e_salary=self.e_salary-investment_amount
                print("AFTER INVESTMENT TAX SALARY:",self.e_salary)
            except Exception as e:
                print("Invalid input",e)




    def expensiveness(self):
        #  print()
         ex=int(input("Enter your total expensive In Number form\n"))
         self.e_salary=self.e_salary-ex
         print(self.e_salary)
         
             

e1=emp("Manthan",20,"Computer sci",-72000000)
e1.showdetailsemp()
e1.incomtextdetails()
e1.investment()
e1.expensiveness()
