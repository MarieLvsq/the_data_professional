import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned data
table_1 = pd.read_csv('cleaned_table_1.csv')
table_3 = pd.read_csv('cleaned_table_3.csv')
table_4 = pd.read_csv('cleaned_table_4.csv')
table_6 = pd.read_csv('cleaned_table_6.csv')
table_17 = pd.read_csv('cleaned_table_17.csv')
table_22 = pd.read_csv('cleaned_table_22.csv')
table_40 = pd.read_csv('cleaned_table_40.csv')
table_41 = pd.read_csv('cleaned_table_41.csv')

# Visualisation functions
def plot_bar_chart_seaborn(df, x_col, y_col, yerr_lower_col, yerr_upper_col, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_col, y=y_col, data=df, ci=None)
    plt.errorbar(x=df[x_col], y=df[y_col], yerr=[df[y_col] - df[yerr_lower_col], df[yerr_upper_col] - df[y_col]], fmt='none', c='black', capsize=5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

# Plotting each table
plot_bar_chart_seaborn(table_1, 'Household_Type', 'Mean', 'Lower_CI', 'Upper_CI', 'Household Type', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Household Type')
plot_bar_chart_seaborn(table_3, 'Gender', 'Mean', 'Lower_CI', 'Upper_CI', 'Gender', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Gender')
plot_bar_chart_seaborn(table_4, 'Urban_Rural_Area', 'Mean', 'Lower_CI', 'Upper_CI', 'Urban/Rural Area', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Urban/Rural Area')
plot_bar_chart_seaborn(table_6, 'Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI', 'Public Services Footprint', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Public Services Footprint')
plot_bar_chart_seaborn(table_17, 'Gender', 'Mean', 'Lower_CI', 'Upper_CI', 'Gender', 'Have Use of a Car (%)', 'Have Use of a Car by Gender')
plot_bar_chart_seaborn(table_22, 'Limiting_Long_Term_Illness', 'Mean', 'Lower_CI', 'Upper_CI', 'Limiting Long Term Illness', 'Have Use of a Car (%)', 'Have Use of a Car by Limiting Long Term Illness')
plot_bar_chart_seaborn(table_40, 'Age_Group', 'Mean', 'Lower_CI', 'Upper_CI', 'Age Group', 'Feeling of Safety (%)', 'Feeling of Safety Travelling by Public Transport After Dark by Age')
plot_bar_chart_seaborn(table_41, 'Gender', 'Mean', 'Lower_CI', 'Upper_CI', 'Gender', 'Feeling of Safety (%)', 'Feeling of Safety Travelling by Public Transport After Dark by Gender')
