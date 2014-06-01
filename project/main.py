#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from get_new_video import get_new_video
from rotate_background import rotate_background

app = Flask(__name__)
global img
img = '../static/img/3.jpg'


@app.route('/')
def index():
	global img
	img = rotate_background()
	return render_template('index.html', img=img)


@app.route('/video', methods=['POST', 'GET'])
def video():
	global img
	user_data = ['', '', '', '', []]
	if request.method == 'POST':
		try:
			# If continous mode is turned on
			mode = request.form['mode']
			videoID, user_data = get_video()
			if videoID == "Timeout":
				videoID = "Kdgt1ZHkvnM?autoplay=1&iv_load_policy=3"
				return render_template('video.html', id=videoID, img=img,
															mode='checked',
															limit=user_data[0],
															query=user_data[1],
															upduration=user_data[2],
															loduration=user_data[3],
															category=user_data[4],
															opendisp="block")
			else:
				return render_template('video.html', id=videoID, img=img,
															mode='checked',
															limit=user_data[0],
															query=user_data[1],
															upduration=user_data[2],
															loduration=user_data[3],
															category=user_data[4],
															opendisp="none")
		except:
			# If continous mode is turned off
			videoID, user_data = get_video()
			if videoID == "Timeout":
				videoID = "Kdgt1ZHkvnM?autoplay=1&iv_load_policy=3"
				return render_template('video.html', id=videoID, img=img,
															mode='unchecked',
															limit=user_data[0],
															query=user_data[1],
															upduration=user_data[2],
															loduration=user_data[3],
															category=user_data[4],
															opendisp="block")
			else:
				return render_template('video.html', id=videoID, img=img,
															mode='unchecked',
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


@app.route('/get_video')
def get_video():
	user_data = ['', '', '', '', []]
	categories = ["aut", "com", "edu", "ent", "fil", "how", "mus",
															"new",
															"non",
															"peo",
															"pet",
															"sci",
															"spo",
															"tra"]
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
	category = []
	for cat in categories:
		try:
			category.append(request.form[cat])
		except Exception:
			pass
	user_data[4] = category  # Default input: []. Otherwise list with strings
	videoID = get_new_video(user_data)  # POST Sparar tid om kommenterad
	for x, c in enumerate(user_data[4]):  # Replaces every &
			user_data[4][x] = c.replace("&", "&amp;")
	return(videoID, user_data)


@app.route('/get_video_id')
def get_video_id():
	user_data = ['', '', '', '', []]
	videoID = get_new_video(user_data)
	video_code = "http://www.youtube.com/embed/" + videoID
	return jsonify(result=video_code)


@app.route('/get_template')
def get_template(videoID, user_data):
	pass

if __name__ == '__main__':
	app.debug = True  # REMOVE THIS IN FINAL VERSION
	app.run()
