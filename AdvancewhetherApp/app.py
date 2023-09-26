from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample weather data stored in a dictionary
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>/', methods=['GET'])
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/weather/', methods=['POST'])
def create_weather():
    new_weather = request.get_json()
    if 'city' in new_weather and 'temperature' in new_weather and 'weather' in new_weather:
        city = new_weather['city']
        weather_data[city] = {
            'temperature': new_weather['temperature'],
            'weather': new_weather['weather']
        }
        return jsonify({'message': 'Weather data created'}), 201
    else:
        return jsonify({'error': 'Invalid data format'}), 400

@app.route('/weather/<string:city>/', methods=['PUT'])
def update_weather(city):
    if city in weather_data:
        updated_weather = request.get_json()
        if 'temperature' in updated_weather:
            weather_data[city]['temperature'] = updated_weather['temperature']
        if 'weather' in updated_weather:
            weather_data[city]['weather'] = updated_weather['weather']
        return jsonify(weather_data[city])
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/weather/<string:city>/', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return '', 204
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
