import pandas as pd

# Load the Excel file
file_path = r'C:\Users\Marie LEVESQUE\OneDrive\Documents\ESSEX_Msc_DataScience\2_the_data_professional\unit_9_Data_Analytics_Report\Transport 1314.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load Table 6
df = excel_data.parse('Table 6', skiprows=5, nrows=7, usecols="B, C, E, G")
df.columns = ['Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI']

# Remove any additional NaN rows at the end of the dataframe
df = df.dropna()

# Convert columns to appropriate data types
df['Mean'] = pd.to_numeric(df['Mean'], errors='coerce')
df['Lower_CI'] = pd.to_numeric(df['Lower_CI'], errors='coerce')
df['Upper_CI'] = pd.to_numeric(df['Upper_CI'], errors='coerce')

# Display the cleaned DataFrame
print(df)

# Optionally, save the cleaned data to a new CSV file
df.to_csv('cleaned_table_6.csv', index=False)
