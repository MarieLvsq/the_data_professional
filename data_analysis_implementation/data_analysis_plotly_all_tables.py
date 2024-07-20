import pandas as pd
import plotly.express as px

# Load the cleaned data
table_1 = pd.read_csv('cleaned_table_1.csv')
table_3 = pd.read_csv('cleaned_table_3.csv')
table_4 = pd.read_csv('cleaned_table_4.csv')
table_6 = pd.read_csv('cleaned_table_6.csv')
table_17 = pd.read_csv('cleaned_table_17.csv')
table_22 = pd.read_csv('cleaned_table_22.csv')
table_40 = pd.read_csv('cleaned_table_40.csv')
table_41 = pd.read_csv('cleaned_table_41.csv')


def plot_table(df, x_col, y_col, yerr_lower_col, yerr_upper_col, x_label, y_label, title):
    fig = px.bar(df, x=x_col, y=y_col, 
                 error_y=yerr_upper_col, 
                 error_y_minus=yerr_lower_col, 
                 labels={x_col: x_label, y_col: y_label},
                 title=title)
    fig.show()

# Plot each table
plot_table(table_1, 'Household_Type', 'Mean', 'Lower_CI', 'Upper_CI', 'Household Type', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Household Type')
plot_table(table_3, 'Gender', 'Mean', 'Lower_CI', 'Upper_CI', 'Gender', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Gender')
plot_table(table_4, 'Urban_Rural_Area', 'Mean', 'Lower_CI', 'Upper_CI', 'Urban/Rural Area', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Urban/Rural Area')
plot_table(table_6, 'Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI', 'Public Services Footprint', 'Mean Satisfaction Score', 'Overall Satisfaction with State of Transport System in Wales by Public Services Footprint')
