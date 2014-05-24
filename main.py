from flask import Flask
from flask import url_for
from flask import render_template
from get_new_video import get_new_video

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/video')
def video():
	id = get_new_video()
	return render_template('video.html', id=id)

with app.test_request_context():
	print(url_for('index'))
	print(url_for('video'))
	print(url_for('static', filename='style.css'))

if __name__ == '__main__':
	app.run()
