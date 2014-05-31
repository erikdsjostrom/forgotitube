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
	user_data = ['', '', '', '', []]
	categories = ["aut", "com", "edu", "ent", "fil", "how", "mus",
															"new",
															"non",
															"peo",
															"pet",
															"sci",
															"spo",
															"tra"]
	category = []
	if request.method == 'POST':
		# Perhaps a condition to skip all of this if user_input hasn't changed
		limit = request.form['limit']
		if limit:
			user_data[0] = limit
		else:
			user_data[0] = ''
		query = request.form['query']
		if query:
			user_data[1] = query
		else:
			user_data[1] = ''
		upduration = request.form['upduration']
		if upduration:
			user_data[2] = upduration
		else:
			user_data[2] = ''
		loduration = request.form['loduration']
		if loduration:
			user_data[3] = loduration
		else:
			user_data[3] = ''
		for cat in categories:
			try:
				category.append(request.form[cat])
			except Exception:
				pass
		user_data[4] = category  # Default input: []. Otherwise list with strings
		videoID = get_new_video(user_data)  # POST Sparar tid om kommenterad
		for x, c in enumerate(user_data[4]):
			user_data[4][x] = c.replace("&", "&amp;")
		if videoID == "Timeout":
			videoID = "Kdgt1ZHkvnM?autoplay=1&iv_load_policy=3"
			return render_template('video.html', id=videoID, img=img,
														limit=user_data[0],
														query=user_data[1],
														upduration=user_data[2],
														loduration=user_data[3],
														category=user_data[4],
														opendisp="block")
		else:
			return render_template('video.html', id=videoID, img=img,
														limit=user_data[0],
														query=user_data[1],
														upduration=user_data[2],
														loduration=user_data[3],
														category=user_data[4],
														opendisp="none")
	else:
		user_data = ['', '', '', '', []]
		videoID = get_new_video(user_data)  # GET Sparar tid om kommenterad
		return render_template('video.html', id=videoID, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4],
													opendisp="none")


@app.route('/continous_video', methods=['POST'])
def continous_video():
	for i in range(2):  # Only for testing should be a while loop in final version
		print('test')
		print(video())

if __name__ == '__main__':
	app.debug = True  # REMOVE THIS IN FINAL VERSION
	app.run()
