import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/Marko/Downloads/Python-Data-Science-and-Machine-Learning-Bootcamp/Data-Capstone-Projects/911.csv')
# print(df.head())

# SBB =  dpi-500 in game 13.68 Zoom: 38
# zip = df['zip'].head(5)
# print(zip)

# twp = df['twp'].head(5)
# print(twp)

# num = df['title'].nunique()
# print(num)

df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])
# print(df.head(3))

l = df['Reason'].value_counts().head(3)
print(df['Reason'].value_counts().head(5))

sns.countplot(x='Reason', data=df)
plt.show()