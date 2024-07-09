from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

@app.route('/iss-location', methods=['GET'])
def get_iss_location():
    file_path = '../data/latest_iss_location.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            location = json.load(file)
            if location:
                latest_location = location  # Get the latest location
                return jsonify({
                    'latitude': latest_location['latitude'],
                    'longitude': latest_location['longitude'],
                    'altitude': latest_location.get('altitude', 'N/A'),
                    'velocity': latest_location.get('velocity', 'N/A')
                })
    return jsonify({'error': 'Data not found'}), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
