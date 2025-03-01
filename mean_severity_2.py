import pandas as pd

# Load the data
data = pd.read_csv('C:/Users/bencr/Downloads/combined_collision_v3/accidents_summary2.csv')

# Calculate the mean severity score for each OSM_ID and convert it to an integer (1 means low, 2 means medium, 3 means high)
data['mean_severity_score'] = data['accident_severity_scores'].apply(lambda x: int(round(sum(eval(x)) / len(eval(x)))))

# Save the result to a CSV file
data.to_csv('accidents_summary_with_mean_severity.csv', index=False)

print("The result has been saved to 'accidents_summary_with_mean_severity2.csv'.")

