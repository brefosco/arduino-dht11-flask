from flask import Flask, render_template
from serial import Serial

def get_data_from_arduino():
    arduino = Serial('com8', 9600)
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_in_floats = []
    list_values = decoded_values.split("x")

    for item in list_values:
        list_in_floats.append(float(item))
    temp = list_in_floats[0]
    hum = list_in_floats[1]
    arduino.close()
    return hum, temp

app = Flask(__name__)

@app.route('/')
def show_temp():
    hum, temp = get_data_from_arduino()
    return render_template('hello.html', hum=hum, temp=temp)


if __name__ == "__main__":
    app.run()
