import pandas as pd
import matplotlib.pyplot as plt
from arcgis.features import GeoAccessor, GeoSeriesAccessor

# Load the cleaned data
table_1 = pd.read_csv('cleaned_table_1.csv')
table_3 = pd.read_csv('cleaned_table_3.csv')
table_4 = pd.read_csv('cleaned_table_4.csv')
table_6 = pd.read_csv('cleaned_table_6.csv')
table_17 = pd.read_csv('cleaned_table_17.csv')
table_22 = pd.read_csv('cleaned_table_22.csv')
table_40 = pd.read_csv('cleaned_table_40.csv')
table_41 = pd.read_csv('cleaned_table_41.csv')

# Plot for Table 1
plt.figure(figsize=(10, 6))
plt.bar(table_1['Household_Type'], table_1['Mean'], yerr=[table_1['Mean'] - table_1['Lower_CI'], table_1['Upper_CI'] - table_1['Mean']], capsize=5)
plt.xlabel('Household Type')
plt.ylabel('Mean Satisfaction Score')
plt.title('Overall Satisfaction with State of Transport System in Wales by Household Type')
plt.xticks(rotation=45)
plt.show()

# Plot for Table 3
plt.figure(figsize=(8, 5))
plt.bar(table_3['Gender'], table_3['Mean'], yerr=[table_3['Mean'] - table_3['Lower_CI'], table_3['Upper_CI'] - table_3['Mean']], capsize=5)
plt.xlabel('Gender')
plt.ylabel('Mean Satisfaction Score')
plt.title('Overall Satisfaction with State of Transport System in Wales by Gender')
plt.show()

# Plot for Table 4
plt.figure(figsize=(8, 5))
plt.bar(table_4['Urban_Rural_Area'], table_4['Mean'], yerr=[table_4['Mean'] - table_4['Lower_CI'], table_4['Upper_CI'] - table_4['Mean']], capsize=5)
plt.xlabel('Urban/Rural Area')
plt.ylabel('Mean Satisfaction Score')
plt.title('Overall Satisfaction with State of Transport System in Wales by Urban/Rural Area')
plt.show()

# Convert table 4 into spatially enabled DataFrame
sdf = pd.DataFrame.spatial.from_xy(df=table_4, x_column='Longitude', y_column='Latitude')
#Choropleth Map
sdf.spatial.plot(map_type='choropleth', column='Mean', cmap='coolwarm', legend=True)
# Proportional Symbol Map
sdf.spatial.plot(map_type='proportional', column='Mean', symbol='circle', symbol_size='Mean')
#Heat Map
sdf.spatial.plot(map_type='heatmap', column='Mean', cmap='YlOrRd', legend=True)

