import pandas as pd

# Load your dataset
df = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/combined_collisions_v3_modified.csv')

# Categorize data by accident_severity_index
categories = {1: 'Low', 2: 'Medium', 3: 'High'}
df['severity_category'] = df['Accident_Severity'].map(categories)

# Count the number of times each accident severity index appears
severity_counts = df['Accident_Severity'].value_counts()

print(df)
print("\nCount of each accident severity index:")
print(severity_counts)
