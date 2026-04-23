"""#Day 13"""

#Q: Calculate 7638553 sec in hrs,min,sec.

7638553 // 3600

7638553 % 3600

2953 //60

2953 % 60

#2121 Minutes  49 Minutes  13 Sec

# checking result
2121*60*60 + 49*60 + 13

"""### 4.5) Top 10 songs"""

df

df['name'].value_counts().sort_values(ascending=False).head(10)

df[df['name'] == 'V']

"""### 4.6) Top 5 languages"""

df['language'].value_counts().sort_values(ascending=False).head(5)

df.groupby('language')['language'].count().sort_values(ascending=False).head(5)

"""###4.7) Top 10 singers with most number of solo"""

df['singer_id'].value_counts().sort_values(ascending=False).head(10)

lst = []
for i in df ['singer_id']:
  lst.append(len(i.split('|')))

df['no of singers'] = lst
df.head(5)

df['no of singers'].value_counts().sort_values(ascending=False)

df[df['no of singers'] == 25]



df[df['no of singers'] == 1]['singer_id'].value_counts().sort_values(ascending=False).head(10)

"""### 4.8) Top 10 singers with most number of songs in total"""

singers = df['singer_id'].str.split('|').explode()

singers.value_counts().sort_values(ascending=False).head(10).to_csv('Top_10_singers_with_most_number_of_songs_in_total.csv')

singers.value_counts().sort_values(ascending=False).head(10)

df['singer_id'].str.replace('/artist/','').str.replace('|',',').str.strip()

df

