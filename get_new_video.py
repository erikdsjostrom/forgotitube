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


# usr_data är en lista med följande data inkl. datatyper
# 0: view count limit 		(int)
# 1: search query 			(string)
# 2: duration upper limit 	(int)
# 3: duration lower limit 	(int)
# 4: category 				(string)
# 5: avg rating upper limit (float)
# 6: avg rating lower limit (float)
# 7: likes upper limit 		(int)
# 8: likes lower limit 		(int)
# 9: dislikes upper limit 	(int)
# 10: dislikes lower limit 	(int)
def get_new_video(usr_data):
	while True:
		# Added a try/except for safety, when assigning stuff to avoid crashes.
		try:
			if not usr_data[1]:
				# Default query: random keyword
				randomid = get_random_id(random.choice(keywords))
				vid = Video(randomid, get_info(randomid))
			else:
				# Use the query input
				queryid = get_random_id(usr_data[1])
				vid = Video(queryid, get_info(queryid))
		except Exception:
			continue
		# Setting remaining values to default if they are empty strings
		# 0: view count limit (int)
		if not usr_data[0]:
			usr_data[0] = 50
		# 2: duration upper limit (int)
		if not usr_data[2]:
			usr_data[2] = float("inf")
		# 3: duration lower limit (int)
		if not usr_data[3]:
			usr_data[3] = 0
		# 4: category (string)
		if usr_data[4] != "any":
			# Replaces & with &amp; to match the get_info which takes strings from html
			usr_data[4] = usr_data[4].replace("&", "&amp;")
		# 5: avg rating upper limit (float)
		if not usr_data[5]:
			usr_data[5] = float("inf")
		# 6: avg rating lower limit (float)
		if not usr_data[6]:
			usr_data[6] = 0
		# 7: likes upper limit (int)
		if not usr_data[7]:
			usr_data[7] = float("inf")
		# 8: likes lower limit (int)
		if not usr_data[8]:
			usr_data[8] = 0
		# 9: dislikes upper limit (int)
		if not usr_data[9]:
			usr_data[9] = float("inf")
		# 10: dislikes lower limit (int)
		if not usr_data[10]:
			usr_data[10] = 0

		# Debugging
		# vid.show_info()

		# Filtering out the id if it does not meet all of the requirements
		# This is where the most time is wasted probably
		if any(f.lower() in vid.title.lower() for f in filtr):
			continue
		elif vid.viewcount > usr_data[0]:
			continue
		elif not usr_data[3] <= vid.duration <= usr_data[2]:
			# Did not match duration limits
			continue
		elif usr_data[4] != "any" and usr_data[4] != vid.category:
			print(usr_data[4])
			continue
		elif not usr_data[6] <= vid.rating <= usr_data[5]:
			continue
		elif not usr_data[8] <= vid.likes <= usr_data[7]:
			continue
		elif not usr_data[10] <= vid.dislikes <= usr_data[9]:
			continue
		# The id passed the filtering
		return vid.id
# This is for testing with default inputs
# print(get_new_video([""]*4 + ["any"] + [""]*6))
