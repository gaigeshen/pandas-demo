import pandas as pd

df = pd.DataFrame(data=[['Jack', 20], ['Rose', 21], ['Tom', 23]], columns=['User', 'Age'])

df.to_csv('users.csv', index=False)
