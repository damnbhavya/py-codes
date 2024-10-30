import pandas as pd
import matplotlib.pyplot as plt

df_people = pd.read_csv(r'files\people-1000.csv')

df_people['Date of birth'] = pd.to_datetime(df_people['Date of birth'])
df_people['Year of birth'] = df_people['Date of birth'].dt.year

# Create a figure with multiple subplots for line plots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Line plot: Number of People Born per Year
people_per_year = df_people['Year of birth'].value_counts().sort_index()
axs[0].plot(people_per_year.index, people_per_year.values, color='blue')
axs[0].set_title('Line Plot: Number of People Born per Year')
axs[0].set_xlabel('Year of Birth')
axs[0].set_ylabel('Number of People')

# Line plot: Number of People Born per Month (example additional line plot)
df_people['Month of birth'] = df_people['Date of birth'].dt.month
people_per_month = df_people['Month of birth'].value_counts().sort_index()
axs[1].plot(people_per_month.index, people_per_month.values, color='red')
axs[1].set_title('Line Plot: Number of People Born per Month')
axs[1].set_xlabel('Month of Birth')
axs[1].set_ylabel('Number of People')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df_people['Year of birth'], df_people.index, color='green', alpha=0.5)
plt.title('Scatter Plot: Year of Birth vs People')
plt.xlabel('Year of Birth')
plt.ylabel('Index')
plt.show()

plt.figure(figsize=(10, 6))
plt.boxplot(df_people['Year of birth'].dropna())
plt.title('Box Plot: Distribution of Years of Birth')
plt.ylabel('Year of Birth')
plt.show()

plt.figure(figsize=(10, 6))
job_counts = df_people['Job Title'].value_counts().head(10)
plt.barh(job_counts.index, job_counts.values, color='orange')
plt.title('Bar Plot: Top 10 Most Common Job Titles')
plt.xlabel('Number of People')
plt.gca().invert_yaxis()
plt.show()

gender_counts = df_people['Sex'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Pie Plot: Proportion of People by Gender')
plt.show()

cumulative_people_per_year = people_per_year.cumsum()
plt.figure(figsize=(10, 6))
plt.fill_between(cumulative_people_per_year.index, cumulative_people_per_year.values, color='purple', alpha=0.5)
plt.title('Area Plot: Cumulative Number of People Born Over Years')
plt.xlabel('Year of Birth')
plt.ylabel('Cumulative Number of People')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df_people['Year of birth'].dropna(), bins=20, color='blue', edgecolor='black')
plt.title('Histogram: Distribution of Year of Birth')
plt.xlabel('Year of Birth')
plt.ylabel('Frequency')
plt.show()