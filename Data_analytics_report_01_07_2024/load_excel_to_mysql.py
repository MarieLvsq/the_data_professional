import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file
file_path = r'C:\Users\Marie LEVESQUE\OneDrive\Documents\ESSEX_Msc_DataScience\2_the_data_professional\unit_9_Data_Analytics_Report\Transport 1314.xlsx'
excel_data = pd.ExcelFile(file_path)

# Replace 'your_username' and 'your_password' with your MySQL credentials
engine = create_engine('mysql+mysqlconnector://root:rrrrr@localhost:3306/transport_wales')

# Function to create unique truncated names
def create_truncated_name(name, existing_names, max_length=64):
    truncated_name = name[:max_length]
    # Ensure the truncated name is unique
    suffix = 1
    while truncated_name in existing_names:
        truncated_name = name[:max_length-len(str(suffix))-1] + '_' + str(suffix)
        suffix += 1
    existing_names.add(truncated_name)
    return truncated_name

# Set to keep track of existing names to ensure uniqueness
existing_table_names = set()
existing_column_names = set()

# Function to truncate column names
def truncate_column_names(columns, max_length=64):
    truncated_columns = []
    for col in columns:
        truncated_col = col[:max_length]
        # Ensure the truncated name is unique
        suffix = 1
        while truncated_col in existing_column_names:
            truncated_col = col[:max_length-len(str(suffix))-1] + '_' + str(suffix)
            suffix += 1
        existing_column_names.add(truncated_col)
        truncated_columns.append(truncated_col)
    return truncated_columns

# Loop through each sheet and load it into MySQL
for sheet_name in excel_data.sheet_names:
    if sheet_name not in ['Contents', 'Technical notes']:
        print(f"Processing sheet: {sheet_name}")
        df = excel_data.parse(sheet_name)
        # Clean and truncate the column names
        df.columns = df.columns.str.replace(' ', '_').str.replace(r'[^a-zA-Z0-9_]', '', regex=True)
        df.columns = truncate_column_names(df.columns, max_length=30)
        # Shorten table names
        truncated_sheet_name = create_truncated_name(sheet_name.replace(' ', '_').lower(), existing_table_names, max_length=30)
        print(f"Using table name: {truncated_sheet_name}")
        # Write the dataframe to MySQL
        df.to_sql(truncated_sheet_name, con=engine, if_exists='replace', index=False)