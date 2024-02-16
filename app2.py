from flask import Flask, request, render_template
import urllib.request
import json
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # For default city name Mathura
        city = 'Mathura'

    # Construct the URL for the API request
    api_key = 'da5e53a1de645f10d9bc24d45884d83f'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    # URL for weather icon
    icon = list_of_data['weather']['0']['icon']
    url_icon = f'https://openweathermap.org/img/wn/{icon}.png'
    
    # Fetching data from the API
    source = urllib.request.urlopen(url).read()

    # Converting JSON data to a dictionary
    list_of_data = json.loads(source)

   # Convert temperature from Kelvin to Celsius
    temperature_kelvin = list_of_data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    
    sunrise_time =list_of_data['sys']['sunrise']
    sunset_time =list_of_data['sys']['sunset']
    
    datetime_object_sunrise = datetime.utcfromtimestamp(sunrise_time)
    datetime_object_sunset = datetime.utcfromtimestamp(sunset_time)
    
    formatted_sunset = datetime_object_sunset.strftime('%H:%M')    
    formatted_sunrise = datetime_object_sunrise.strftime( '%H:%M')    
    

    # Data for variable list_of_data 
    data = { 
        "cityname": str(list_of_data['name']), 
        "country_code": str(list_of_data['sys']['country']), 
        "sunrise": str(formatted_sunset),
        "sunrset": str(formatted_sunrise),
        "temp": str(round(temperature_celsius, 2)) + '°C',
        "pressure": str(list_of_data['main']['pressure']), 
        "humidity": str(list_of_data['main']['humidity']) + '%', 
        "feels_like": str(round(temperature_celsius, 2)) + '°C',
        "temp_min": str(round(temperature_celsius, 1)) + '°C',
        "temp_max": str(round(temperature_celsius, 1)) + '°C',
        "description": str((list_of_data['weather'][0]['description'])).capitalize(), 
        "wind": str(list_of_data['wind']['speed'])+ ' km/h', 
        "icon": str((list_of_data['weather']['0']['icon'])),
        "icon_url": url_icon,
    } 
    print(data) 
    print("=============================================")
    print(source)
    return render_template('index3.html', data=data)

if __name__ == '__main__': 
    app.run(debug=True)
