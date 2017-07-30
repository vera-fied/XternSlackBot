#!/usr/bin/env python

import sys

input = sys.argv[1]
output = ""
flag = False

for x in range(0,len(input)-1):
	if flag and input[x] != ':':
		continue
	elif flag and input[x] == ':':
		flag = False
		continue
	elif input[x] == ':':
		flag=True
		if input[x+1] == 's' and input[x+2] == 'c':
			if input[x+10] == 'b' and input[x+11] == 'l':
				output+=' '
			else:
				output+=input[x+10]
		elif input[x+1] == 's' and input[x+2] == 'p':
			output+=' '
		else:
			output+=input[x+1]
print(output)
