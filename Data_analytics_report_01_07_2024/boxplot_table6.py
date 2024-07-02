import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data from the CSV file
cleaned_file_path = 'cleaned_table_6.csv'
df = pd.read_csv(cleaned_file_path)

# Create the boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(
    [df[df['Public_Services_Footprint'] == region]['Mean'] for region in df['Public_Services_Footprint'].unique()],
    labels=df['Public_Services_Footprint'].unique()
)
plt.xlabel('Public Services Footprint')
plt.ylabel('Mean Satisfaction Score')
plt.title('Overall Satisfaction with State of Transport System in Wales by Public Services Footprint')
plt.xticks(rotation=45)
plt.show()

