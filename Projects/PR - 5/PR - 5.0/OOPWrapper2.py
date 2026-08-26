from abc import ABC, abstractmethod
from datetime import datetime
import random


class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Customer(Person):

    def __init__(self, name, age, address, customer_id):
        super().__init__(name, age, address)
        self.customer_id = customer_id

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Address : {self.address}")
        print(f"Customer ID : {self.customer_id}")


class Account(ABC):

    __total_account = 0

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        self.transaction = []
        Account.__total_account += 1

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount!")
            return

        self.__balance += amount

        self.transaction.append({
            "Type": "Deposit",
            "Amount": amount,
            "Time": datetime.now()
        })

        print("Money deposited successfully.")

    @abstractmethod
    def withdraw(self, amount):
        pass

    @staticmethod
    def get_total_account():
        return Account.__total_account


class Savingsaccount(Account):

    def __init__(self, account_number, account_holder, interest_rate, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount!")
            return

        if amount > self.balance:
            print("Insufficient Balance")
            return

        self.balance -= amount

        self.transaction.append({
            "Type": "Withdraw",
            "Amount": amount,
            "Time": datetime.now()
        })

        print("Money withdrawn successfully.")

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

    def acc_type(self):
        return "Saving Account"

    def display(self):
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Interest Rate : {self.interest_rate}%")
        print(f"Account Type : {self.acc_type()}")
        print(f"Balance : {self.balance}")


class Currentaccount(Account):

    def __init__(self, account_number, account_holder, overdraft_limit, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount!")
            return

        if self.balance - amount < -self.overdraft_limit:
            print("Insufficient balance!")
            return

        self.balance -= amount

        self.transaction.append({
            "Type": "Withdraw",
            "Amount": amount,
            "Time": datetime.now()
        })

        print("Money withdrawn successfully.")

    def acc_type(self):
        return "Current Account"

    def display(self):
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Overdraft Limit : {self.overdraft_limit}")
        print(f"Account Type : {self.acc_type()}")
        print(f"Balance : {self.balance}")


class Bank:

    customers = []
    accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def add_customer(self, customer):
        self.customers.append(customer)

    @staticmethod
    def no_account():
        print(Account.get_total_account())


while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Print Statement")
    print("7. View Total Accounts (staticmethod)")
    print("8. Exit")

    choice = int(input("\nEnter your choice : "))


    if choice == 1:

        print("\nWelcome !, please enter your some details")

        name = input("Enter your Name : ")
        age = int(input("Enter your Age : "))
        address = input("Enter your Address : ")

        customer_ID = random.randint(1111, 9999)

        customer1 = Customer(name, age, address, customer_ID)

        Bank.customers.append(customer1)

        customer1.display()

        print("\n1. Saving Account")
        print("2. Current Account")

        sub_choice = int(input("\nPlease enter your choice of Account : "))

        if sub_choice == 1:

            account_number = random.randint(111111111111, 999999999999)

            saving1 = Savingsaccount(
                account_number,
                name,
                4
            )

            Bank.accounts.append(saving1)

            saving1.display()

        elif sub_choice == 2:

            account_number = random.randint(111111111111, 999999999999)

            current1 = Currentaccount(
                account_number,
                name,
                50000
            )

            Bank.accounts.append(current1)

            current1.display()

        else:
            print("Invalid account choice!")


    elif choice == 2:

        print("\n===== DEPOSIT MONEY =====")

        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))

        found = False

        for account in Bank.accounts:

            if account.account_number == account_number:

                account.deposit(amount)

                found = True

                break

        if not found:
            print("\nAccount not found!")


    elif choice == 3:

        print("\n===== WITHDRAW MONEY =====")

        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))

        found = False

        for account in Bank.accounts:

            if account.account_number == account_number:

                account.withdraw(amount)

                found = True

                break

        if not found:
            print("\nAccount not found.")


    elif choice == 4:

        print("\n===== TRANSFER MONEY =====")

        sender_number = int(input("Enter sender account number: "))
        receiver_number = int(input("Enter receiver account number: "))
        amount = float(input("Enter transfer amount: "))

        sender = None
        receiver = None

        for account in Bank.accounts:

            if account.account_number == sender_number:
                sender = account

            elif account.account_number == receiver_number:
                receiver = account

        if sender is None:

            print("\nSender account not found.")

        elif receiver is None:

            print("\nReceiver account not found.")

        elif amount <= 0:

            print("\nInvalid transfer amount.")

        elif sender.balance < amount:

            print("\nInsufficient balance.")

        else:

            sender.balance -= amount
            receiver.balance += amount

            sender.transaction.append({
                "Type": "Transfer Sent",
                "Amount": amount,
                "Time": datetime.now()
            })

            receiver.transaction.append({
                "Type": "Transfer Received",
                "Amount": amount,
                "Time": datetime.now()
            })

            print("Money transferred successfully.")


    elif choice == 5:

        print("\n===== CHECK BALANCE =====")

        account_number = int(input("Enter account number: "))

        found = False

        for account in Bank.accounts:

            if account.account_number == account_number:

                print(f"Account Number : {account.account_number}")
                print(f"Account Holder : {account.account_holder}")
                print(f"Account Type   : {account.acc_type()}")
                print(f"Balance        : ₹{account.balance}")

                found = True

                break

        if not found:
            print("Account not found.")


    elif choice == 6:

        print("\n===== ACCOUNT STATEMENT =====")

        account_number = int(input("Enter account number: "))

        found = False

        for account in Bank.accounts:

            if account.account_number == account_number:

                print(f"\nAccount Number : {account.account_number}")
                print(f"Account Holder : {account.account_holder}")
                print(f"Account Type   : {account.acc_type()}")
                print(f"Balance        : ₹{account.balance}")

                print("\n===== TRANSACTIONS =====")

                if len(account.transaction) == 0:

                    print("No transactions found.")

                else:

                    for transaction in account.transaction:

                        print(f"\nType   : {transaction['Type']}")
                        print(f"Amount : ₹{transaction['Amount']}")
                        print(f"Time   : {transaction['Time']}")

                found = True

                break

        if not found:
            print("\nAccount not found.")


    elif choice == 7:

        print("\n===== TOTAL ACCOUNTS =====")

        Bank.no_account()


    elif choice == 8:

        print("Thank you!")

        break


    else:

        print("Invalid choice!")