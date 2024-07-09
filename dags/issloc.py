import requests
import json
from datetime import datetime

def fetch_iss_location(**kwargs):
    response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
    data = response.json()
    timestamp = data['timestamp']
    lat = data['latitude']
    lon = data['longitude']
    alt = data['altitude']
    speed = data['velocity']

    #file_path = '/opt/airflow/data/latest_iss_location.json'

    # Save data to a JSON file
    with open('/opt/airflow/data/latest_iss_location.json', 'w') as file:
        json.dump({'timestamp': timestamp, 'latitude': lat, 'longitude': lon, 'altitude': alt, 'velocity': speed}, file)

    print(f"Logged ISS Location: {lat},{lon},{alt},{speed} at {datetime.utcfromtimestamp(timestamp)}")

