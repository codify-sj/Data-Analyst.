"""#Day 15 | Project 2 (Company Insights EDA)"""

df

"""###1.6) Removing Duplicate"""

df['job_id'].info()

df['job_id'].astype('str')

len(df.drop_duplicates(subset='job_id'))

len(df)

len(df.drop_duplicates(subset='job_link'))

df.drop_duplicates(subset='job_id', inplace = True)

len(df)

"""## 2) Column wise Data Cleaning"""

df.head(3)

"""###2.1) job_id Exploration"""

df['job_id'].value_counts()

df['job_id'].nunique()

"""###2.2) job_role Exploration"""

df['job_role'].value_counts()

df['job_role'].unique()

df['job_role'].head(20)

"""###2.2) Company Exploration"""

df['company'].value_counts()

df[df['company'] == 'Lavya Associates']

df[df['company'] == 'Lavya Associates']['job_link'].values

df[df['company'] == 'Lavya Associates']['company_link'].values

df[df['company'] == 'Lavya Associates']['company_link'].unique()

df['company_link'].value_counts()

df[df['company'] == 'Accenture']['company_link'].unique() #exploring companies if there are any multiple links for a particular link.

df[df['company'] == 'Hucon']['company_link'].unique() #exploring companies if there are any multiple links for a particular link.

"""###2.3) Company_links Exploration"""

df['company_link'].value_counts()

df[df['company_link'] == 'https://www.naukri.com/lavya-associates-hr-services-jobs-careers-932996' ]['company'].unique() ## we will contact from where the data is extracted , why we are getting inconsistancy as Lavya Associates? as its is giving two links. how to deal with this problem  or contact the manager.

"""#### 2.4) Experience Exploration"""

df['experience']

df['experience'].unique() # check if there is any null or nan value instead of range of experience

for i in df['experience'][:10]:
#  print(i.split())
 if len(i.split()) == 2:
  print(i)

c = 0
for i in df['experience']:
 if len(i.split()) == 2:
  c += 1
print(c)

len(df['experience'])

df['start_exp'] = df['experience'].str.replace('Yrs','').str.strip().str.split('-').str[0]

df['end_exp'] = df['experience'].str.replace('Yrs','').str.strip().str.split('-').str[1]

df

df['salary'].unique()

df.head(2)

