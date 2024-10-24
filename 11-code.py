import pandas as pd
try:
    # Read Excel file
    df = pd.read_excel(r'files\sample.xlsx')
except FileNotFoundError:
    print("Error: The file 'data.xlsx' was not found.")
    exit()
except Exception as e:
    print(f"Error reading 'data.xlsx': {e}")
    exit()
# Display first few rows
print("First few rows:")
print(df.head())
# Get summary statistics
print("\nSummary statistics:")
print(df.describe())
# Check if 'Age' column exists
if 'Age' not in df.columns:
    print("Error: 'Age' column not found in the data.")
else:
    # Filter data
    filtered_data = df[df['Age'] > 30]
    print("\nFiltered data (Age > 30):")
    print(filtered_data)
# Check if 'Salary' column exists
if 'Salary' not in df.columns:
    print("Error: 'Salary' column not found in the data.")
else:
    # Sort data
    sorted_data = df.sort_values(by='Salary', ascending=False)
    print("\nSorted data (by Salary):")
    print(sorted_data)
    # Add a new column
    df['Bonus'] = df['Salary'] * 0.1
    print("\nData with new column (Bonus):")
    print(df)
    # Write to Excel file
    try:
        df.to_excel(r'files\output.xlsx', index=False)
        print("\nData written to output.xlsx")
    except Exception as e:
        print(f"Error writing to 'output.xlsx': {e}")

