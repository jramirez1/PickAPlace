
from flask import Flask, render_template, request
import requests, json
from flask_bootstrap import Bootstrap
from pprint import pprint




#parameters for query
#query=restaurants+in+Salinas&key=api_key'

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def home():
	return render_template('index.html')
	#for k in results:
	#	print(k['name'])



@app.route('/info/<string:place>', methods = ['GET', 'POST'])
def info(place):

	api_key = 'AIzaSyBFfpbANyFIZVheOZ7Pi4iJ5ojT7fjnGEo'
	endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

	food_type = place.replace(' ', '+')

	

			

	params = 'query={}+near+san+francisco&key={}'.format(food_type,api_key)

	place_request = endpoint + params

	response = requests.get(place_request)

	info = response.json()

	results = info['results']
			
	return render_template('info.html', results = results)

'''
#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCLNO5mol_LjqDuOkTKLBke4Q9de-6GVy4'

#Asks the user to input Where they are and where they want to go.
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')

#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request

#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()

#Loads response as JSON
directions = json.loads(response)
print(directions)
'''