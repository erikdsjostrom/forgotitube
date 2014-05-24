from random import randint


def rotate_background():
	img = '../static/img/' + str(randint(1, 13)) + '.jpg'
	return img

rotate_background()
