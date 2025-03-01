import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/london_boroughs_coordinates.csv')

# Determine the minimum and maximum values of Location_Easting and Location_Northing
minimum_latitude = df['Latitude'].min()
maximum_latitude = df['Latitude'].max()
minimum_longitude = df['Longitude'].min()
maximum_longitude = df['Longitude'].max()

print(f"Minimum Latitude: {minimum_latitude}")
print(f"Maximum Latitude: {maximum_latitude}")
print(f"Minimum Longitude: {minimum_longitude}")
print(f"Maximum Longitude: {maximum_longitude}")