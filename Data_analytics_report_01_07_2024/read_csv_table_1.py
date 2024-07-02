import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_table_1.csv')

# Calculate mean satisfaction scores (already provided in the dataset)
mean_scores = df[['Household_Type', 'Mean', 'Lower_CI', 'Upper_CI']]

# Print the mean satisfaction scores with confidence intervals
print(mean_scores)

# Visualize the mean satisfaction scores with error bars
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(df['Household_Type'], df['Mean'], yerr=[df['Mean'] - df['Lower_CI'], df['Upper_CI'] - df['Mean']], capsize=5)
plt.xlabel('Household Type')
plt.ylabel('Mean Satisfaction Score')
plt.title('Overall Satisfaction with State of Transport System in Wales by Household Type')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()