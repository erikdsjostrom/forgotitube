from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from get_new_video import get_new_video
#from rotate_background import rotate_background

app = Flask(__name__)


@app.route('/')
def index():
	#img = rotate_background.py
	return render_template('index.html')


# @app.route('/video', methods=['POST'])
# def settings():
# 	limit = request.form['limit']
# 	query = request.form['query']
# 	print(limit)
# 	print(lol)
# 	# upduration = request.form['upduration']
# 	# loduration = request.form['loduration']
# 	# category = request.form['category']
# 	# uprating = request.form['uprating']
# 	# lorating = request.form['lorating']
# 	# uplikes = request.form['uplikes']
# 	# lolikes = request.form['lolikes']
# 	# updislikes = request.form['updislikes']
# 	# lodislikes = request.form['lodislikes']
# 	# id = get_new_video()  TAKE NOTE
# 	id = 'ay-FQAafeR0'
# 	return render_template('video.html', id=id, limit=limit, query=query)
# 															# upduration=upduration,
# 															# loduration=loduration,
# 															# category=category,
# 															# uprating=uprating,
# 															# lorating=lorating,
# 															# uplikes=uplikes,
# 															# lolikes=lolikes,
# 															# updislikes=updislikes,
# 															# lodislikes=lodislikes)


@app.route('/video', methods=['POST'])
def video():
	#id = get_new_video() TAKE NOTE
	limit = request.form['limit']
	query = request.form['query']
	id = 'ay-FQAafeR0'
	print('lol')
	return render_template('video.html', id=id, limit=limit, query=query)

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
