from random import randint


def rotate_background():
	img = '../static/img/' + str(randint(1, 12)) + '.jpg'
	return img

rotate_background()
