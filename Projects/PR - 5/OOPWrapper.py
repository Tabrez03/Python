print("\n---Python OOP Project: Enployee Management System---\n")

class Employee:
    def __init__(self,name,age,eid,salary):
        self.__name = name
        self.__age = age
        self.eid = eid
        self.__salary = salary

    
    def showInfo(self):
        print(f"\nEmployee created with Name :{self.__name} , Age :{self.__age} , EID : {self.eid} and Salary : {self.__salary} ")


    def __del__(self):
        pass

class Manager(Employee):
    def __init__(self, name, age, eid, salary,department):
        super().__init__(name, age, eid, salary)
        self.__department = department 
        

    def showInfo(self):
        super().showInfo()
        print(f" Department is : {self.__department} ")

    def __del__(self):
        pass

class Developer(Employee):
    def __init__(self, name, age, eid, salary,Programming):
        super().__init__(name, age, eid, salary)
        self.__programming = Programming

    def showInfo(self):
        super().showInfo()
        print(f"Expert in : {self.__programming} Programing Language.")    

    def __del__(self):
        pass

emp = []
man = []
dev = []

while True:

    print('''\nChoose an Operation:
             1. Create an Employee
             2. Create a Manager
             3. Create a Developer
             4. Show Details
             5. Exit \n''')
    
    choice = int(input("Enter your choice :"))

    if choice == 1:
        name = input("Enter employee name :")
        age = int(input("Enter employee age :"))
        eid = input("Enter employee ID :")
        salary = input("Enter employee salary :")

        eobj = Employee(name,age,eid,salary)

        emp.append(eobj)

        print(f"\nEmployee is created.\n")

    elif choice == 2:
        name = input("Enter Manager name :")
        age = int(input("Enter Manager age :"))
        eid = input("Enter Manager ID :")
        salary = input("Enter Manager salary :")
        department = input("Enter Manager's department :")

        mobj =Manager(name,age,eid,salary,department)

        man.append(mobj)

        print("\nManager is Created.\n")

    elif choice ==3:
        name = input("Enter Developer name :")
        age = int(input("Enter Developer age :"))
        eid = input("Enter Developer ID :")
        salary = input("Enter Developer salary :")
        programming = input("Enter Developer programming language :")

        dobj = Developer(name,age,eid,salary,programming)

        dev.append(dobj)

        print("\nDeveloper is Created.\n")


    elif choice ==4:
        subch = int(input("\nEnter 1/2/3 to view Employee/Manager/Developer :"))

        if subch==1:
            for em in emp:
                em.showInfo()

        elif subch==2:
            for em in man:
                em.showInfo()
        

        elif subch==3:
            for em in dev:
                em.showInfo()

        else:
            print("\n Invalid Choice !\n")


    elif choice ==5:
        print("\nExiting the system. All resources have been freed.")

        print("Goodbye !")
        break

