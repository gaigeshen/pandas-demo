import pandas as pd

df = pd.DataFrame(data=[['Jack', 20], ['Rose', 21], ['Tom', 23]], columns=['User', 'Age'])

print('df'.center(40, '='))
print(df, end='\n\n')

df = pd.DataFrame(data={'User': ['Jack', 'Rose', 'Tom'], 'Age': [20, 21, 23]})

print('df'.center(40, '='))
print(df, end='\n\n')

df = pd.DataFrame(data=[{'User': 'Jack', 'Age': 20}, {'User': 'Rose', 'Age': 21}, {'User': 'Tom', 'Age': 23}])

print('df'.center(40, '='))
print(df, end='\n\n')

print('df.loc[0]'.center(40, '='))
print(df.loc[0], end='\n\n')

print('df.loc[[0, 1, 2]]'.center(40, '='))
print(df.loc[[0, 1, 2]], end='\n\n')

print('itertuples'.center(40, '='))
for row in df.itertuples(index=False):
    print(f'User: {row[0]}, Age: {row[1]}')
print()

print('df.apply'.center(40, '='))
df.apply(lambda r: print(r.values), axis='columns')