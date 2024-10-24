import pandas as pd
import numpy as np
lseries = pd.Series([10, 20, 30, 40])
aseries = pd.Series(np.array([50, 60, 70, 80]))
dseries = pd.Series({'a': 90, 'b': 100, 'c': 110})
print("Series from List:\n", lseries)
print("\nSeries from Array:\n", aseries)
print("\nSeries from Dictionary:\n", dseries)
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Salary': [50000, 54000, 61000, 58000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
df2 = df.copy()
df2.loc[1, 'Age'] = np.nan
print("\nDataFrame with NaN value:\n", df2)
df2['Age'] = df2['Age'].fillna(df2['Age'].mean())
print("\nAfter Imputation:\n", df2)
df3 = df.groupby('Age').agg({'Salary': 'sum'})
print("\nGrouped DataFrame by Age:\n", df3)
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Name':['John', 'Anna', 'Peter']})
df2 = pd.DataFrame({'ID': [3, 4, 5],
                    'Age': [35, 40, 50]})
df4 = pd.merge(df1, df2, on='ID', how='inner')
print("\nMerged DataFrame:\n", df4)
df5 = pd.concat([df1, df2], axis=0)
print("\nConcatenated DataFrame:\n", df5)
nulls = df.isnull()
print("\nChecking for Null Values:\n", nulls)
dfcsv = pd.read_csv(r'files\csvfile.csv')
print("\nData from CSV:\n", dfcsv)
dfexcel = pd.read_excel(r'files\excelfile.xlsx')
print("\nData from Excel:\n", dfexcel)

