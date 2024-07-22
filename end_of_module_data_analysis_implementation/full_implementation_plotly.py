import pandas as pd
import plotly.express as px

# Load the Excel file
file_path = 'Transport_1314.xlsx'
excel_data = pd.ExcelFile(file_path)

# General function to clean and preprocess tables
def clean_table(sheet_name, skip_rows, use_cols, col_names, drop_total=False, n_rows=None):
    df = excel_data.parse(sheet_name, skiprows=skip_rows, usecols=use_cols, nrows=n_rows)
    df.columns = col_names
    df.dropna(inplace=True)
    df[col_names[1:]] = df[col_names[1:]].apply(pd.to_numeric, errors='coerce')
    if drop_total:
        df = df[df[col_names[0]] != 'Total']
    return df

# Preprocess each relevant table
table_1 = clean_table('Table 1', skip_rows=5, use_cols="B, C, E, G",
                      col_names=['Household_Type', 'Mean', 'Lower_CI', 'Upper_CI'], drop_total=True)

table_6 = clean_table('Table 6', skip_rows=5, use_cols="B, C, E, G",
                      col_names=['Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI'], drop_total=True)

table_3 = clean_table('Table 3', skip_rows=3, use_cols="B, C, E, G", n_rows=3,
                      col_names=['Gender', 'Mean', 'Lower_CI', 'Upper_CI'])

table_4 = clean_table('Table 4', skip_rows=3, use_cols="B, C, E, G", n_rows=3,
                      col_names=['Urban / rural area', 'Mean', 'Lower_CI', 'Upper_CI'])

table_17 = clean_table('Table 17', skip_rows=4, use_cols="B, C, E, G, I, K, M", n_rows=3,
                       col_names=['Gender', 'Yes_%', 'Yes_Lower_CI', 'Yes_Upper_CI', 'No_%', 'No_Lower_CI', 'No_Upper_CI'])

table_22 = clean_table('Table 22', skip_rows=3, use_cols="B, C, E, G, I, K, M", n_rows=3,
                       col_names=['Limiting long-term illness', 'Yes_%', 'Yes_Lower_CI', 'Yes_Upper_CI', 'No_%', 'No_Lower_CI', 'No_Upper_CI'])

table_40 = clean_table('Table 40', skip_rows=4, use_cols="B, C, E, G, I", n_rows=6,
                       col_names=['Age_Group', 'Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe'])

table_41 = clean_table('Table 41', skip_rows=4, use_cols="B, C, E, G, I, K", n_rows=3,
                       col_names=['Gender', 'Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe', 'Total'])

# Save cleaned data
table_1.to_csv('cleaned_table_1.csv', index=False)
table_6.to_csv('cleaned_table_6.csv', index=False)
table_3.to_csv('cleaned_table_3.csv', index=False)
table_4.to_csv('cleaned_table_4.csv', index=False)
table_17.to_csv('cleaned_table_17.csv', index=False)
table_22.to_csv('cleaned_table_22.csv', index=False)
table_40.to_csv('cleaned_table_40.csv', index=False)
table_41.to_csv('cleaned_table_41.csv', index=False)

# Visualisation function
def plot_bar_chart(df, x_col, y_col, lower_ci_col, upper_ci_col, xlabel, ylabel, title):
    df['Error'] = df[upper_ci_col] - df[y_col]
    fig = px.bar(df, x=x_col, y=y_col, error_y='Error', labels={x_col: xlabel, y_col: ylabel}, title=title)
    fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel, title=title)
    fig.show()

# Visualise tables 1 and 6
plot_bar_chart(table_1, 'Household_Type', 'Mean', 'Lower_CI', 'Upper_CI', 'Household Type', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Household Type')
plot_bar_chart(table_6, 'Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI', 'Public Services Footprint', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Public Services Footprint')

# Visualize tables 3, 4, and 17
table_3['error_plus'] = table_3['Upper_CI'] - table_3['Mean']
table_3['error_minus'] = table_3['Mean'] - table_3['Lower_CI']

table_4['error_plus'] = table_4['Upper_CI'] - table_4['Mean']
table_4['error_minus'] = table_4['Mean'] - table_4['Lower_CI']

fig_table_3 = px.bar(table_3, x='Gender', y='Mean', error_y='error_plus', error_y_minus='error_minus',
                     title='Overall Satisfaction with State of Transport System in Wales by Gender',
                     labels={'Gender': 'Gender', 'Mean': 'Mean Satisfaction Score'})
fig_table_3.show()

fig_table_4 = px.bar(table_4, x='Urban / rural area', y='Mean', error_y='error_plus', error_y_minus='error_minus',
                     title='Overall Satisfaction with State of Transport System in Wales by Urban / Rural Area',
                     labels={'Urban / rural area': 'Urban / Rural Area', 'Mean': 'Mean Satisfaction Score'})
fig_table_4.show()

table_17_long = table_17.melt(id_vars=['Gender'], value_vars=['Yes_%', 'No_%'],
                              var_name='Car_Use', value_name='Percentage')

fig_table_17 = px.bar(table_17_long, x='Gender', y='Percentage', color='Car_Use',
                      title='Have Use of a Car by Gender',
                      labels={'Percentage': 'Have Use of a Car (%)'})
fig_table_17.show()

# Visualise tables 22, 40, and 41
table_22_long = table_22.melt(id_vars=['Limiting long-term illness'], value_vars=['Yes_%', 'No_%'],
                              var_name='Car_Use', value_name='Percentage')

fig_table_22 = px.bar(table_22_long, x='Limiting long-term illness', y='Percentage', color='Car_Use',
                      title='Have Use of a Car by Limiting Long-Term Illness',
                      labels={'Percentage': 'Have Use of a Car (%)'})
fig_table_22.show()

table_40_long = table_40.melt(id_vars=['Age_Group'], value_vars=['Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe'],
                              var_name='Feeling_of_Safety', value_name='Percentage')

fig_table_40 = px.bar(table_40_long, x='Age_Group', y='Percentage', color='Feeling_of_Safety',
                      title='Feeling of Safety Travelling by Public Transport After Dark by Age',
                      labels={'Percentage': 'Feeling of Safety (%)'})
fig_table_40.show()

table_41_long = table_41.melt(id_vars=['Gender'], value_vars=['Very_Safe', 'Fairly_Safe', 'Fairly_Unsafe', 'Very_Unsafe'],
                              var_name='Feeling_of_Safety', value_name='Percentage')

fig_table_41 = px.bar(table_41_long, x='Gender', y='Percentage', color='Feeling_of_Safety',
                      title='Feeling of Safety Travelling by Public Transport After Dark by Gender',
                      labels={'Percentage': 'Feeling of Safety (%)'})
fig_table_41.show()
