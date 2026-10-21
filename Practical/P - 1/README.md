# Smart Expense Tracker

A simple Python-based **Smart Expense Tracker** that allows users to record, analyze, filter, and visualize their daily expenses.

The project uses **Pandas, NumPy, Matplotlib, and Seaborn** to manage expense data and generate useful financial reports.

## Features

- Add new expenses
- Validate expense amounts and categories
- Store expenses in a CSV file
- View spending percentage by category
- Calculate monthly average spending
- Display statistical information about expenses
- Filter expenses by category
- Generate visual financial reports
- Automatically save expense data to `expenses.csv`
- Generate charts and save them as `chart.png`

## Technologies Used

- **Python**
- **NumPy** – Numerical calculations
- **Pandas** – Data handling and CSV management
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Datetime** – Date validation

## Project Structure

```text
Smart-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── chart.png
└── README.md
```

> `expenses.csv` and `chart.png` are created/updated automatically when the program is used.

## Installation

### 1. Install Python

Make sure Python 3.x is installed on your computer.

You can check your Python version with:

```bash
python --version
```

### 2. Install Required Libraries

Run:

```bash
pip install numpy pandas matplotlib seaborn
```

## How to Run

Run the Python program from the project directory:

```bash
python expense_tracker.py
```

The application will display a menu:

```text
==============================
   SMART EXPENSE TRACKER
==============================
1. Add New Expense
2. View Summary
3. Filter Expenses by Category
4. Generate Financial Report
5. Exit
```

Enter the number corresponding to the operation you want to perform.

## Adding an Expense

Select:

```text
1. Add New Expense
```

You will be asked for:

- Date
- Amount
- Category
- Description

### Supported Categories

- Food
- Transport
- Utilities
- Entertainment

### Example

```text
Enter Date (YYYY-MM-DD): 2026-10-21
Enter Amount: 250
Enter Category (Food, Transport, Utilities, Entertainment): Food
Enter Description: Lunch
```

The expense will be saved to `expenses.csv`.

## View Summary

Select:

```text
2. View Summary
```

The program displays:

### Spending Percentage by Category

Shows what percentage of total spending belongs to each category.

### Monthly Average Spending

Calculates the average expense amount for each month.

### Detailed Statistical Summary

Displays statistical information such as:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median
- 75th percentile
- Maximum

## Filter Expenses

Select:

```text
3. Filter Expenses by Category
```

For example:

```text
Enter category to filter (e.g., Food, Transport): Food
```

The program will display all expenses belonging to the selected category.

## Generate Financial Report

Select:

```text
4. Generate Financial Report
```

The program generates four visualizations:

1. **Category Totals** – Bar chart showing total spending for each category.
2. **Spending Percentage** – Pie chart showing the percentage of spending by category.
3. **Daily Spending** – Line chart showing spending over time.
4. **Amount Frequency** – Histogram showing the distribution of expense amounts.

The generated report is saved as:

```text
chart.png
```

## CSV Data Format

The application stores expense information in `expenses.csv`.

Example:

```csv
Date,Amount,Category,Description
2026-10-20,250,Food,Lunch
2026-10-20,100,Transport,Bus
2026-10-21,500,Entertainment,Movie
2026-10-21,1200,Utilities,Electricity Bill
```

## Data Validation

The program validates:

- Date format must be `YYYY-MM-DD`
- Amount must be a number
- Amount must be greater than zero
- Category must be one of the supported categories

Invalid input produces an appropriate error message instead of adding the expense.

## Example Workflow

```text
1. Add New Expense
       ↓
2. Data is saved to expenses.csv
       ↓
3. View Summary
       ↓
4. Analyze spending
       ↓
5. Filter by category
       ↓
6. Generate Financial Report
       ↓
7. View chart.png
```

## Future Improvements

Possible future enhancements include:

- Edit existing expenses
- Delete expenses
- Search expenses by date
- Filter expenses by date range
- Set monthly budgets
- Display budget alerts
- Export reports to PDF
- Add a graphical user interface (GUI)
- Add password/user authentication
- Store data in SQLite instead of CSV
- Add more detailed monthly and yearly charts
- Add income tracking and savings analysis

## Author

**Smart Expense Tracker**

A Python project demonstrating:

- Object-Oriented Programming
- File handling
- Data processing
- Data validation
- Statistical analysis
- Data visualization

## License

This project is intended for educational and personal use.