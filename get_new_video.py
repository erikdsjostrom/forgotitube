#!/usr/bin/python
import random
from get_id import get_random_id
from get_id import get_info
from get_id import Video


def get_new_video():
	def view_limit(limit, keywords):
		with open("filter.txt") as fil:
			filter = fil.read().splitlines()
		while True:
			randkeyword = random.choice(keywords)
			tryid = get_random_id(randkeyword)
			try:
				info = get_info(tryid)
				vid = Video(tryid, info)
				title = vid.title
				views = vid.viewcount
				vid.show_info()  # Ta bort denna rad för att sluta printa
			except TypeError:
				continue
			if title is None or title == [] or views is None or views == []:
				continue
			elif any(f.lower() in title[0].lower() for f in filter):
				continue
			elif views < limit:
				return tryid

	with open("keywords.txt") as kw:
		keywords = kw.read().splitlines()
	return view_limit(50, keywords)
get_new_video()
