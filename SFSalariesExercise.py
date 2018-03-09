import pandas as pd


df = pd.read_csv('/Users/Marko/Desktop/Salaries.csv')

# print(df.head())

# print(df.info())

# mean = df['BasePay'].mean()
# print(mean)

# print(df['OvertimePay'].max())

# d = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']
# print(d['JobTitle'])

# p = d['TotalPayBenefits']
# print(p)

# l = df['TotalPayBenefits'].max()
# d = df[df['TotalPayBenefits'] == l]
# print(d['EmployeeName'])

# q = df.iloc[df['TotalPayBenefits'].idxmax()]
# print(q)

# l = df['TotalPayBenefits'].min()
# d = df[df['TotalPayBenefits'] == l]
# print(d['EmployeeName'])

# m = df.groupby('Year').mean()['BasePay']
# print(m)

# l = df['JobTitle'].value_counts().head(5)
# print(l)

# print(df['JobTitle'].nunique())

# l = sum(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1)
# print(l)

def cheifString(title):
	if 'chief' in title.lower().split():
		return True
	else:
		return False

l = sum(df['JobTitle'].apply(cheifString))
print(l)
