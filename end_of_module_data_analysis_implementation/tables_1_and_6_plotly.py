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

table_6 = clean_table('Table 6', skip_rows=5, use_cols="B, C, E, G",
                      col_names=['Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI'])

# Save cleaned data
table_1.to_csv('cleaned_table_1.csv', index=False)
table_6.to_csv('cleaned_table_6.csv', index=False)

# Function to plot with Plotly
def plot_bar_chart(df, x_col, y_col, lower_ci_col, upper_ci_col, xlabel, ylabel, title):
    df['Error'] = df[upper_ci_col] - df[y_col]
    fig = px.bar(df, x=x_col, y=y_col, error_y='Error', labels={x_col: xlabel, y_col: ylabel}, title=title)
    fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel, title=title)
    fig.show()

# Plotting tables with adjusted columns
plot_bar_chart(table_1, 'Household_Type', 'Mean', 'Lower_CI', 'Upper_CI', 'Household Type', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Household Type')
plot_bar_chart(table_6, 'Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI', 'Public Services Footprint', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Public Services Footprint')
