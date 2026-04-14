"""#Day 10"""

!pip install streamlit

!git clone "https://github.com/HarshvardhanSingh-13/Datasets"

"""#Data Exploration

## 1.1)Importing libary
"""

import pandas as pd

"""## 1.2)Loading libary"""

df = pd.read_csv('/content/Datasets/Gaana/songs.csv')   #(df is dataframe)

df

df.info()

df.describe()

df.isnull().sum()

df['singer']

df['singer'] == 'jagjit singh'

df[df['language'] == 'Urdu']

"""## Q1) Find songs of singer name Lata Mangeshkar

## Q2) FInd songs of singer Lata Mangeshkar which have language Hindi
"""



df['singer'] == 'Lata Mangeshkar'

df[(df['singer'] == 'Lata Mangeshkar') & (df['language']=='Hindi')]

df[df['singer'] == 'Jagjit Singh']

df[(df['singer'] == 'Jagjit Singh') & (df['language']=='Urdu')]





df['language'].unique()

df['language'].nunique()

len(df['language'].unique())

df['singer'].unique()

df['singer'].nunique()

len(df['singer'].unique())

len(df[df['language'] == 'Urdu'])

df[df['language'] == 'Urdu'].nunique()



"""## Q. Find number of values where language is Telugu"""

len(df[df['language'] == 'Telugu'])



df[df['language'] == 'Telugu'].nunique()



df[df['language'] == 'Telugu']['name']

