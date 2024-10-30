# iot-simulation-mqtt-python

This project integrates MQTT communication with a RESTful API using FastAPI and SQLAlchemy. It includes:

- MQTT broker and clients using `paho-mqtt`.
- RESTful API built with FastAPI.
- Client application interacting with the API.
- Data persistence using SQLite.

## Project Structure

- `main.py`: Defines REST API endpoints.
- `database.py`: Database configuration.
- `publisher.py`: MQTT publisher simulating sensor data.
- `subscriber.py`: MQTT subscriber interacting with the REST API.
- `alert_publisher.py`: MQTT publisher for critical alerts.
- `client.py`: Client application for API interaction.
- `requirements.txt`: Project dependencies.

## Requirements

- Python 3.8 or higher
- `paho-mqtt`
- `fastapi`
- `uvicorn`
- `requests`
- `sqlalchemy`


## Installation

1. **Clone the Repository**
2. **Create a Virtual Environment**
   - python3 -m venv venv
   - source venv/bin/activate
3. **Install Dependencies**
   - pip install -r requirements.txt

## Running the Project
Start the MQTT Broker

Ensure Mosquitto is installed and running:
```bash
brew install mosquitto  # On macOS
brew services start mosquitto
```

Run the FastAPI Server
```bash
uvicorn main:app --reload
```

Run the MQTT Subscriber

```bash
python subscriber.py
```

Run the MQTT Publishers

Sensor Data Publisher:
```bash
python publisher.py
```
Critical Alerts Publisher:
```bash
python alert_publisher.py
```