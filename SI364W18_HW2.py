## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file (and a little bit inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that the routes described in the README exist 
#and render the templates they are supposed to (all templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required, Email
import requests
import json

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################

@app.route('/artistform')
def artistform():
	return render_template('artistform.html')

@app.route('/artistinfo')
def artistinfo():
	if request.method == 'GET':
		base_url = "https://itunes.apple.com/search"
		params_diction = {}

		artist = request.args.get('artist')
		params_diction['term'] = artist
		resp = requests.get(base_url, params = params_diction)
		result = json.loads(resp.text)['results']

		return render_template('artist_info.html', objects = result)

@app.route('/artistlinks')
def artistlinks():
	return render_template(artist_links.html)

@app.route('/specific/song/<artist_name>')
def specific(artist_name):
	if request.method == 'GET':
		base_url = "https://itunes.apple.com/search"
		params_diction = {}
		
		result = request.args
		params_diction['term'] = artist_name
		resp = requests.get(base_url, params = params_diction)
		result = json.loads(resp.text)['results']
		return render_template('specific_artist.html', results = result)

	
#create class to represent WTForm that inherits flask form
class AlbumEntryForm(FlaskForm):
	label = StringField('Enter the name of an album: ', validators=[Required()])
	options = RadioField('How much do you like this album? (1 is low, 3 is high) ', choices=[('1','1'),('2','2'),('3','3')], validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/album_entry')
def album_entry():
	album_entry_form = AlbumEntryForm()
	return render_template('album_entry.html', form = album_entry_form)

@app.route('/album_result', methods = ['GET', 'POST'])
def album_result():
	if request.method == 'POST':
		album_dict = {}
		album_title = request.form['name']
		ranking = request.form['options']
		album['title'] = title
		album['score'] = score
		return render_template('album_data.html', album = album )

####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/user/<name>')
def hello_user(name):
	return '<h1>Hello {0}<h1>'.format(name)


if __name__ == '__main__':
	app.run(use_reloader=True,debug=True)
