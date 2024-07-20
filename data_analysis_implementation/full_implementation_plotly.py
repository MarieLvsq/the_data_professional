import pandas as pd
import plotly.express as px

# Load the Excel file
file_path = 'Transport_1314.xlsx'
excel_data = pd.ExcelFile(file_path)

# Function to clean and preprocess each table
def clean_table(sheet_name, skip_rows, use_cols, col_names, drop_total=True):
    df = excel_data.parse(sheet_name, skiprows=skip_rows, usecols=use_cols)
    df.columns = col_names
    df.dropna(inplace=True)
    df[col_names[1:]] = df[col_names[1:]].apply(pd.to_numeric, errors='coerce')
    if drop_total:
        df = df[df[col_names[0]] != 'Total']
    return df

# Preprocess each relevant table
table_1 = clean_table('Table 1', skip_rows=5, use_cols="B, C, E, G",
                      col_names=['Household_Type', 'Mean', 'Lower_CI', 'Upper_CI'])

table_3 = clean_table('Table 3', skip_rows=5, use_cols="B, C, E, G",
                      col_names=['Gender', 'Mean', 'Lower_CI', 'Upper_CI'])

table_4 = clean_table('Table 4', skip_rows=5, use_cols="B, C, E, G",
                      col_names=['Urban_Rural_Area', 'Mean', 'Lower_CI', 'Upper_CI'])

table_6 = clean_table('Table 6', skip_rows=5, use_cols="B, C, E, G",
                      col_names=['Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI'])

table_17 = clean_table('Table 17', skip_rows=5, use_cols="B, C, E, G",
                       col_names=['Gender', 'Yes_Percentage', 'Yes_Lower_CI', 'Yes_Upper_CI'], drop_total=False)

table_22 = clean_table('Table 22', skip_rows=5, use_cols="B, C, E, G",
                       col_names=['Limiting_Long_Term_Illness', 'Yes_Percentage', 'Yes_Lower_CI', 'Yes_Upper_CI'], drop_total=False)

table_40 = clean_table('Table 40', skip_rows=5, use_cols="B, C, E, G, I, K, M, O",
                       col_names=['Age_Group', 'Very_Safe', 'Very_Safe_Lower_CI', 'Very_Safe_Upper_CI', 
                                  'Fairly_Safe', 'Fairly_Safe_Lower_CI', 'Fairly_Safe_Upper_CI', 
                                  'Fairly_Unsafe', 'Fairly_Unsafe_Lower_CI', 'Fairly_Unsafe_Upper_CI'], drop_total=False)

table_41 = clean_table('Table 41', skip_rows=5, use_cols="B, C, E, G, I, K, M, O",
                       col_names=['Gender', 'Very_Safe', 'Very_Safe_Lower_CI', 'Very_Safe_Upper_CI', 
                                  'Fairly_Safe', 'Fairly_Safe_Lower_CI', 'Fairly_Safe_Upper_CI', 
                                  'Fairly_Unsafe', 'Fairly_Unsafe_Lower_CI', 'Fairly_Unsafe_Upper_CI'], drop_total=False)

# Save cleaned data
table_1.to_csv('cleaned_table_1.csv', index=False)
table_3.to_csv('cleaned_table_3.csv', index=False)
table_4.to_csv('cleaned_table_4.csv', index=False)
table_6.to_csv('cleaned_table_6.csv', index=False)
table_17.to_csv('cleaned_table_17.csv', index=False)
table_22.to_csv('cleaned_table_22.csv', index=False)
table_40.to_csv('cleaned_table_40.csv', index=False)
table_41.to_csv('cleaned_table_41.csv', index=False)

# Function to plot with Plotly
def plot_bar_chart(df, x_col, y_col, lower_ci_col, upper_ci_col, xlabel, ylabel, title):
    df['Error'] = df[upper_ci_col] - df[y_col]
    fig = px.bar(df, x=x_col, y=y_col, error_y='Error', labels={x_col: xlabel, y_col: ylabel}, title=title)
    fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel, title=title)
    fig.show()

# Plotting tables with adjusted columns
plot_bar_chart(table_1, 'Household_Type', 'Mean', 'Lower_CI', 'Upper_CI', 'Household Type', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Household Type')
plot_bar_chart(table_3, 'Gender', 'Mean', 'Lower_CI', 'Upper_CI', 'Gender', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Gender')
plot_bar_chart(table_4, 'Urban_Rural_Area', 'Mean', 'Lower_CI', 'Upper_CI', 'Urban/Rural Area', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Urban/Rural Area')
plot_bar_chart(table_6, 'Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI', 'Public Services Footprint', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Public Services Footprint')

# Plotting special tables with percentages
def plot_percentage_bar_chart(df, x_col, y_col, lower_ci_col, upper_ci_col, xlabel, ylabel, title):
    df['Error'] = df[upper_ci_col] - df[y_col]
    fig = px.bar(df, x=x_col, y=y_col, error_y='Error', labels={x_col: xlabel, y_col: ylabel}, title=title)
    fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel, title=title)
    fig.show()

plot_percentage_bar_chart(table_17, 'Gender', 'Yes_Percentage', 'Lower_CI', 'Upper_CI', 'Gender', 'Have Use of a Car (%)', 'Have Use of a Car by Gender')
plot_percentage_bar_chart(table_22, 'Limiting_Long_Term_Illness', 'Yes_Percentage', 'Lower_CI', 'Upper_CI', 'Limiting Long Term Illness', 'Have Use of a Car (%)', 'Have Use of a Car by Limiting Long Term Illness')

# Plotting safety perception tables
def plot_safety_perception_chart(df, x_col, very_safe_col, fairly_safe_col, fairly_unsafe_col, very_unsafe_col, xlabel, ylabel, title):
    fig = px.bar(df, x=x_col, y=[very_safe_col, fairly_safe_col, fairly_unsafe_col, very_unsafe_col],
                 labels={x_col: xlabel, 'value': ylabel}, title=title,
                 barmode='group')
    fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel, title=title)
    fig.show()

plot_safety_perception_chart(table_40, 'Age_Group', 'Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe', 'Age Group', 'Feeling of Safety (%)', 'Feeling of Safety Travelling by Public Transport After Dark by Age')
plot_safety_perception_chart(table_41, 'Gender', 'Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe', 'Gender', 'Feeling of Safety (%)', 'Feeling of Safety Travelling by Public Transport After Dark by Gender')
