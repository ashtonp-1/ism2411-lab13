print('Self Reflection:')
#1. 

#2.

#3.

print('Exercise 1:')

import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print('Exercise 2:')

south = df[df['region'] == 'South']

print(len(south))
print(south.head())


print('Exercise 3:')

top_5 = df.nlargest(5, 'revenue')
print(top_5)

print('Exercise 4:')

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head(5))

print('Exercise 5:')

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(f'Mean Per Unit Revenue: {df["per_unit"].mean():.2f}')

print('Exercise 6:')

print(df['region'].unique())
print(df['region'].value_counts())

print('Exercise 7:')

rpr = df[['region', 'product', 'revenue']]
print(rpr.shape)

