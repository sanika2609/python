import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print("Average Age:", average_age)
