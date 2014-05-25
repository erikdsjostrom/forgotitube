with open("get_new_video.py") as fp:
	for i, line in enumerate(fp):
		if "\xe3" in line:
			print(i, repr(line))
