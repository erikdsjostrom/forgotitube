from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from get_new_video import get_new_video
#from rotate_background import rotate_background

app = Flask(__name__)

global glimit
glimit = 'Default: 50'
global gquery
gquery = 'Default: random word'

@app.route('/')
def index():
	# global glimit
	# glimit = 'Default: 50'
	# global gquery
	# gquery = 'Default: random word'
	#img = rotate_background.py
	return render_template('index.html')


@app.route('/video', methods=['POST'])
def video():
	global glimit
	global gquery
	#id = get_new_video() TAKE NOTE
	limit = request.form['limit']
	if limit and limit != glimit:
		glimit = limit
	query = request.form['query']
	if query and query != gquery:
		gquery = query
	id = 'ay-FQAafeR0'
	return render_template('video.html', id=id, limit=glimit, query=gquery)

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
