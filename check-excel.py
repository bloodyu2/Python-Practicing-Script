import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('data.xlsx')

# Check if there are any duplicate rows in the DataFrame
if df.duplicated().any():
  print("There are duplicate rows in the data.")
else:
  print("There are no duplicate rows in the data.")
