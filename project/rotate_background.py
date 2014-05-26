from random import randint
import fnmatch
import os


def rotate_background():
	numofimages = len(fnmatch.filter(os.listdir("./static/img"), '*.jpg'))
	img = '../static/img/' + str(randint(1, numofimages)) + '.jpg'
	return img
