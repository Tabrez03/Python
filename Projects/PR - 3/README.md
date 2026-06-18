# 🎓 Student Data Organizer

A simple Python console application for managing student records. This project allows users to add, view, update, and delete student information, as well as display all unique subjects offered.

## ✨ Features

* ➕ Add new students
* 📋 Display all student records
* ✏️ Update student information
* 🗑️ Delete student records
* 📚 Display all unique subjects offered
* 🚪 Exit the program safely

## 🛠️ Technologies Used

* Python 3
* Lists
* Dictionaries
* Sets
* Loops and Conditional Statements

## 📂 Data Stored for Each Student

Each student record contains:

* **ID**
* **Name**
* **Age**
* **Grade**
* **Date of Birth**
* **Subjects** (stored as a set)

Example:

```python
{
    "Id": 1,
    "Name": "John",
    "Age": 16,
    "Grade": "10th",
    "Date of Birth": "2010-05-15",
    "Subjects": {"Math", "Science", "English"}
}
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/student-data-organizer.git
```

2. Navigate to the project folder:

```bash
cd student-data-organizer
```

3. Run the program:

```bash
python student_data_organizer.py
```

## 📋 Menu Options

```
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

## 📸 Sample Output

```
Welcome to the Student Data Organizer!

Select an Option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subject Offered
6. Exit

Enter your choice: 1

Enter student name: Alice
Enter student age: 17
Enter student grade: 12th
Enter student birthdate (YYYY-MM-DD): 2009-03-21
Enter student subjects (comma-separated): Math, Science, English

Student added successfully!
```

## 🎯 Concepts Practiced

This project demonstrates:

* Lists
* Dictionaries
* Sets
* CRUD Operations (Create, Read, Update, Delete)
* Loops
* Conditional Statements
* User Input Handling
* Data Organization

## 🔮 Future Improvements

* Search students by ID or name
* Save records to a file (JSON/CSV)
* Load records automatically when the program starts
* Input validation and error handling
* Sort students by name or grade
* Build a graphical user interface (GUI)

## 👨‍💻 Author

**Tabrez Bazer**

Data Science Student | Learning Python 🐍

---

⭐ Feel free to fork this repository and contribute!
