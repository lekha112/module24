pip install pandas
import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
# Access the 'Name' column
print(df['Name'])
# Access the first row
print(df.iloc[0])  # By index

# Access the row with index label 2
print(df.loc[2])  # By index label
# Adding a new column for Salary
df['Salary'] = [70000, 80000, 65000, 90000]

print(df)
# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]

print(filtered_df)
# Summary statistics
print(df.describe())
