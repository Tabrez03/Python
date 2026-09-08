# 📔 Personal Journal Manager

A simple **Personal Journal Manager** built with Python using **Object-Oriented Programming (OOP)** and **file handling**.
The program allows users to create, view, search, and delete journal entries through an easy-to-use command-line interface.

---

## ✨ Features

* ➕ **Add a New Entry** — Write and save a journal entry.
* 📖 **View All Entries** — Display all saved journal entries.
* 🔍 **Search for an Entry** — Search journal entries using a word or phrase.
* 🗑️ **Delete All Entries** — Delete all saved journal entries.
* 🚪 **Exit** — Safely exit the program.
* ⚠️ **Input Validation** — Handles invalid menu input without crashing.
* 📁 **Automatic File Storage** — Entries are stored in a text file named `Journalfile.txt`.

---

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **File Handling**
* **Exception Handling**
* **Command-Line Interface (CLI)**

---

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── journal.py
├── Journalfile.txt
└── README.md
```

> `Journalfile.txt` is created automatically when the first journal entry is added.

---

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/Personal-Journal-Manager.git
```

### 3. Navigate to the Project Folder

```bash
cd Personal-Journal-Manager
```

### 4. Run the Program

```bash
python journal.py
```

---

## 📋 Menu Options

When the program starts, you will see:

```text
-------------------------------------
Welcome to Personal Journal Manager!
-------------------------------------

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter Input:
```

### 1️⃣ Add a New Entry

Select option `1` and enter your journal entry.

Example:

```text
Enter your journal entry:
Today I learned Python file handling.

Entry successfully added!
```

The entry is saved inside `Journalfile.txt`.

---

### 2️⃣ View All Entries

Select option `2` to display all saved journal entries.

Example:

```text
Your Journal Entries:
-------------------------------------
Today I learned Python.
I practiced file handling.
I created my first journal manager.
```

---

### 3️⃣ Search for an Entry

Select option `3` and enter a word or phrase.

Example:

```text
Enter a word to search: Python

Matching Entries:
--------------------------------------
Today I learned Python.
I practiced Python file handling.
```

---

### 4️⃣ Delete All Entries

Select option `4`.

The program asks for confirmation:

```text
Are you sure you want to delete all entries? (yes/no):
```

Enter `yes` to clear all journal entries.

```text
All entries deleted successfully.
```

---

### 5️⃣ Exit

Select option `5` to close the program.

```text
Goodbye!
```

---

## 🧠 Concepts Demonstrated

This project is useful for practicing several Python concepts.

### Object-Oriented Programming

The program uses a `JournalManager` class to organize journal-related operations.

```python
class JournalManager:
    def __init__(self):
        self.file = 'Journalfile.txt'
```

### File Handling

The program uses different file modes:

* `a` — Append new entries
* `r` — Read existing entries
* `w` — Clear all entries

### Exception Handling

`FileNotFoundError` is handled when the journal file does not exist.

```python
try:
    # File operation
except FileNotFoundError:
    print("The journal file does not exist.")
```

### Input Validation

The program prevents invalid menu input from crashing the application.

```python
try:
    choice = int(input("Enter Input: "))
except ValueError:
    print("Enter Valid Choice!")
```

---

## 🔮 Future Improvements

Some possible improvements for this project are:

* 📅 Add dates and timestamps to entries
* ✏️ Edit existing journal entries
* 🔐 Add password protection
* 🗂️ Organize entries by date or category
* 🔎 Make searching case-insensitive
* 🖥️ Create a graphical user interface (GUI)
* 💾 Store entries using JSON or a database
* 🗑️ Allow users to delete individual entries

---

## 🎯 Learning Objective

The main goal of this project is to practice:

> **Python OOP + File Handling + Exception Handling + User Input**

It is a beginner-friendly project that demonstrates how Python can be used to create a practical command-line application.

---

## 👨‍💻 Author

**Your Name**

If you found this project useful, feel free to ⭐ the repository!

---

## 📜 License

This project is created for **educational and learning purposes**.
