import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/osm_info.csv')

# Read the second CSV file
df2 = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/accidents_summary_with_mean_severity_2.csv')

# Merge the two files on the common columns 'latitude' and 'longitude'
merged_df = pd.merge(df1, df2, on=['Latitude', 'Longitude'])

# Save the merged data to a new CSV file
merged_df.to_csv('merged_output_file.csv', index=False)

