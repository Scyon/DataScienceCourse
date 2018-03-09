import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

labels = ['a', 'b', 'c']
array = list(range(10, 40, 10))
# print(array)

series = pd.Series(data=array, index=labels)
print(series)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

df['new'] = df['X'] + df['Y']
print(df)

df.drop('A', inplace=True)
print(df)

df.drop('W', axis=1, inplace=True)
print(df)

print('-'*40)
rdf = df[df['Y']>0]
print(rdf)

# rdf.reset_index(inplace=True)
# print(rdf)
# rdf.index.name = 'test'
# print(rdf)