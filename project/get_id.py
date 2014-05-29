#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import urllib
import urllib.request
import urllib.parse
import re
# import sys


class Video():
	def __init__(self, id, list):
		self.id = id
		self.viewcount = int(list[0])
		self.title = list[1]
		self.duration = int(list[2])
		self.category = list[3].replace("&amp; ", "& ")

	def show_info(self):
		print([self.id, self.viewcount, self.title,
								self.duration,
								self.category])


def get_random_id(searchquery):
	# This line right here, encodes the url in utf-8 (so it can be read by urlopen etc)
	searchquery = urllib.parse.quote_plus(searchquery.encode("utf-8"))
	gdataurl = "http://gdata.youtube.com/feeds/api/videos?q=" + searchquery + "&orderby=published&key=AIzaSyB533JS4sNHgWm8Obc7NS6bfBiD6v7Coow"
	#try:
	sock = urllib.request.urlopen(gdataurl).read().decode("utf-8")
	#sys.stdout.buffer.write(sock.encode("utf-8"))
	idatt = re.compile("/watch\?v=(.*?)&")
	foundid = idatt.findall(sock)
	if not foundid:
		return None
	return random.choice(foundid)
	#except Exception:
		# print("get_random_id error:")
		# print(e)
	#	pass


# get_info takes an id and returns a list with the following things
# 0: view count, 1: title, 2: duration (sec), 3: category
def get_info(id):
	id = urllib.parse.quote_plus(id.encode("utf-8"))
	url = "https://gdata.youtube.com/feeds/api/videos/" + str(id) + "?v=2"
	try:
		sock = urllib.request.urlopen(url).read().decode("utf-8")
		vc = re.compile("viewCount='(.*?)\'")
		dur = re.compile("duration='(.*?)\'")
		cat = re.compile("category label='(.*?)\'")
		title = re.compile("<title>(.*?)</title>")
		data = [""]*7
		data[0] = str(vc.findall(sock)[0])
		data[1] = str(title.findall(sock)[0])
		data[2] = str(dur.findall(sock)[0])
		data[3] = str(cat.findall(sock)[0])
		return data

	except Exception:
		# print("get_info error:")
		# print(h)
		pass
