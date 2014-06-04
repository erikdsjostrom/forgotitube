#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import g
import flask_sijax
import os
from get_new_video import get_new_video
from rotate_background import rotate_background

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)
global img
global user_data
img = '../static/img/3.jpg'


@app.route('/')
def index():
	global img
	img = rotate_background()
	return render_template('index.html', img=img)


@flask_sijax.route(app, '/video')
def video():
	def get_categories(values):
		categories = []
		if 'aut' in values:
			categories.append('Autos & Vehicles')
		if 'com' in values:
			categories.append('Comedy')
		if 'edu' in values:
			categories.append('People & Blogs')
		if 'ent' in values:
			categories.append('Autos & Vehicles')
		if 'fil' in values:
			categories.append('Film & Animation')
		if 'how' in values:
			categories.append('Howto & Style')
		if 'mus' in values:
			categories.append('Music')
		if 'new' in values:
			categories.append('News & Politics')
		if 'non' in values:
			categories.append('Nonprofits & Activism')
		if 'peo' in values:
			categories.append('People & Blogs')
		if 'pet' in values:
			categories.append('Pets & Animals')
		if 'sci' in values:
			categories.append('Science & Technology')
		if 'spo' in values:
			categories.append('Sports')
		if 'tra' in values:
			categories.append('Travel & Events')
		return(categories)

	def process_form(obj_response, values):
		# Add a check to see if user_data has actually changed...later
		print(values)
		limit = values['limit']
		query = values['query']
		upduration = values['upduration']
		loduration = values['loduration']
		if 'mode' in values:
			#This is were something contititus should be done
			pass
		if len(values) > 4:
			categories = get_categories(values)
		else:
			categories = []
		user_data = [limit, query, upduration, loduration, categories]
		videoID = get_new_video(user_data)
		if videoID == "Timeout":
			print('Timeout')
			videoID = 'Kdgt1ZHkvnM?autoplay=1&iv_load_policy=3'
			video_code = "http://www.youtube.com/embed/" + videoID
			obj_response.css('#timeout', 'display', 'block')
			obj_response.attr('#iframe', 'src', video_code)
		else:
			video_code = "http://www.youtube.com/embed/" + videoID
			obj_response.css('#timeout', 'display', 'none')
			obj_response.attr('#iframe', 'src', video_code)
	if g.sijax.is_sijax_request:
		# Sijax request detected - let Sijax handle it
		g.sijax.register_callback('process_form', process_form)
		return g.sijax.process_request()

	# Regular (non-Sijax request) - render the page template
	user_data = ['', '', '', '', []]
	videoID = get_new_video(user_data)  # GET Sparar tid om kommenterad
	return render_template('video.html', id=videoID, img=img)


if __name__ == '__main__':
	app.debug = True  # REMOVE THIS IN FINAL VERSION
	app.run()
