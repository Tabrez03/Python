# 🏢 Employee Management System

A simple **Employee Management System** developed in **Python** using **Object-Oriented Programming (OOP)** concepts. This console-based application allows users to create and manage different types of employees, including **Employees**, **Managers**, and **Developers**, while demonstrating core OOP principles such as inheritance, encapsulation, constructors, method overriding, and polymorphism.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [OOP Concepts Used](#-oop-concepts-used)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Menu Options](#-menu-options)
- [Sample Output](#-sample-output)
- [Future Enhancements](#-future-enhancements)
- [Technologies Used](#-technologies-used)
- [Author](#-author)

---

## 📖 Project Overview

This project simulates a basic employee management system where users can:

- Create Employee records
- Create Manager records
- Create Developer records
- View details of stored employees

The application is menu-driven and stores data temporarily in memory using Python lists.

---

## ✨ Features

- 👨‍💼 Create Employee records
- 👔 Create Manager records
- 👨‍💻 Create Developer records
- 📋 Display Employee, Manager, or Developer details separately
- 🔒 Uses encapsulation with private attributes
- 🧬 Demonstrates inheritance and method overriding
- 🖥️ Easy-to-use console interface

---

## 🧠 OOP Concepts Used

### Classes
- `Employee`
- `Manager`
- `Developer`

### Inheritance
- `Manager` inherits from `Employee`
- `Developer` inherits from `Employee`

### Encapsulation
Private attributes are used for data protection:

- `__name`
- `__age`
- `__salary`
- `__department`
- `__programming`

### Constructor
Each class initializes its attributes using the `__init__()` constructor.

### Method Overriding
The `showInfo()` method is overridden in both `Manager` and `Developer` classes to display additional information.

### Destructor
Each class includes a `__del__()` method to demonstrate destructor syntax.

---

## 📂 Project Structure

```
Employee-Management-System/
│
├── employee_management.py
└── README.md
```

---

## ▶️ How to Run

### Prerequisites

- Python 3.x installed on your system

### Steps

1. Clone this repository:

```bash
git clone https://github.com/your-username/Employee-Management-System.git
```

2. Navigate to the project directory:

```bash
cd Employee-Management-System
```

3. Run the program:

```bash
python employee_management.py
```

---

## 📋 Menu Options

```
Choose an Operation:

1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit
```

---

## 💻 Sample Output

### Main Menu

```
---Python OOP Project: Employee Management System---

Choose an Operation:

1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit
```

### Creating an Employee

```
Enter employee name : Alice
Enter employee age : 25
Enter employee ID : EMP101
Enter employee salary : 45000

Employee is created.
```

### Displaying Employee Information

```
Employee created with Name : Alice,
Age : 25,
EID : EMP101
Salary : 45000
```

### Creating a Manager

```
Enter Manager name : Robert
Enter Manager age : 40
Enter Manager ID : MAN201
Enter Manager salary : 85000
Enter Manager's department : Human Resources

Manager is Created.
```

### Displaying Manager Information

```
Employee created with Name : Robert,
Age : 40,
EID : MAN201
Salary : 85000
Department is : Human Resources
```

---

## 🔮 Future Enhancements

- ✏️ Update employee details
- ❌ Delete employee records
- 🔍 Search employees by ID
- 💾 Store data in files (CSV/JSON)
- 🗄️ Database integration (SQLite/MySQL)
- ⚠️ Input validation and exception handling
- 📈 Salary increment functionality
- 🖥️ Graphical User Interface (Tkinter/PyQt)
- 📊 Employee statistics and reports

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## 🎯 Learning Outcomes

This project demonstrates:

- Creating classes and objects
- Constructors and destructors
- Inheritance
- Encapsulation
- Method overriding
- Polymorphism
- Lists of objects
- Menu-driven programming

---

## 👨‍💻 Author

**Tabrez Bazer**

🎓 Data Science Student  
🐍 Currently Learning Python & Object-Oriented Programming

GitHub: https://github.com/your-username

---

## 📜 License

This project is created for educational and learning purposes. Feel free to use, modify, and improve it.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub and sharing it with others learning Python!