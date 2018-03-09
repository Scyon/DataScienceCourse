import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# tips = sns.load_dataset('tips')
# # sns.distplot(tips['total_bill'])
# # plt.show()
# plt.style.use('ggplot')
# # tips.plot(kind='hexbin', x='tip', y='total_bill', style='coolwarm', alpha=0.5, cmap='coolwarm')
# tips.plot(kind='area', x='tip', y='total_bill')

# plt.show()
# print(tips)

# ecom = pd.read_csv('/Users/Marko/Downloads/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/Ecommerce Purchases.csv')
# print(ecom)
# plt.style.use('ggplot')
# ecom.plot.scatter(x='Purchase Price', y='CC Security Code', alpha=0.5)
# plt.show()

# ecom = pd.read_csv('/Users/Marko/Downloads/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/Ecommerce Purchases.csv')
# sns.lmplot(x='Purchase Price', y='CC Security Code', data=ecom)
# plt.show()

ecom = pd.read_csv('/Users/Marko/Downloads/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/Ecommerce Purchases.csv')
sns.violinplot(x='Job', y='CC Security Code', hue='Company', data=ecom.iloc[0:5])
plt.show()