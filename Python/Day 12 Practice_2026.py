"""#Day 12 Project 1 (Gaana EDA)"""

for i in df['duration'][:10]:
  print(i, int(i.split(':')[0])*60 + int(i.split(':')[1]))

duration = [] #empty_list
for i in df['duration']:
  mins = int(i.split(':')[0])
  secs = int(i.split(':')[1])
  duration.append( mins*60 + secs)
#duration
df['duration_in_sec'] = duration
df

df['duration_in_sec']

df['duration_in_sec'].sort_values(ascending=False)

3595/60 #what if there is some songs above 1 hours. we have to check

duration = []
for i in df['duration']:
  if len(i.split(":")) == 3:
   print(i)

df[df['duration'] == '01:00:21']

duration = []

for i in df['duration']:
  if len(i.split(":")) == 3:
    print(i,i.split(':')[0])

duration = [] #empty_list
for i in df['duration']:
  if len(i.split(":")) == 2:
   min = int(i.split(':')[0])
   secs = int(i.split(':')[1])
   duration.append( min*60 + secs)
  elif len(i.split(":")) == 3:
   hours = int(i.split(':')[0])
   mins  = int(i.split(':')[1])
   secs = int(i.split(':')[2])
   duration.append(hours*60*60 + mins*60 + secs)

#duration
df['duration_in_sec'] = duration
df

df['duration_in_sec'].sort_values(ascending=False)

df.sort_values(by = 'duration_in_sec' , ascending= False).head(5)

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

df

"""##4) Data Anaytics

##4.1)Total number of unique Songs
"""

df['name'].nunique()

df['link'].nunique()

"""## 4.2)  Total number of unique Singers"""

df['singer'].nunique()

df['singer_id'].nunique()

df['singer_id']

len(df[df['singer_id'] == '/artist/chitra-singh'])

# df['singer_id'].str.split('|').explode() or # df['singer'].str.split('|').explode()

#(with explode function)

df['singer_id'].str.split('|').explode().nunique()

df['singer'].str.split('|').explode().nunique()

#with normal function (without explode function)

['/artist/chitra-singh','/artist/jagjeet-singh-1'] + ['/artist/chitra-singh','/artist/jagjeet-singh-1']



lst = []

for i in df['singer_id']:
  lst = lst + i.split('|')
  #print(lst)
print(len(set(lst)))

#lst

"""##4.3) Find total Unique Languages"""

df['language'].nunique()

"""##4.4) Accumulative duration of songs listed on Ganna"""

df['duration_in_sec'].sum()

df['duration_in_sec'].sum() // 3600

hours = df['duration_in_sec'].sum() // 3600
hours

mins = (df['duration_in_sec'].sum() % 3600) // 60

mins

sec = (df['duration_in_sec'].sum() % 3600) % 60
sec

3160*3600 + 21*60 + 7
