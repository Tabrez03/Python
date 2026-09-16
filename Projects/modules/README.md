# Multi-Utility Toolkit

A modular, menu-driven Python application that combines useful **date/time, mathematical, random-data, UUID, file-handling, and module-exploration utilities** into one easy-to-use command-line toolkit.

## 📌 Project Overview

The **Multi-Utility Toolkit** is designed to demonstrate how Python's built-in modules can work together with custom modules.

Instead of creating separate programs for each task, this project provides a single interactive menu where users can select the utility they need.

The main program imports functions from a custom `modules` package and provides a simple command-line interface.

## ✨ Features

### 1. 🕒 Datetime and Time Operations

* Display the current date and time
* Calculate the difference between two dates
* Format dates into different formats
* Start a stopwatch
* Start a countdown timer

### 2. 🧮 Mathematical Operations

* Calculate factorial
* Calculate compound interest
* Perform trigonometric calculations:

  * Sine
  * Cosine
  * Tangent
* Calculate the area of:

  * Circle
  * Rectangle
  * Triangle

### 3. 🎲 Random Data Generation

* Generate a random number within a specified range
* Generate a random list
* Create a random password
* Generate a random OTP

### 4. 🆔 UUID Generation

* Generate a unique identifier using UUID

### 5. 📁 File Operations

Using custom file-handling functions, the program can:

* Create a new file
* Write data to a file
* Read data from a file
* Append data to a file

### 6. 🔍 Module Attribute Explorer

The program allows users to enter a module name and explore its available attributes using:

```python
importlib.import_module()
dir()
```

This is useful for learning how Python modules and their attributes can be inspected dynamically.

## 🗂️ Project Structure

```text
Multi-Utility-Toolkit/
│
├── main.py
│
├── modules/
│   ├── __init__.py
│   ├── datetime_tools.py
│   ├── math_tools.py
│   ├── random_tools.py
│   ├── uuid_tools.py
│   └── file_tools.py
│
└── README.md
```

> The exact filenames inside the `modules` package can be changed according to your implementation.

## 🛠️ Technologies Used

* Python 3
* `datetime`
* `importlib`
* `math`
* `random`
* `uuid`
* Custom Python modules
* Command-Line Interface (CLI)

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone or Download the Project

Place the project folder on your computer.

### 3. Check the Module Structure

Make sure the custom `modules` package is available in the same project directory as the main program.

### 4. Run the Program

If your main file is named `main.py`:

```bash
python main.py
```

## 🖥️ Main Menu

When the program starts, it displays:

```text
===================================
Welcome to Multi-Utility Toolkit
===================================
Choose an option:
    1. Datetime and Time Operations
    2. Mathematical Operations
    3. Random Data Generation
    4. Generate Unique Identifiers (UUID)
    5. File Operation (Custom Module)
    6. Explore Module Attributes (dir())
    7. Exit
```

## 📅 Date Format

For date input, the program uses:

```text
DD-MM-YYYY
```

Example:

```text
16-09-2026
```

The program can also display dates in formats such as:

```text
DD/MM/YYYY
YYYY-MM-DD
DD Month, YYYY
DD-MM-YYYY HH:MM:SS
```

## 📐 Mathematical Operations

### Factorial

Example:

```text
Enter Number to Find of Factorial: 5
```

The factorial utility calculates:

```text
5! = 120
```

### Compound Interest

The program accepts:

* Principal amount
* Rate of interest
* Time in years

and calculates the compound-interest result.

### Trigonometry

The toolkit supports:

* Sine
* Cosine
* Tangent

Users can enter an angle in degrees.

### Geometry

The toolkit supports area calculations for:

* Circle
* Rectangle
* Triangle

## 🎲 Random Data Generation

Users can generate:

```text
Random Number
Random List
Random Password
Random OTP
```

The range, list size, password length, and OTP length are provided interactively.

## 📁 File Handling

The file-operation menu provides four operations:

```text
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
```

These operations are implemented through functions imported from the custom `modules` package.

## 🔎 Dynamic Module Exploration

One of the educational features of this project is the ability to inspect modules dynamically.

The program uses:

```python
module_obj = importlib.import_module(mod_name)
attributes = dir(module_obj)
```

For example, entering:

```text
math
```

allows the program to display the attributes available in Python's `math` module.

## 🧠 Python Concepts Demonstrated

This project demonstrates several important Python concepts:

* Functions
* Custom modules and packages
* Import statements
* `datetime`
* Exception handling with `try` and `except`
* `while` loops
* Conditional statements
* Nested menus
* Lists
* Numeric operations
* String formatting
* File handling
* Dynamic imports
* `dir()`
* User input validation
* Modular programming

## 🛡️ Input Validation

The program includes error handling for many invalid inputs, such as:

* Non-numeric menu choices
* Invalid dates
* Negative mathematical values
* Invalid ranges
* Invalid password lengths
* Invalid OTP lengths
* Missing Python modules

This helps make the command-line application more user-friendly.

## 🎯 Purpose of the Project

The main purpose of this project is to practice **Python fundamentals and modular programming** by combining multiple utilities into one application.

It is useful for learning how a larger Python program can be divided into smaller, reusable modules.

## 🔮 Future Improvements

Possible improvements include:

* Add a graphical user interface (GUI)
* Add more mathematical functions
* Add unit conversion tools
* Add temperature and currency converters
* Improve password generation options
* Add colored CLI output
* Add logging
* Add automated tests
* Improve menu navigation
* Add configuration settings
* Add more file-management features

## 👨‍💻 Author

**Tabrez**

## 📄 License

This project is created for educational and learning purposes. You may modify and improve it according to your needs.
