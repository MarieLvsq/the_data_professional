import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

titanic = pd.read_csv("1_titanic_modified_seaborn.csv")
titanic.info()
titanic.head()

titanic = titanic.drop(["name", "ticket", "cabin"], axis=1)

#How many men and women were in Titanic?
sns.catplot(x="sex", data=titanic, kind='count')

#How many men and women were in different classes?
sns.catplot(x="class", data=titanic, hue="sex", kind='count')

#What were the total numbers of passengers in different classes?
sns.catplot(x="class", data=titanic, kind='count')

#What were the total numbers of passengers dead or alive
sns.catplot(x="alive", data=titanic, kind='count')

#Where did the passengers embark from?
sns.catplot(x="class", data=titanic, hue="embark_town", kind="count")

#What classes had the survivors travelled in?
sns.catplot(hue="class", x="survived", data=titanic, kind='count')

#Which gender on which class survived most?
sns.catplot(x="survived", hue="sex", data=titanic, kind='count')

#Passenger from which port survived most?
sns.catplot(hue="survived", x="embark_town", data=titanic, kind='count')

#What is the age distribution of passengers?
sns.displot(titanic.age.dropna())

#What is the fare distribution of Titanic?
g = sns.FacetGrid(titanic, row='survived', col='class')
g.map(sns.histplot, "fare")
plt.show()

#Show correlation within different attributes of the dataset?
titanic_numeric = titanic.copy()
titanic_numeric = pd.get_dummies(titanic, drop_first=True)
sns.heatmap(titanic_numeric.corr(), annot=True, fmt=".2f", cmap='coolwarm')

plt.show()
