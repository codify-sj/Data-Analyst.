"""#Day 11"""

df.info()

df.describe()

df.head(10)

df.tail(10)

df.isnull()

df.isnull().sum()

df['language'] == 'Urdu'

df[df['language'] == 'Urdu']

df[(df['language'] == 'Urdu') & (df['singer'] == 'Jagjit Singh')]

df['language'].unique()

"""###This is for unique Language:"""

for i in df ['language'].unique():
  print(i)

"""###Count in particular Language"""

len(df[df['language'] == 'Odia'])

"""###This is unique language with count:"""

for i in df ['language'].unique():
  print(i, len(df[df['language'] == i]))

"""###This is inbuild function for value counts."""

df['language'].value_counts()

df['language'].nunique() # or len(df['language'].unique())

"""##1.5) Checking Duplicate"""

df['link'].duplicated().sum()

df[df['link'].duplicated()]

df_ = df[df['link'].duplicated()]

df_

df_.info()

df_.describe()

len(df[df['language'] == 'Old'])

df['language'].unique()

[df['language'] == 'Old']

df_ = df[(df['language'] == 'Hindi') | (df['language'] == 'Old')]

df_ ['link'].duplicated().sum()

df.drop_duplicates(subset = 'link', inplace = True)
df

"""##2) Exploring every column

###2.1) Exploring Names
"""

df

df['name'].describe()

df['name'].value_counts()

df[df['name'] == 'V']

"""### 2.6) Exploring Languages"""

df['language'].value_counts()

df['language'].value_counts().sort_values(ascending=True).plot(kind='bar')

##KPI's

'''
1. Total Singers
2. Total Songs
3. Unique Languages
4. Total Songs Played
5. Plays in hours | 100 Million hours Played
6. Genre of Songs


-- Yearly Analystics

7. Top Songs of the year
8. Top Singer of the year
9. Yearly views of certain Artist

-- Monthly Analystics
7. Top Songs of the month
8. Top Singer of the month
9. Monthly views of certain artist

-- Daily Analystics
7. Top Songs of the Day
8. Top Singer of the Day
9. Daily views of certain artist

'''

"""## 3) Data Cleaning

### 3.1) Cleaning Duration
"""

df

df['duration'] [:10]

for i in df['duration'] [:10]:
  print(i)

for i in df['duration'] [:10]:
  print(i.split(':')[0])

