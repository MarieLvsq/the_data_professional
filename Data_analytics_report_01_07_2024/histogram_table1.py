import pandas as pd
import matplotlib.pyplot as plt

# Load a table
df = pd.read_csv('cleaned_table_1.csv')

# Summary statistics
print(df.describe())

# Histogram of satisfaction scores
df['Mean'].hist()
plt.xlabel('Mean Satisfaction Score')
plt.ylabel('Frequency')
plt.title('Distribution of Satisfaction Scores')
plt.show()
