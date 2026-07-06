class Employee:
    def __init__(self,name,age,salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def showInfo(self):
        print(f"Name : {self.__name} Age : {self.__age} Salary : {self.__salary}")

    def __delete__(self,):
        pass

class Manager(Employee):
    
    def __init__(self, name, age, salary,department):
        super().__init__(name, age, salary)
        self.__department = department

    def showInfo(self):
        super().showInfo()
        print(f"The Manager belong to {self.__department} department.")

    def __del__(self):
        pass


class Developer(Employee):
    def __init__(self, name, age, salary,programming):
        super().__init__(name, age, salary)
        self.__programming = programming

    def showInfo(self):
        super().showInfo()
        print(f"The Developer is expert in {self.program} programming.")
    def __del__(self):
        pass

emp = []
man = []
dev = []

while True:

    print('''Enter 1 to creat an employee
             Enter 2 create an manager
             Enter 3 to create an developer
             Enter 4 to view
             Enter 5 to delete''')
    
    choice = int(input("Enter your choice :"))

    if choice == 1:
        name =input("Enter emp name :")
        age = int(input("Enter emp age :"))
        salary = int(input("Enter emp salary :"))

        eobj = Employee(name,age,salary)

        emp.append(eobj)

        print("\n Employee is created !\n")


    elif choice == 2:
        name =input("Enter emp name :")
        age = int(input("Enter emp age :"))
        salary = int(input("Enter emp salary :"))
        dname = input("Enter manager department name :")

        mobj = Manager(name,age,salary,dname)
        
        man.append(mobj)

        print("\n Manager is created !\n")

    elif choice ==3:
        name =input("Enter emp name :")
        age = int(input("Enter emp age :"))
        salary = int(input("Enter emp salary :"))
        pname = input("Enter developer programming name :")

        dobj = Developer(name,age,salary,pname)

        dev.append(dobj)

        print("\nDeveloper is created !\n")

    elif choice == 4:
        subCh = int(input("Enter 1/2/3 to view Emp/Man/Dev :"))

        if subCh ==1:
            for em in emp:
                em.showInfo()    

        elif subCh ==2:
            for em in man:
                em.showInfo()    

        elif subCh ==3:
            for em in dev:
                em.showInfo()        

        else:
            print("\nInvalid !\n")

    else:
        break