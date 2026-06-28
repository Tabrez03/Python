# 📊 Data Analyzer and Transformer Program

A simple menu-driven Python application that allows users to input a dataset and perform various data analysis and transformation operations. This project demonstrates the use of Python functions, recursion, filtering, sorting, and list operations.

---

## 🚀 Features

* 📥 Input a 1D dataset
* 📋 Display dataset summary
* 🔢 Calculate the factorial of a number using recursion
* 🔍 Filter data using a threshold value
* 📈 Sort data in ascending or descending order
* 📊 Display dataset statistics
* 🚪 Exit the program safely

---

## 🛠️ Concepts Used

* Python Functions
* Recursion
* Lists
* Lambda Functions
* `filter()`
* `sorted()`
* Multiple Return Values
* Menu-Driven Programming
* User Input Handling

---

## 📂 Menu Options

```text
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
```

---

## 📖 Function Descriptions

### `summary()`

Returns:

* Total number of elements
* Maximum value
* Minimum value
* Sum of all elements
* Average of the dataset

---

### `factorial(n)`

Calculates the factorial of a number using recursion.

**Example**

```text
Input : 5
Output: 120
```

---

### `fil(m)`

Filters all values greater than or equal to the threshold using Python's `filter()` function.

**Example**

```text
Dataset : [5, 10, 15, 20]
Threshold : 12

Output:
[15, 20]
```

---

### `sort_Arr()`

Sorts the dataset in:

* Ascending Order
* Descending Order

---

### `multi_val()`

Returns:

* Maximum Value
* Minimum Value
* Sum of Values
* Average Value

---

## ▶️ Sample Output

```text
Welcome to the Data Analyzer and Transformer Program

1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program

Please enter your choice: 1

Enter data for a 1D array:
10 25 8 40 16

Data has been stored successfully!
```

---

## 💻 Requirements

* Python 3.x

No external libraries are required.

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/data-analyzer-transformer.git
```

2. Navigate to the project folder.

```bash
cd data-analyzer-transformer
```

3. Run the program.

```bash
python main.py
```

---

## 📁 Project Structure

```text
Data-Analyzer-and-Transformer/
│
├── main.py
├── README.md
```

---

## 📚 Learning Outcomes

This project helps you practice:

* Writing reusable functions
* Recursion in Python
* List manipulation
* Lambda expressions
* Filtering and sorting data
* Returning multiple values from functions
* Building menu-driven console applications
* Improving problem-solving skills

---

## 🔮 Future Improvements

* Add input validation
* Handle invalid menu choices
* Support decimal numbers
* Save and load datasets from files
* Calculate median, mode, and standard deviation
* Display graphs using Matplotlib
* Export results to CSV

---

## 👨‍💻 Author

**Tabrez Bazer**

Data Science Student | Python Learner

---

## 📄 License

This project is created for educational purposes and is free to use and modify.
