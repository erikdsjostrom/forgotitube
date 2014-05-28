#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
#from get_new_video import get_new_video
from rotate_background import rotate_background

app = Flask(__name__)
global user_data
user_data = 'placeholder'
global img
img = 'placeholder'
global old_user_data
old_user_data = ['Default: 50', 'Default: Random word', "Default: ∞", "Default: 0", "any"]


@app.route('/')
def index():
	global img
	img = rotate_background()
	return render_template('index.html', img=img)


@app.route('/video', methods=['POST', 'GET'])
def video():
	global img
	global user_data
	global old_user_data
	global id
	if request.method == 'POST':
		# Perhaps a condition to skip all of this if user_input hasn't changed
		limit = request.form['limit']
		if limit:
			user_data[0] = limit
		query = request.form['query']
		if query:
			user_data[1] = query
		upduration = request.form['upduration']
		if upduration:
			user_data[2] = upduration
		loduration = request.form['loduration']
		if loduration:
			user_data[3] = loduration
		category = request.form['category']
		if category and category != 'any':
			user_data[4] = category
		if user_data[0] == 'Default: 50':
			user_data[0] = ''
		if user_data[1] == 'Default: Random word':
			user_data[1] = ''
		if user_data[2] == 'Default: ∞':
			user_data[2] = ''
		if user_data[3] == 'Default: 0':
			user_data[3] == '1'
		user_data[3] = '1'
		id = get_new_video(user_data)  # POST Sparar tid om kommenterad
		print(user_data)
		return render_template('video.html', id=id, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4])
	else:
		user_data = ['Default: 50', 'Default: Random word', "Default: ∞", "Default: 0", "any"]
		id = get_new_video(["10000"] + [""] + [""] + [""] + ["any"])  # GET Sparar tid om kommenterad
		return render_template('video.html', id=id, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4])

if __name__ == '__main__':
	app.debug = True
	app.run()
