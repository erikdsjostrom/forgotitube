from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from get_new_video import get_new_video
from rotate_background import rotate_background

app = Flask(__name__)
# global id
# id = 'ay-FQAafeR0'
global img
img = '../static/img/1.jpg'
global user_data
user_data = ['Default: 50', 'Default: random word', "Default: ∞", "Default: 0",
													"any", "Default: 5", "Default: 0",
													"Default: ∞", "Default: 0",
													"Default: ∞", "Default: 0"]


@app.route('/')
def index():
	global img
	img = rotate_background()
	print(img)  # This should probably not be here in final version
	return render_template('index.html', img=img)


@app.route('/video', methods=['POST', 'GET'])
def video():
	global img
	global user_data
	global id
	#user_data = [""]*4 + ["any"] + [""]*6
	#id = get_new_video(user_data)  # Sparar tid om kommenterad
	id = 'ay-FQAafeR0'  # Statisk id
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
		if loduration and loduration != user_data[3]:
			user_data[3] = loduration
		category = request.form['category']
		if category and category != user_data[4]:
			user_data[4] = category
		uprating = request.form['uprating']
		if uprating and uprating != user_data[5]:
			user_data[5] = uprating
		lorating = request.form['lorating']
		if lorating and lorating != user_data[6]:
			user_data[6] = lorating
		uplikes = request.form['uplikes']
		if uplikes and uplikes != user_data[7]:
			user_data[7] = uplikes
		lolikes = request.form['lolikes']
		if lolikes and lolikes != user_data[8]:
			user_data[8] = lolikes
		updislikes = request.form['updislikes']
		if updislikes and updislikes != user_data[9]:
			user_data[9] = updislikes
		lodislikes = request.form['lodislikes']
		if lodislikes and lodislikes != user_data[10]:
			user_data[10] = lodislikes
		user_data = [user_data[0], user_data[1], user_data[2],
			user_data[3], user_data[4], user_data[5], user_data[6],
			user_data[7], user_data[8], user_data[9], user_data[10]]
		print(user_data)
		#id = get_new_video(user_data)  # Sparar tid om kommenterad
		return render_template('video.html', id=id, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4],
													uprating=user_data[5],
													lorating=user_data[6],
													uplikes=user_data[7],
													lolikes=user_data[8],
													updislikes=user_data[9],
													lodislikes=user_data[10])
	else:
		return render_template('video.html', id=id, img=img,
													limit=user_data[0],
													query=user_data[1],
													upduration=user_data[2],
													loduration=user_data[3],
													category=user_data[4],
													uprating=user_data[5],
													lorating=user_data[6],
													uplikes=user_data[7],
													lolikes=user_data[8],
													updislikes=user_data[9],
													lodislikes=user_data[10])

with app.test_request_context():
	print(url_for('index'))
	print(url_for('video'))
	print(url_for('static', filename='style.css'))

if __name__ == '__main__':
	# HEY! DEBUG IS TURNED ON REMEMBER TO TURN IT OFF WHEN YOU LEAVE!!!
	# Lol
	app.debug = True
	#DON'T YOU DARE FORGET IT
	app.run()
