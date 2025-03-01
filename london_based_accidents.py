import pandas as pd

# Load your dataset
df = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/combined_collisions_v3.csv')

# Define London's borough boundaries
min_lat, max_lat = 51.3550556, 51.6517156
min_lon, max_lon = -0.453256, 0.15050513

# Filter the dataset to include only accidents within the defined boundaries
filtered_df = df[(df['Latitude'] >= min_lat) & (df['Latitude'] <= max_lat) &
                 (df['Longitude'] >= min_lon) & (df['Longitude'] <= max_lon)]

# Count the number of accidents within the boundaries by Accident_Severity
severity_counts_within_boundaries = filtered_df['Accident_Severity'].value_counts()

print("Count of each accident severity index within London's borough boundaries:")
print(severity_counts_within_boundaries)