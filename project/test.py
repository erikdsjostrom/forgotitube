import fnmatch
import os

print(len(fnmatch.filter(os.listdir("./static/img"), '*')))
