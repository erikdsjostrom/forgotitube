from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from get_new_video import get_new_video
from rotate_background import rotate_background

app = Flask(__name__)
global id
id = 'ay-FQAafeR0'
global img
img = '../static/img/1.jpg'
global glimit
glimit = 'Default: 50'  # Start value
global gquery
gquery = 'Default: random word'  # Start value


@app.route('/')
def index():
	global img
	img = rotate_background()
	print(img)
	return render_template('index.html', img=img)


@app.route('/video', methods=['POST', 'GET'])
def video():
	global img
	global glimit
	global gquery
	global id
	#id = get_new_video()  # Sparar tid om kommenterad
	id = 'ay-FQAafeR0'  # Statisk id
	if request.method == 'POST':
		limit = request.form['limit']
		#Check if the limit has been updated and changed from the previous limit
		if limit and limit != glimit:
			glimit = limit
		query = request.form['query']
		if query and query != gquery:
			gquery = query
		return render_template('video.html', id=id, img=img, limit=glimit, query=gquery)
	else:
		return render_template('video.html', id=id, img=img, limit=glimit, query=gquery)

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
