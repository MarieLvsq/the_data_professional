import pandas as pd
import plotly.express as px

# Load the Excel file
file_path = 'Transport_1314.xlsx'
excel_data = pd.ExcelFile(file_path)

# Function to clean and preprocess each table
def clean_table(sheet_name, skip_rows, n_rows, use_cols, col_names):
    df = excel_data.parse(sheet_name, skiprows=skip_rows, nrows=n_rows, usecols=use_cols)
    df.columns = col_names
    df.dropna(inplace=True)
    df[col_names[1:]] = df[col_names[1:]].apply(pd.to_numeric, errors='coerce')
    return df

# Preprocess Table 40
table_40 = clean_table('Table 40', skip_rows=5, n_rows=6, use_cols="B, C, E, G, I",
                      col_names=['Age_Group', 'Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe'])

# Preprocess Table 41
table_41 = clean_table('Table 41', skip_rows=5, n_rows=2, use_cols="B, C, E, G, I, K",
                       col_names=['Gender', 'Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe', 'Total'])

# Save cleaned data
table_40.to_csv('cleaned_table_40.csv', index=False)
table_41.to_csv('cleaned_table_41.csv', index=False)

# Display the cleaned DataFrame
print("Cleaned Table 4:")
print(table_40)
print("\nCleaned Table 41:")
print(table_41)

# Melt the data for Table 40 to long format for better visualisation
table_40_long = table_40.melt(id_vars=['Age_Group'], value_vars=['Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe'],
                              var_name='Feeling_of_Safety', value_name='Percentage')

# Visualization for Table 40
fig_table_40 = px.bar(table_40_long, x='Age_Group', y='Percentage', color='Feeling_of_Safety',
                      title='Feeling of Safety Travelling by Public Transport After Dark by Age',
                      labels={'Percentage': 'Feeling of Safety (%)'})
fig_table_40.show()

# Melt the data for Table 41 to long format for better visualisation
table_41_long = table_41.melt(id_vars=['Gender'], value_vars=['Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe'],
                              var_name='Feeling_of_Safety', value_name='Percentage')

# Visualization for Table 41
fig_table_41 = px.bar(table_41_long, x='Gender', y='Percentage', color='Feeling_of_Safety',
                      title='Feeling of Safety Travelling by Public Transport After Dark by Gender',
                      labels={'Percentage': 'Feeling of Safety (%)'})
fig_table_41.show()
