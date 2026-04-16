"""#Day 11"""

df.info()

df.describe()

df.head(10)

df.tail(10)

df.isnull()

df.isnull().sum()

df['language'] == 'Urdu'

df['language'] == 'Urdu'

df[df['language'] == 'Urdu']

df[(df['language'] == 'Urdu') & (df['singer'] == 'Jagjit Singh')]

df['language'].unique()

for i in df ['language'].unique():
  print(i)

