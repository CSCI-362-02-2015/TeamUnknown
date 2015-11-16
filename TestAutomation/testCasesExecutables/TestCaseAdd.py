#!/usr/bin/env python

import os, sys

def testAdd(x, y):

	#get Directory for functions
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
	currentworkingdirectory = (currentworkingdirectory + '/project/src')
	sys.path.insert(0, currentworkingdirectory)

	from functions import add

	try:
		output = add(int(x),int(y))
	except:
		output = "ERROR"

	return output


