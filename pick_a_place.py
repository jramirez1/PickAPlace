
from flask import Flask,jsonify, render_template, request, session
import requests, json, os
from flask_bootstrap import Bootstrap
from pprint import pprint






app = Flask(__name__)
app.secret_key = os.urandom(24)
bootstrap = Bootstrap(app)



@app.route('/')
def home():


	return render_template('index.html')
	






@app.route('/zip', methods = ['GET', 'POST'])
def zip():
	if request.method =='POST':
		zip = request.form['zipcode']

		session['zip_code'] = str(zip.replace(' ', "+"))

		return render_template('index.html', zip = zip)






@app.route('/info/<string:place>', methods = ['GET', 'POST'])
def info(place):

	#a = request.form.get('zipcode')
	#return(a)
	if 'zip_code' in session:
		query_zip=session['zip_code']  


	api_key = 'put_key_here'
	endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

	food_type = place.replace(' ', '+')

	params = 'query={}+near+{}&key={}'.format(food_type, query_zip, api_key)

	place_request = endpoint + params

	response = requests.get(place_request)

	info = response.json()

	results = info['results']
			
	return render_template('info.html', results = results)


@app.route('/restaurant/<string:place_id>')
def restaurant(place_id):
	
	restaurant_id = place_id

	api_key = 'put_key_here'
	endpoint = 'https://maps.googleapis.com/maps/api/place/details/json?'

	query_parameters = 'place_id={}&key={}'.format(restaurant_id, api_key)
	query = endpoint + query_parameters

	details_request = requests.get(query)

	details = details_request.json()

	results = details['result']


	return render_template('restaurants.html', results = results)

