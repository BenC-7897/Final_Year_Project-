import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/osm_info.csv')

# Drop rows where both 'OSM_ID' and 'OSM_TYPE' have empty values
df_cleaned = df.dropna(subset=['OSM_ID', 'OSM_Type'], how='all')

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('C:/Users/bencr/Downloads/combined_collision_v3/osm_ids.csv', index=False)