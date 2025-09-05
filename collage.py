# class emp:
        
#     def __init__(self,name,age,department,salary):
#         self.e_name=name
#         self.e_age=age
#         self.e_department=department
#         self.e_salary=salary
#         if self.e_salary>=0:
#               self.e_salary=salary
#         else:
#             self.e_salary="Invalid salary amount"
          

#     def showdetailsemp(self):
#         print(self.e_name)
#         print(self.e_age)
#         print(self.e_department)
#         print(self.e_salary)


#     def incomtextdetails(self):
#         if self.e_salary==str(self.e_salary):
#             exit()
#         elif self.e_salary>1200000:
#             self.afterincometax=self.e_salary/100*12
#             print("Your Taxable Amount:",self.afterincometax)
#         elif self.e_salary<=1200000 and self.e_salary>800000:
#             self.afterincometax=self.e_salary/100*10
#             print("Your Taxable Amount:",self.afterincometax)
#         elif self.e_salary<=800000 and self.e_salary>500000:
#             self.afterincometax=self.e_salary/100*8
#             print("Your Taxable Amount:",self.afterincometax)
#         else :
#             print("You have no tax")

#         self.e_salary=self.e_salary-self.afterincometax
#         print("AFTER INCOME TAX SALARY:",self.e_salary)


#     def investment(self):
#         while True:
#             print("1.Press 1 For Bond that have 12% return")
#             print("2.Press 2 For FD that have 7% return")
#             print("3.Press 3 For LIC that have 10% return")
#             print("4.Press 4 For Exit")
            
#             cinve=int(input("Enter Your Invetment chooise\n"))
#             match cinve:
#                 case 1:
#                         investment_amount=self.afterincometax/100*12
#                         print(investment_amount)
#                 case 2:
#                         investment_amount=self.afterincometax/100*7
#                         print(investment_amount)
#                 case 3:
#                         investment_amount=self.afterincometax/100*10
#                         print(investment_amount)
#                 case 4:
#                         break
                      
#                 case __:
#                         print("Invalid Choice")
                    
#             try:
#                 self.e_salary=self.e_salary-investment_amount
#                 print("AFTER INVESTMENT TAX SALARY:",self.e_salary)
#             except Exception as e:
#                 print("Invalid input",e)




#     def expensiveness(self):
#         #  print()
#          ex=int(input("Enter your total expensive In Number form\n"))
#          self.e_salary=self.e_salary-ex
#          print(self.e_salary)
         
             

# e1=emp("Manthan",20,"Computer sci",-72000000)
# e1.showdetailsemp()
# e1.incomtextdetails()
# e1.investment()
# e1.expensiveness()

class university:
    co = 0
    fbe = 0
    en = 0
    ah = 0
    sci = 0

    # Define department subjects and teachers as class-level dictionaries
    department_subjects = {
        "Commerce": {
            "Account": "Aniket Varma",
            "Taxation": "Gopal Suthar",
            "Business Administration": "Paresh Thakor"
        },
        "Finance and Business Economics": {
            "Finance": "Nirmala Sitaraman",
            "Business": "Gautam Adani",
            "Economics": "Man Mohan Singh"
        },
        "Engineering": {
            "Information": "Amit Shah",
            "C/C++": "Kaveri Mathur",
            "DBMS": "Bill Gates"
        },
        "Arts and Humanities": {
            "Arts": "Rakesh Sharma",
            "Humanities": "Jainil Patel",
            "History": "Shish Desai"
        },
        "Science": {
            "Biology": "Sujal Roy",
            "Physics": "Ujjala Bataviya",
            "Maths": "Mark Waugh"
        }
    }

    department_workload = {
        "Commerce": {
            "Account": 4,
            "Taxation": 3,
            "Business Administration": 2
        },
        "Finance and Business Economics": {
            "Finance": 6,
            "Business": 3,
            "Economics": 2
        },
        "Engineering": {
            "Information": 5,
            "C/C++": 2,
            "DBMS": 3
        },
        "Arts and Humanities": {
            "Arts": 3,
            "Humanities": 7,
            "History": 6
        },
        "Science": {
            "Biology": 1,
            "Physics": 3,
            "Maths": 2
        }
    }

    def __init__(self, department, name, enrollment_number):
        self.u_department = department
        self.us_name = name
        self.us_enr = str(enrollment_number)
        if len(self.us_enr) == 10:
            if self.u_department == "Commerce":
                university.co += 1
            elif self.u_department == "Finance and Business Economics":
                university.fbe += 1
            elif self.u_department == "Engineering":
                university.en += 1
            elif self.u_department == "Arts and Humanities":
                university.ah += 1
            elif self.u_department == "Science":
                university.sci += 1
            else:
                self.u_department = "NO DEPARTMENT EXISTS"
        else:
            print("Not valid enrollment number")
            exit()

    def infodetailsofstudent(self):
        print(self.us_name)
        print(self.us_enr)
        if self.u_department == "NO DEPARTMENT EXISTS":
            print("Student does not have any department and not exists")
            exit()
        else:
            print(self.u_department)
        if self.u_department == "Commerce":
            print(university.co)
        elif self.u_department == "Finance and Business Economics":
            print(university.fbe)
        elif self.u_department == "Engineering":
            print(university.en)
        elif self.u_department == "Arts and Humanities":
            print(university.ah)
        elif self.u_department == "Science":
            print(university.sci)

    def departmentfacultydetails(self):
        subjects = university.department_subjects.get(self.u_department)
        if subjects:
            for subject, teacher in subjects.items():
                print(f"{subject}: {teacher}")

    def totalworkload(self):
        workloads = university.department_workload.get(self.u_department)
        if workloads:
            for subject, load in workloads.items():
                print(f"{subject}: {load}")
            total = sum(workloads.values())
            print(f"Total workload: {total}")

    def topthings(self):
        workloads = university.department_workload.get(self.u_department)
        if workloads:
            sorted_loads = sorted(workloads.values(), reverse=True)
            print(sorted_loads)



u1=university("Science","Manthan",1201231234)
u1.infodetailsofstudent()
u1.departmentfacultydetails()
u1.totalworkload()
u1.topthings()
print("--------------------------------------")
u2=university("Commerce","Tirth",1201231135)
u2.infodetailsofstudent()
u2.departmentfacultydetails()
u2.totalworkload()
u2.topthings()
print("--------------------------------------")
u3=university("Science","Khushubu",1201231236)
u3.infodetailsofstudent()
u3.departmentfacultydetails()
u3.totalworkload()
u3.topthings()

