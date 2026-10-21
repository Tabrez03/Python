# ETF vs Stock Count by Listing Exchange

## Overview

This program uses **Pandas** and **Matplotlib** to visualize the number of ETFs and stocks listed on each exchange. It creates a **stacked bar chart** to compare ETF and stock counts across different listing exchanges.

## Requirements

Install the required Python libraries:

```bash
pip install pandas matplotlib
```

## Program

```python
import pandas as pd
import matplotlib.pyplot as plt

pd.crosstab(df['Listing Exchange'], df['ETF']).plot(
    kind='bar',
    stacked=True
)

plt.title('ETF vs Stock Count in Each Exchange')
plt.ylabel('Count')
plt.xlabel('Listing Exchange')
plt.show()
```

## Input Data

The program requires a Pandas DataFrame named `df` with these columns:

- **Listing Exchange** — the exchange where the security is listed.
- **ETF** — indicates whether the security is an ETF or a stock.

Example:

| Listing Exchange | ETF |
|---|---|
| NYSE | False |
| NASDAQ | True |
| NYSE | True |
| NASDAQ | False |

## How It Works

1. `pd.crosstab()` counts ETFs and stocks for each listing exchange.
2. `kind='bar'` creates a bar chart.
3. `stacked=True` stacks ETF and stock counts in each bar.
4. `plt.title()` adds the chart title.
5. `plt.ylabel()` labels the y-axis.
6. `plt.xlabel()` labels the x-axis.
7. `plt.show()` displays the chart.

## Output

The chart displays:

- **X-axis:** Listing Exchange
- **Y-axis:** Number of securities
- **Bar sections:** ETFs and stocks
- **Stacked bars:** Total securities for each exchange

This visualization makes it easy to compare the number of ETFs and stocks across different exchanges.

## Loading the Data

Before running the visualization, make sure `df` has been created. For example:

```python
df = pd.read_csv('your_data.csv')
```

Make sure the CSV file contains the required columns:

```text
Listing Exchange
ETF
```

## Conclusion

This program provides a simple visual representation of ETF and stock distribution across listing exchanges using **Pandas** and **Matplotlib**.