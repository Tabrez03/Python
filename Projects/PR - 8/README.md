# NumPy Analyzer

A Python-based **NumPy Analyzer** project that combines **NumPy operations** with important **Object-Oriented Programming (OOP)** concepts.

This project allows users to create 1D, 2D, and 3D NumPy arrays and perform mathematical operations, indexing, slicing, searching, sorting, filtering, and statistical analysis.

---

## 📌 Project Overview

The **NumPy Analyzer** is designed as a console-based application for practicing:

* NumPy array operations
* Object-Oriented Programming
* Abstraction
* Encapsulation
* Inheritance
* Method overriding
* Class methods
* Static methods
* Properties and setters
* Special methods
* Array indexing and slicing
* Mathematical and statistical operations

The project uses a hierarchy of classes where each child class adds new functionality to the analyzer.

---

## 🚀 Features

### 1. Create NumPy Arrays

The program supports creating:

* 1D arrays
* 2D arrays
* 3D arrays

Users can enter their own values, which are converted into NumPy arrays.

### 2. Mathematical Operations

The program supports:

* Addition
* Subtraction
* Multiplication
* Division

Operations are performed between two arrays having the same size and shape.

### 3. Indexing and Slicing

The project demonstrates NumPy indexing and slicing for:

* 1D arrays
* 2D arrays
* 3D arrays

For 2D arrays, users can also select:

* A submatrix
* An entire column
* An entire row

### 4. Search, Sort and Filter

Users can perform:

* Searching for a specific value
* Sorting array elements
* Filtering elements greater than a specified value

### 5. Statistics

The analyzer provides:

* Sum
* Mean
* Median
* Maximum value
* Minimum value
* Standard deviation

---

## 🧠 OOP Concepts Used

This project demonstrates several important Python OOP concepts.

### Abstraction

The `NumpyAnalyzer` class inherits from `ABC` and contains an abstract method:

```python
@abstractmethod
def module_name(self):
    pass
```

Every child class must provide its own implementation of `module_name()`.

---

### Encapsulation

The array storage is kept private using:

```python
self.__arrays = []
```

A property and setter are used to control access:

```python
@property
def array(self):
    return self.__arrays

@array.setter
def array(self, value):
    if not isinstance(value, list):
        raise TypeError("Array storage must be a list.")
    self.__arrays = value
```

---

### Inheritance

The project uses multi-level inheritance:

```text
NumpyAnalyzer
      ↓
CreateArray
      ↓
MathOperation
      ↓
CombineSplitArray
      ↓
SearchSortFilter
      ↓
StatisticsAnalyzer
```

Each class inherits functionality from its parent class.

---

### Method Overriding

Every child class overrides the `module_name()` method.

For example:

```python
def module_name(self):
    return "Statistics Module"
```

This allows each class to provide its own module name.

---

### Class Variable

The project uses:

```python
object_count = 0
```

This variable keeps track of the number of analyzer objects created.

---

### Class Method

The following class method returns the object count:

```python
@classmethod
def get_object_count(cls):
    return cls.object_count
```

---

### Static Methods

The project contains static methods such as:

```python
@staticmethod
def welcome_meassage():
    ...
```

and:

```python
@staticmethod
def display_menu():
    ...
```

These methods do not require `self` or `cls`.

---

### Special Method

The `__str__()` method provides a readable description of the analyzer:

```python
def __str__(self):
    return (
        f"{self.app_name} | "
        f"Stored Arrays: {len(self.__arrays)}"
    )
```

---

## 🔢 NumPy Concepts Used

The project demonstrates several NumPy functions and techniques.

| NumPy Function  | Purpose                      |
| --------------- | ---------------------------- |
| `np.array()`    | Create NumPy arrays          |
| `np.reshape()`  | Change array shape           |
| `np.add()`      | Addition                     |
| `np.subtract()` | Subtraction                  |
| `np.multiply()` | Multiplication               |
| `np.divide()`   | Division                     |
| `np.where()`    | Search for values            |
| `np.sort()`     | Sort array elements          |
| `np.sum()`      | Calculate sum                |
| `np.mean()`     | Calculate average            |
| `np.median()`   | Calculate median             |
| `np.max()`      | Find maximum                 |
| `np.min()`      | Find minimum                 |
| `np.std()`      | Calculate standard deviation |

---

## 📂 Class Structure

### `NumpyAnalyzer`

Base abstract class containing:

* Array storage
* Object counter
* Property and setter
* Class method
* Static methods
* Abstract method
* String representation
* Array availability checking

### `CreateArray`

Responsible for:

* Creating 1D arrays
* Creating 2D arrays
* Creating 3D arrays

### `MathOperation`

Responsible for:

* Creating a second array
* Addition
* Subtraction
* Multiplication
* Division

### `CombineSplitArray`

Responsible for:

* Indexing
* Slicing
* Working with 1D, 2D, and 3D arrays

### `SearchSortFilter`

Responsible for:

* Searching
* Sorting
* Filtering

### `StatisticsAnalyzer`

Responsible for:

* Sum
* Mean
* Median
* Maximum
* Minimum
* Standard deviation

---

## 🛠️ Requirements

Make sure Python is installed on your computer.

You also need NumPy.

Install NumPy using:

```bash
pip install numpy
```

Check the installation:

```bash
python -c "import numpy; print(numpy.__version__)"
```

---

## ▶️ How to Run

1. Clone or download the project.

2. Open the project folder in your terminal.

3. Install NumPy:

```bash
pip install numpy
```

4. Run the Python program:

```bash
python filename.py
```

Replace `filename.py` with the actual name of your Python file.

---

## 💡 Example

A 1D array can be created by entering:

```text
Enter elements separated by spaces: 10 20 30 40 50
```

The resulting NumPy array will be:

```text
[10 2]()
```
