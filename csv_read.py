import pandas as pd

df = pd.read_csv('users.csv')

print('df'.center(40, '='))
print(df, end='\n\n')

print('df.head(1)'.center(40, '='))
print(df.head(1), end='\n\n')

print('df.tail(1)'.center(40, '='))
print(df.tail(1))
