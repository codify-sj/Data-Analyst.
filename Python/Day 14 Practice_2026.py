"""#Day 14 | Project 2"""

!git clone "https://github.com/HarshvardhanSingh-13/Datasets"

"""##1) Overall Exploration

### 1.1) Loading the dataset
"""

df = pd.read_csv('/content/Datasets/Job Postings/jobs.csv.zip')
df.head()

'''
KPI's

1) Calculate the average rating for each company.
2) Identify companies with the highest and lowest average ratings.
3) Compare the distribution of ratings across different companies.
4) Calculate the total number of reviews for each company.
5) List the top 10 companies based on average rating and number of reviews.
6) Identify the top responsibilities for each role

7) Lowest and Highest Rating Companies
8) Number of Active Jobs in any company | Top Companies
8) Companies which provide Max/Min Average Salary
9) Salary Vs Expectation of any company
10) Companies hiring for most numbers of location

'''

"""### 1.2) Information about the dataset"""

df

df.info()

df.describe()

"""###1.3) Checking for null values"""

df.isnull().sum()

"""### 1.4) Removing Column 'posted_on'"""

df['posted_on'].unique()



del df['posted_on']
df

"""### 1.5) Removing Null Values"""

df.isnull().sum()

df.dropna(subset=['job_id']).isnull().sum()
