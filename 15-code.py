import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'files\organizations-1000.csv')

df_sorted = df.sort_values(by='Founded')
plt.figure(figsize=(10, 6))
plt.plot(df_sorted['Founded'], df_sorted['Number of employees'], color='blue')
plt.title('Line Plot: Employees vs Founded Year')
plt.xlabel('Founded Year')
plt.ylabel('Number of Employees')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Founded'], df['Number of employees'], color='green')
plt.title('Scatter Plot: Employees vs Founded Year')
plt.xlabel('Founded Year')
plt.ylabel('Number of Employees')
plt.show()

plt.figure(figsize=(10, 6))
plt.boxplot(df['Number of employees'].dropna())
plt.title('Box Plot: Distribution of Employees')
plt.ylabel('Number of Employees')
plt.show()

plt.figure(figsize=(10, 6))
avg = df.groupby('Industry')['Number of employees'].mean().sort_values(ascending=False).head(10)
plt.barh(avg.index, avg.values, color='orange')
plt.title('Bar Plot: Top 10 Industries by Avg Employees')
plt.xlabel('Average Number of Employees')
plt.gca().invert_yaxis()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['Decade'] = (df['Founded'] // 10) * 10
decade_counts = df['Decade'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(decade_counts, labels=decade_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Pie Plot: Organizations Founded by Decade')
plt.show()

plt.figure(figsize=(10, 6))
cumulative_sum = df_sorted.groupby('Founded')['Number of employees'].sum().cumsum()
plt.fill_between(cumulative_sum.index, cumulative_sum.values, color='purple', alpha=0.5)
plt.title('Area Plot: Cumulative Employees by Year')
plt.xlabel('Founded Year')
plt.ylabel('Cumulative Number of Employees')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['Number of employees'].dropna(), bins=20, color='blue', edgecolor='black')
plt.title('Histogram: Distribution of Number of Employees')
plt.xlabel('Number of Employees')
plt.ylabel('Frequency')
plt.show()
