import pandas as pd
import plotly.express as px

# Load the Excel file
file_path = 'Transport_1314.xlsx'
excel_data = pd.ExcelFile(file_path)

# Function to clean and preprocess Table 3
def clean_table(sheet_name, skip_rows, n_rows, use_cols, col_names):
    df = excel_data.parse(sheet_name, skiprows=skip_rows, nrows=n_rows, usecols=use_cols)
    df.columns = col_names
    df.dropna(inplace=True)
    df[col_names[1:]] = df[col_names[1:]].apply(pd.to_numeric, errors='coerce')
    return df

# Preprocess Table 3
table_3 = clean_table('Table 3', skip_rows=3, n_rows=3, use_cols="B, C, E, G",
                        col_names=['Gender', 'Mean', 'Lower_CI', 'Upper_CI'])

table_4 = clean_table('Table 4', skip_rows=3, n_rows=3, use_cols="B, C, E, G", 
                      col_names=['Urban / rural area', 'Mean', 'Lower_CI', 'Upper_CI'])

# Preprocess Table 17
table_17 = clean_table('Table 17', skip_rows=4, n_rows=3, use_cols="B, C, E, G, I, K, M",
                          col_names=['Gender', 'Yes_%', 'Yes_Lower_CI', 'Yes_Upper_CI', 'No_%', 'No_Lower_CI', 'No_Upper_CI'])


# Save cleaned data
table_3.to_csv('cleaned_table_3.csv', index=False)
table_4.to_csv('cleaned_table_4.csv', index=False)
table_17.to_csv('cleaned_table_17.csv', index=False)

# Display the cleaned DataFrames
print("Cleaned Table 3:")
print(table_3)
print("\nCleaned Table 4:")
print(table_4)
print("\nCleaned Table 17:")
print(table_17)

# Calculate the error bars
table_3['error_plus'] = table_3['Upper_CI'] - table_3['Mean']
table_3['error_minus'] = table_3['Mean'] - table_3['Lower_CI']

table_4['error_plus'] = table_4['Upper_CI'] - table_4['Mean']
table_4['error_minus'] = table_4['Mean'] - table_4['Lower_CI']

# Visualization for Table 3 (Overall satisfaction with the state of the transport system in Wales, by gender)
fig_table_3 = px.bar(table_3, x='Gender', y='Mean', error_y='error_plus', error_y_minus='error_minus',
                     title='Overall Satisfaction with State of Transport System in Wales by Gender',
                     labels={'Gender': 'Gender', 'Mean': 'Mean Satisfaction Score'})
fig_table_3.show()

# Visualization for Table 4 (Overall satisfaction with the state of the transport system in Wales, by urban / rural area)
fig_table_4 = px.bar(table_4, x='Urban / rural area', y='Mean', error_y='error_plus', error_y_minus='error_minus',
                     title='Overall Satisfaction with State of Transport System in Wales by Urban / Rural Area',
                     labels={'Urban / rural area': 'Urban / Rural Area', 'Mean': 'Mean Satisfaction Score'})
fig_table_4.show()

# Visualization for Table 17 (Have use of a car, by gender)
table_17_long = table_17.melt(id_vars=['Gender'], value_vars=['Yes_%', 'No_%'],
                              var_name='Car_Use', value_name='Percentage')

fig_table_17 = px.bar(table_17_long, x='Gender', y='Percentage', color='Car_Use',
                      title='Have Use of a Car by Gender',
                      labels={'Percentage': 'Have Use of a Car (%)'})
fig_table_17.show()