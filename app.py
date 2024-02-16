# from flask import Flask, render_template, request 

# # import json to load JSON data to a python dictionary 
# import json 

# # urllib.request to make a request to api 
# import urllib.request 


# app = Flask(__name__) 
# # api = 'da5e53a1de645f10d9bc24d45884d83f'
# @app.route('/', methods =['POST', 'GET']) 
# def weather(): 
# 	if request.method == 'POST': 
# 		city = request.form['city'] 
# 	else: 
# 		# for default name mathura 
# 		city = 'mathura'


#     # construct the URL for the API request
# 	api = 'da5e53a1de645f10d9bc24d45884d83f'
# 	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
	
# 	# source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid =' + api+'').read() 
# 	source = urllib.request.urlopen(url).read() 
#     # print(source)
# 	# converting JSON data to a dictionary 
# 	list_of_data = json.loads(source)
# ========
from flask import Flask, request
import urllib.request
import json

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

    # Fetching data from the API
    source = urllib.request.urlopen(url).read()

    # Converting JSON data to a dictionary
    list_of_data = json.loads(source)

    # Process the data as needed
    # ...

    

	# data for variable list_of_data 
    data = { 
		"country_code": str(list_of_data['sys']['country']), 
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']), 
		"temp": str(list_of_data['main']['temp']) + 'k', 
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
	} 
    print(data) 
    print("=============================================")
    print(source)
    return render_template('index.html', data=data)
    # return "Weather data retrieved successfully"

if __name__ == '__main__': 
	app.run(debug = True) 
