import pandas as pd


ecom = pd.read_csv('/Users/Marko/Downloads/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/Ecommerce Purchases.csv')

# print(ecom.head())

# print(ecom.info())

# l = ecom['Purchase Price'].mean()
# print(l)

# l = ecom['Purchase Price'].max()
# print(l)

# l = ecom['Purchase Price'].min()
# print(l)

# l = ecom['Language'].value_counts()['en']
# print(l)

# l = ecom['Job'].value_counts()['Lawyer']
# print(l)

# l = ecom['AM or PM'].value_counts()
# print(l)

# l = ecom['Job'].value_counts().head(5)
# print(l)

# l = ecom[ecom['Lot'] == '90 WT']['Purchase Price']
# print(l)

# l = ecom[ecom['Credit Card'] == 4926535242672853]['Email']
# print(l)

# l = len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)])
# print(l)

# def expire(date):
# 	a = date.split('/')
# 	if a[1] == '25':
# 		return True
# 	else:
# 		return False

# l = len(ecom[ecom['CC Exp Date'].apply(expire)])
# print(l)

def getEmailProvider(email):
	l = email.split('@')
	return l[1]

l = ecom['Email'].apply(getEmailProvider).value_counts().head(5)
print(l)








