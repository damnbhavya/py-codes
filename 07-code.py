# read csv file
import pandas as pd
df1 = pd.read_csv(r'files\Iris.csv')
print(df1)

# count the null values
df2 = pd.read_csv(r'files\5_6309864337204842721.csv')
nulls = df2.isnull().sum()
tnulls = nulls.sum()
print("Total null values:", tnulls)

# group by species and count each species
species = df1['Species'].value_counts()
print(species)

# merge df1 and df2 and store in df3
df3 = pd.merge(df1, df2, on='Id', how='inner')
df3.to_csv(r'files\merge.csv', index=False)
print("Saved merged data.")
print(df3)

# concat df1 and df2 and store in df4
df4 = pd.concat([df1, df2], ignorqe_index=True)
df4.to_csv(r'files\concat.csv', index=False)
print("Saved concatenated data.")
print(df4)

# replace the null values in df2 by the mean of sepal length
mean_value = df2['SepalLengthCm'].mean()
df2.fillna(mean_value, inplace=True)
print("Null values replaced.")
print(df2)

# checking null values
nulls = df2.isnull().sum()
tnulls = nulls.sum()
print("Total null values:", tnulls)