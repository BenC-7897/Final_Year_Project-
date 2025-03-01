from geopy.geocoders import Nominatim
import pandas as pd

# List of London's boroughs
boroughs = [
    "Barking and Dagenham", "Barnet", "Bexley", "Brent", "Bromley", "Camden", "Croydon", 
    "Ealing", "Enfield", "Greenwich", "Hackney", "Hammersmith and Fulham", "Haringey", 
    "Harrow", "Havering", "Hillingdon", "Hounslow", "Islington", "Kensington and Chelsea", 
    "Kingston upon Thames", "Lambeth", "Lewisham", "Merton", "Newham", "Redbridge", 
    "Richmond upon Thames", "Southwark", "Sutton", "Tower Hamlets", "Waltham Forest", 
    "Wandsworth", "Westminster", "City of London"  
]

# Initialize geolocator
geolocator = Nominatim(user_agent="london_boroughs_locator")

# Dictionary to store boroughs and their coordinates
borough_coordinates = {}

# Get coordinates for each borough
for borough in boroughs:
    location = geolocator.geocode(f"{borough}, London, UK")
    if location:
        borough_coordinates[borough] = (location.latitude, location.longitude)
    else:
        borough_coordinates[borough] = (None, None)

# Create a DataFrame from the dictionary
df = pd.DataFrame(borough_coordinates.items(), columns=['Borough', 'Coordinates'])

# Split the coordinates into separate latitude and longitude columns
df[['Latitude', 'Longitude']] = pd.DataFrame(df['Coordinates'].tolist(), index=df.index)

# Drop the 'Coordinates' column as it's no longer needed
df.drop(columns=['Coordinates'], inplace=True)

# Save the DataFrame to an Excel file
df.to_csv("london_boroughs_coordinates.csv", index=False)

print("The coordinates have been saved to london_boroughs_coordinates.csv")