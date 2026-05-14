"""#Day 10 | Project 1 (Gaana EDA)

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2--0CkvNYFjr-dQmoup0VpbpkHhlwuUGNYA&s" width=600 height=150>

## 1) Overall Data Exploration

### 1.1) Importing libary
"""

!pip install streamlit

import pandas as pd
import numpy as np

"""### 1.2) Loading Dataset"""

!git clone "https://github.com/HarshvardhanSingh-13/Datasets"

df = pd.read_csv('/content/Datasets/Gaana/songs.csv')   #(df is dataframe)

df

"""### 1.3) Basic Data Exploration"""

df.info()

df.describe()

"""###1.4) Checking for null values"""

df.isnull().sum()

"""### 1.5) Basic exploration based on singer and Language"""

df['singer']

df['singer'] == 'jagjit singh'

df[df['language'] == 'Urdu']

"""#### Q1) Find songs of singer name Lata Mangeshkar"""

df['singer'] == 'Lata Mangeshkar'

df[df['singer'] == 'Lata Mangeshkar']

"""#### Q2) FInd songs of singer Lata Mangeshkar which have language Hindi"""

df[(df['singer'] == 'Lata Mangeshkar') & (df['language']=='Hindi')]

df[df['singer'] == 'Jagjit Singh']

df[(df['language']=='Urdu') & (df['singer'] == 'Jagjit Singh')]





df['language'].unique()



df['language'].nunique() ##Or ##len(df['language'].unique())





df['singer'].unique()

df['singer'].nunique()

len(df['singer'].unique())

len(df[df['language'] == 'Urdu'])

df[df['language'] == 'Urdu'].nunique()



"""#### Q3) Find number of values where language is Telugu"""

len(df[df['language'] == 'Telugu'])



df[df['language'] == 'Telugu'].nunique()



df[df['language'] == 'Telugu']['name']
