#!/usr/bin/python
import random
import urllib
import urllib.request
import re
#import os


def main():
	with open("keywords.txt") as kw:
		keywords = kw.read().splitlines()
	return view_limit(50, keywords)
	# url = 'https://www.youtube.com/watch?v=' + str(id)
	# playable_url = 'mpv ' + url + ' --fs'
	# os.system(playable_url)


def view_limit(limit, keywords):
	filter = ["How to say", "How to spell", "How to pronounce"]
	views = 1
	while views > 0:
		randkeyword = random.choice(keywords)
		validids = get_id(randkeyword)
		if len(validids) == 0:
			continue
		tryid = random.choice(validids)
		url = 'http://gdata.youtube.com/feeds/api/videos/' + tryid
		title, views = test_connection(url)
		if title is None or title == []:
			continue
		elif any(f.lower() in title[0].lower() for f in filter):
			continue
		elif views < limit:
			return tryid


# Tries connection and returns view count (if the id is valid)
def test_connection(url):
	try:
		sock = urllib.request.urlopen(url).read().decode("utf-8")
		titlepatt = re.compile("<title[^>]*>(.*?)</title>")
		viewpatt = re.compile("viewCount='(.*?)'/>")
		title = titlepatt.findall(sock)
		views = viewpatt.findall(sock)
		if views == [] or views is None:
			return(title, 0)
		else:
			return(title, int(views[0]))
	except Exception:
		pass


def get_id(searchquery):
	gdataurl = "http://gdata.youtube.com/feeds/api/videos?q="
	try:
		sock = urllib.request.urlopen(gdataurl + searchquery).read().decode("utf-8")
		idatt = re.compile("/v/(.*?)\?")
		foundid = idatt.findall(sock)
		return foundid
	except Exception:
		pass

if __name__ == '__main__':
	print(main())
