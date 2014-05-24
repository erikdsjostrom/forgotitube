#!/usr/bin/python
import random
from get_id import get_random_id
from get_id import get_info
from get_id import Video

global filtr
global keywords
with open("filter.txt") as fil:
	filtr = fil.read().splitlines()
with open("keywords.txt") as kw:
	keywords = kw.read().splitlines()

<<<<<<< HEAD
=======
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
				#vid.show_info()  # Kommentera denna rad för att sluta printa
			except TypeError:
				continue
			if title is None or title == [] or views is None or views == []:
				continue
			elif any(f.lower() in title[0].lower() for f in filter):
				continue
			elif views < limit:
				return tryid
>>>>>>> upstream/master

# user_data är en lista med följande data:
# NOTERA ATT ALLT ÄR STRÄNGAR
# 0: view count limit
# 1: search query
# 2: duration upper limit
# 3: duration lower limit
# 4: category
# 5: avg rating upper limit
# 6: avg rating lower limit
# 7: likes upper limit
# 8: likes lower limit
# 9: dislikes upper limit
# 10: dislikes lower limit
def get_new_video(user_data):
	while True:
		# Added a try/except for safety, when assigning stuff to avoid crashes.
		try:
			if not user_data[1]:
				# Default query: random keyword
				randomid = get_random_id(random.choice(keywords))
				vid = Video(randomid, get_info(randomid))
			else:
				# Use the query input
				queryid = get_random_id(user_data[1])
				vid = Video(queryid, get_info(queryid))
		except Exception:
			continue
		# Setting remaining values to default if they are empty strings
		# 0: view count limit
		if not user_data[0]:
			user_data[0] = 50
		else:
			user_data[0] = int(user_data[0])
		# 2: duration upper limit
		if not user_data[2]:
			user_data[2] = float("inf")
		# 3: duration lower limit
		if not user_data[3]:
			user_data[3] = 0
		# 4: category
		if user_data[4] != "any":
			# Replaces & with &amp; to match the get_info which takes strings from html
			user_data[4] = user_data[4].replace("&", "&amp;")
		# 5: avg rating upper limit
		if not user_data[5]:
			user_data[5] = float("inf")
		# 6: avg rating lower limit
		if not user_data[6]:
			user_data[6] = 0
		else:
			user_data[6] = int(user_data[6])
		# 7: likes upper limit
		if not user_data[7]:
			user_data[7] = float("inf")
		# 8: likes lower limit
		if not user_data[8]:
			user_data[8] = 0
		else:
			user_data[8] = int(user_data[8])
		# 9: dislikes upper limit
		if not user_data[9]:
			user_data[9] = float("inf")
		# 10: dislikes lower limit
		if not user_data[10]:
			user_data[10] = 0

		# Debugging
		# vid.show_info()

		# Filtering out the id if it does not meet all of the requirements
		# This is where the most time is wasted probably
		if any(f.lower() in vid.title.lower() for f in filtr):
			continue
		elif vid.viewcount > user_data[0]:
			continue
		elif not (user_data[3] <= vid.duration <= user_data[2]):
			# Did not match duration limits
			continue
		elif user_data[4] != "any" and user_data[4] != vid.category:
			print(user_data[4])
			continue
		elif not user_data[6] <= vid.rating <= user_data[5]:
			continue
		elif not user_data[8] <= vid.likes <= user_data[7]:
			continue
		elif not user_data[10] <= vid.dislikes <= user_data[9]:
			continue
		# The id passed the filtering
		return vid.id
# This is for testing with default inputs
# print(get_new_video([""]*4 + ["any"] + [""]*6))
