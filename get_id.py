#!/usr/bin/python
import random
import urllib
import urllib.request
import re


class Video():
	def __init__(self, id, list):
		self.id = id
		self.viewcount = int(list[0])
		self.title = list[1]
		self.duration = int(list[2])
		self.likes = int(list[3])
		self.dislikes = int(list[4])
		self.rating = float(list[5])
		self.category = list[6]

	def show_info(self):
		print([self.id, self.viewcount, self.title,
								self.duration, self.likes,
								self.dislikes, self.rating,
								self.category])


def get_random_id(searchquery):
		gdataurl = "http://gdata.youtube.com/feeds/api/videos?q=" + searchquery + "&orderby=published"
		try:
			sock = urllib.request.urlopen(gdataurl).read().decode("utf-8")
			idatt = re.compile("url='http://www.youtube.com/v/(.*?)\?")
			foundid = idatt.findall(sock)
			return random.choice(foundid)
		except Exception:
			pass


# get_info takes an id and returns a list with the following things
# 0: view count, 1: title, 2: duration (sec),
# 3: likes, 4: dislikes, 5: category
def get_info(id):
	url = "https://gdata.youtube.com/feeds/api/videos/" + str(id) + "?v=2"
	try:
		sock = urllib.request.urlopen(url).read().decode("utf-8")
		vc = re.compile("viewCount='(.*?)\'")
		dur = re.compile("duration='(.*?)\'")
		numlik = re.compile("numLikes='(.*?)\'")
		numdislik = re.compile("numDislikes='(.*?)\'")
		cat = re.compile("category label='(.*?)\'")
		title = re.compile("<title>(.*?)</title>")
		rat = re.compile("rating average='(.*?)\'")
		data = [""]*7
		data[0] = str(vc.findall(sock)[0])
		data[1] = str(title.findall(sock)[0])
		data[2] = str(dur.findall(sock)[0])
		data[3] = str(numlik.findall(sock)[0])
		data[4] = str(numdislik.findall(sock)[0])
		data[5] = str(rat.findall(sock)[0])
		data[6] = str(cat.findall(sock)[0])
		return data

	except Exception:
		pass
