# OrbitFlow: Real-Time ISS Tracking with Airflow

OrbitFlow is a dynamic project that uses Apache Airflow to track the International Space Station (ISS) in real-time. The project fetches ISS location data, updates it continuously, and provides live visualizations using Flask and Leaflet.

## Features
- Real-time ISS location tracking
- Continuous updates with Apache Airflow
- Live visualizations using Flask and Leaflet
- Display of ISS altitude and speed

## Architecture
- **Airflow**: Schedules and fetches ISS location data.
- **Flask**: Serves the ISS location data and renders the web interface.
- **Leaflet**: Provides the interactive map for visualizing the ISS path.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/orbitflow.git
   cd orbitflow
   ```

2. Launch the application using Docker Compose:
    ```bash
    docker-compose up -d
    ```

Access the Airflow web interface at http://localhost:8080.

Access the Flask app at http://localhost:5000.

Usage
Airflow will automatically schedule and run the task to fetch ISS location data.
Open your browser and navigate to http://localhost:5000 to see the live tracking map.
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

