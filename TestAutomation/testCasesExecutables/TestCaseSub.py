#!/usr/bin/env python

import os, sys

def testSub(x, y):

	#get Directory for functions
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
	currentworkingdirectory = (currentworkingdirectory + '/project/src')
	sys.path.insert(0, currentworkingdirectory)

	from functions import sub

	try:
		output = sub(int(x),int(y))
	except:
		output = "ERROR"
	
	return output

