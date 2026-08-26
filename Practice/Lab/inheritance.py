# Task 1:
class Person:

    def __init__(self, name,  age):
        self.name=name
        self.age=age

class Student(Person):

    def __init__(self, name, age, roll_no, year):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.year=year

    def display_data(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll No : {self.roll_no}")
        print(f"Standard : {self.year}")

student1=Student("Tabrez",21,111,"1st year")
student1.display_data()


# Task 2:
class Vehicle:

    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

class Car(Vehicle):

    def __init__(self, brand, model, fuel_type):
        super().__init__(brand,model)
        self.fuel_type=fuel_type

    def display_data(self):
        print(f"\nBrand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Fuel Type : {self.fuel_type}")

car1=Car("BMW","M4","Petrol")
car1.display_data()

# Task 3:

class Employee:

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name,salary)
        self.department=department

    def display_data(self):
        print(f"\nName : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"Department : {self.department}")

employee1=Manager("Vivek",26000,"IT")
employee1.display_data()

# Task 4:
class BankAccount:

    def __init__(self, account_no, holder_name ,balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.balance=balance

class SavingsAccount(BankAccount):

    def __init__(self, account_no, holder_name, balance, interest_rate):
        super().__init__(account_no,holder_name,balance)
        self.interest_rate=interest_rate

    def display_data(self):
        print(f"\nAccount No : {self.account_no}")
        print(f"Holder Name : {self.holder_name}")
        print(f"Balance : {self.balance}")
        print(f"Interest Rate : {self.interest_rate}%")
        print(f"Interest : {self.balance * self.interest_rate / 100}")

account1=SavingsAccount(1234321,"Sumit",20000,10)
account1.display_data()

# Task 5:
class Product:

    def __init__(self, product_name, price):
        self.product_name=product_name
        self.price=price

class Electronics(Product):

    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name,price)
        self.brand=brand
        self.warranty=warranty

    def display_data(self):
        print(f"\nProduct : {self.product_name}")
        print(f"Price : {self.price}")
        print(f"Brand : {self.brand}")
        print(f"Warranty : {self.warranty} years")

product1=Electronics("Mobile",100000,"Redmagic",5)
product1.display_data()

        