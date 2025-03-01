import requests
import csv
import os
from concurrent.futures import ThreadPoolExecutor

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

def get_osm_info(lat, lon):
    query = f"""
    [out:json];
    (
      node(around:10, {lat}, {lon});
      way(around:10, {lat}, {lon});
      relation(around:10, {lat}, {lon});
    );
    out center;
    """
    response = requests.get(OVERPASS_URL, params={"data": query})
    if response.status_code == 200:
        data = response.json()
        if "elements" in data and len(data["elements"]) > 0:
            element = data["elements"][0]
            return element["id"], element["type"]
    return None, None

def process_coordinate(lat, lon):
    try:
        osm_id, osm_type = get_osm_info(lat, lon)
        print(f"Latitude: {lat}\nLongitude: {lon}\nOSM_ID: {osm_id}\nOSM_Type: {osm_type}\n")
        return lat, lon, osm_id, osm_type
    except Exception as e:
        print(f"Error processing coordinate {lat}, {lon}: {e}\n")
        return lat, lon, None, None

def process_chunk(chunk_file):
    output_file = chunk_file.replace('.csv', '_processed.csv')
    
    try:
        with open(chunk_file, 'r', encoding='utf-8-sig') as infile, open(output_file, 'w', newline='') as outfile:
            csv_reader = csv.reader(infile)
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(['Latitude', 'Longitude', 'OSM_ID', 'OSM_Type'])
            
            next(csv_reader)  # Skip header
            chunk = []
            for row in csv_reader:
                lat, lon = map(float, row[:2])
                chunk.append((lat, lon))
                
            with ThreadPoolExecutor(max_workers=9) as executor:
                results = list(executor.map(lambda coord: process_coordinate(coord[0], coord[1]), chunk))
                
            for result in results:
                csv_writer.writerow(result)
                
        print(f"Written to {output_file}\n")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}. Make sure the file exists.\n")
    except Exception as e:
        print(f"Error processing chunk: {e}\n")

# Example usage: process a specific osm_info_chunk file
chunk_file = 'C:/Users/bencr/Downloads/chunks/osm_info_chunk_18.csv'
process_chunk(chunk_file)