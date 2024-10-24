import pandas as pd
path = 'file.xlsx'
df = pd.read_excel(path)
print(df)

path = 'output.xlsx'
df.to_excel(path, index=False)
print(f"DataFrame has been written to {path}")