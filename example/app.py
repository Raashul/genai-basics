## basic example using pandas

import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df)

# Get basic statistics
print("\nSummary Statistics:\n", df.describe())

# Select a specific column
print("\nAges:\n", df['Age'])

# Filter data (e.g., people older than 28)
filtered_df = df[df['Age'] > 28]
print("\nFiltered Data (Age > 28):\n", filtered_df)
