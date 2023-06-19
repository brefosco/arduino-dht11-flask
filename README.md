# arduino-dht11-flask

## Description

`arduino-dht11-flask` is a project that connects an Arduino Uno to a DHT11 Temperature/Humidity sensor and displays the sensor readings on a web page using Flask.

## Installation

1.  Clone this repository.
2.  Install the required Python packages using pip:
    `pip install -r requirements.txt`

## Hardware Setup

1.  Connect the DHT11 sensor to your Arduino Uno.
2.  Load the Arduino script from the `dhtPython` directory onto your Arduino Uno.
3.  Ensure the serial port and baud rate in the Arduino script match the ones in `flasking.py`.

## Usage

Run the Flask application using Python:

`python flasking.py`

The application will start a web server and display the temperature and humidity readings from the Arduino on the web page at `http://localhost:5000`.
