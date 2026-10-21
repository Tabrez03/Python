# 📊 Sale Data Analyzer

A beginner-friendly **Python Data Analysis and Visualization project** built using **Pandas, Matplotlib, and Seaborn**.

This program allows users to load a CSV dataset, explore its contents, perform DataFrame operations, handle missing data, generate descriptive statistics, create different visualizations, and save charts to files.

## 🚀 Features

- 📂 Load CSV datasets
- 🔍 Explore dataset information
- 📋 Display first and last 5 rows
- 🏷️ Display column names
- 🔢 Display data types
- ℹ️ Display basic dataset information
- ➕ Perform DataFrame statistical operations
- 🧹 Handle missing values
- 📊 Generate descriptive statistics
- 📈 Create different types of charts
- 💾 Save generated visualizations
- ⚠️ Basic error handling for invalid input and files

## 📌 Data Exploration

The program provides several options for exploring the dataset:

1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic information

## 🧮 DataFrame Operations

Users can select a column and calculate:

- Sum
- Standard deviation
- Minimum value
- Maximum value

Example:

```text
Enter column name: Sales

sum     125000
std       2450
min        500
max       15000
```

## 🧹 Missing Data Handling

The program provides options for handling missing values:

1. Display rows/columns with missing values
2. Fill missing numerical values with the mean
3. Drop rows containing missing values
4. Replace missing numerical values with a user-defined value

## 📊 Statistical Analysis

The `describe()` function is used to generate summary statistics for numerical columns.

It provides information such as:

- Count
- Mean
- Standard deviation
- Minimum
- Quartiles
- Maximum

## 📈 Data Visualization

The project supports six different visualization types:

### 1. Bar Plot
Used to compare values across categories.

### 2. Line Plot
Used to show trends and changes in data.

### 3. Scatter Plot
Used to visualize relationships between two numerical variables.

### 4. Pie Chart
Used to display the proportion of different categories.

### 5. Histogram
Used to visualize the distribution of numerical data.

### 6. Stack Plot
Used to visualize cumulative trends between variables.

## 💾 Save Visualization

After generating a chart, users can save it to a file.

Example:

```text
Enter file name to save the plot (e.g., linechart.png): sales_chart.png

Visualization saved as sales_chart.png successfully!
```

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**

## 📦 Installation

Install the required libraries using:

```bash
pip install pandas matplotlib seaborn
```

## ▶️ How to Run

1. Clone or download the project.
2. Make sure Python is installed.
3. Install the required libraries.
4. Run the Python file:

```bash
python sale_data_analyzer.py
```

5. Enter the path of your CSV dataset when prompted.

Example:

```text
Enter the path of the dataset (CSV file): sales.csv
```

## 🖥️ Main Menu

```text
============ Data Analysis & Visualization Program ============

Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame operation
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
```

## 📁 Project Structure

```text
Sale-Data-Analyzer/
│
├── sale_data_analyzer.py
├── dataset.csv
└── README.md
```

## 🎯 Concepts Demonstrated

This project demonstrates practical use of:

- Object-Oriented Programming
- Classes and Objects
- Constructors
- Destructors
- Pandas DataFrames
- CSV file handling
- Data cleaning
- Missing-value handling
- Statistical analysis
- Data visualization
- Matplotlib
- Seaborn
- Exception handling
- User input and menu-driven programming

## 🔮 Future Improvements

Possible improvements include:

- Add automatic dataset validation
- Add more statistical operations
- Add correlation analysis
- Add heatmap visualization
- Add box plots and violin plots
- Export cleaned datasets
- Add a graphical user interface
- Add automatic report generation
- Improve handling of categorical missing values

## 👨‍💻 Author

**Sale Data Analyzer**

A Python data analysis project created for learning and practicing **Pandas, Matplotlib, Seaborn, and Object-Oriented Programming**.