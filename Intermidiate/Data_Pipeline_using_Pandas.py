import pandas as pd

# Loading data
data = {'Name': ['Shah', 'Masumi', 'Jinay'], 'Age': [25, 30, 35], 'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Data transformation pipeline
df['Salary'] = df['Salary'] * 1.1  # Applying a 10% raise
df['Age'] = df['Age'] + 1  # Aging each person by 1 year

# Filtering data
df_filtered = df[df['Salary'] > 55000]

# Display result
print(df_filtered)
