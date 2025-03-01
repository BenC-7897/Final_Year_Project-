import pandas as pd

# Load the data
data = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/combined_collisions_v3.csv')

# Keep relevant columns
data = data[['Latitude', 'Longitude', 'Accident_Severity']]

# Define the boundaries for London's boroughs
min_latitude = 51.3550556
max_latitude = 51.6517156
min_longitude = -0.453256
max_longitude = 0.15050513

# Filter data within the defined boundaries
filtered_data = data[
    (data['Latitude'] >= min_latitude) &
    (data['Latitude'] <= max_latitude) &
    (data['Longitude'] >= min_longitude) &
    (data['Longitude'] <= max_longitude)
]

# Filter data to include only accident severity scores of 1, 2, and 3
filtered_data = filtered_data[filtered_data['Accident_Severity'].isin([1, 2, 3])]

# Group by Latitude and Longitude and calculate the number of accidents and accident severity scores
result = filtered_data.groupby(['Latitude', 'Longitude']).agg(
    number_of_accidents=('Latitude', 'size'),
    accident_severity_scores=('Accident_Severity', lambda x: list(x))
).reset_index()

# Save the result to a CSV file
result.to_csv('accidents_summary2.csv', index=False)

print("The result has been saved to 'accidents_summary.csv'.")