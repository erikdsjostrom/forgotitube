#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from get_new_video import get_new_video
from rotate_background import rotate_background

app = Flask(__name__)
global img
img = 'placeholder'


@app.route('/')
def index():
	global img
	img = rotate_background()
	return render_template('index.html', img=img)


@app.route('/video', methods=['POST', 'GET'])
def video():
	global img
	user_data = ['', '', '', '', 'any']
	if request.method == 'POST':
		# Perhaps a condition to skip all of this if user_input hasn't changed
		limit = request.form['limit']
		if limit and limit != 50:
			user_data[0] = limit
		else:
			user_data[0] = ''
		query = request.form['query']
		if query:
			user_data[1] = query
		else:
			user_data[1] = ''
		upduration = request.form['upduration']
		if upduration and upduration != 'inf':
			user_data[2] = upduration
		else:
			user_data[2] = ''
		loduration = request.form['loduration']
		if loduration:
			user_data[3] = loduration
		else:
			user_data[3] = ''
		category = request.form['category']
		print
		if category and category != 'Any':
			user_data[4] = category

		videoID = get_new_video(user_data)  # POST Sparar tid om kommenterad
		if videoID == "Timeout":
			return render_template('video.html', id="Kdgt1ZHkvnM?autoplay=1&iv_load_policy=3", img=img,
														limit=user_data[0],
														query=user_data[1],
														upduration=user_data[2],
														loduration=user_data[3],
														category=user_data[4].replace('&', '&amp;'),
														opendisp="block")
		else:
			return render_template('video.html', id=videoID, img=img,
														limit=user_data[0],
														query=user_data[1],
														upduration=user_data[2],
														loduration=user_data[3],
														category=user_data[4].replace('&', '&amp;'),
														opendisp="none")
	else:
		user_data = ['', '', '', '', 'any']
		videoID = get_new_video(user_data)  # GET Sparar tid om kommenterad
		return render_template('video.html', id=videoID, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4],
													opendisp="none")

if __name__ == '__main__':
	app.debug = True #REMOVE THIS IN FINAL VERSION
	app.run()
