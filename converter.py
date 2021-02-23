#!/usr/bin/env python
'''

CREATED BY GABRIEL CULLEN
https://github.com/GabrielCullen/


'''
#reads in a file of passwords that have been cracked, converts into a more basic format
#abCd12! becomes lluldds
import sys

def checkChar(char):

	if char.isdigit():
		return "d"

	if char.isupper():
		return "u"

	if char.islower():
		return "l"

	return "s"

# get arguments from command line
ifile = sys.argv[1]

# try to open file and create results array
results = []
f = open(ifile, 'r')
lines = f.readlines()
count = 0.00
total_size = 0
# create mask array and store result

for line in lines:
	parsed_data= []
	tidyline = line.replace('\r\n','').replace('\n','')
	for c in tidyline:
		parsed_data.append(checkChar(c))
	results.append("".join(parsed_data))
	count = count +1
	length = len(tidyline)
	total_size = total_size+length
file = sys.argv[2]
f = open(file, "w")


for each in results:
    f.write(str(each)+"\n")
f.close()
print("Converted " + str(count) + " lines to " + file)
print("Average password length - " + str(total_size/count))