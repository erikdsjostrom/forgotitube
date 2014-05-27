#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from get_new_video import get_new_video
from rotate_background import rotate_background

app = Flask(__name__)
global img
img = '../static/img/1.jpg'
global user_data
user_data = ['Default: 50', 'Default: random word', "Default: ∞", "Default: 0", "any"]


@app.route('/')
def index():
	global img
	img = rotate_background()
	return render_template('index.html', img=img)


@app.route('/video', methods=['POST', 'GET'])
def video():
	global img
	global user_data
	global id

	if request.method == 'POST':
		#Perhaps a condition to skip all of this if user_input hasn't changed
		limit = request.form['limit']
		if limit and limit != user_data[0]:
			user_data[0] = limit
		query = request.form['query']
		if query and query != user_data[1]:
			user_data[1] = query
		upduration = request.form['upduration']
		if upduration and upduration != user_data[2]:
			user_data[2] = upduration
		loduration = request.form['loduration']
		print(loduration)
		if loduration and loduration != user_data[3]:
			user_data[3] = loduration
		category = request.form['category']
		if category and category != user_data[4] and category != 'any':
			user_data[4] = category
		user_data = [user_data[0], user_data[1], user_data[2], user_data[3], user_data[4]]
		id = get_new_video(user_data)  # Sparar tid om kommenterad
		return render_template('video.html', id=id, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4])
	else:
		id = get_new_video(user_data)  # Sparar tid om kommenterad
		return render_template('video.html', id=id, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4])

if __name__ == '__main__':
	app.run()
