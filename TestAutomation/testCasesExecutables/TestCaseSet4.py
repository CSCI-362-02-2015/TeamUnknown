#!/usr/bin/env python

import os, sys

#get Directory for functions
currentworkingdirectory = os.getcwd()
currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
currentworkingdirectory = (currentworkingdirectory + '/project/src')
sys.path.insert(0, currentworkingdirectory)

from functions import div

#get Directory for driver scripts
currentworkingdirectory = currentworkingdirectory.replace('/project/src', '')
currentworkingdirectory = (currentworkingdirectory + '/scripts')

sys.path.insert(0, currentworkingdirectory)

#from htmlConverter import writeFile
from outfile import intToText
from TestCaseReader import testCaseExtractor


#get file directory
currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
currentworkingdirectory = (currentworkingdirectory + '/testCases')

#create file pointers
inFile = currentworkingdirectory + "/" + "testCase" + sys.argv[1]


currentworkingdirectory = currentworkingdirectory.replace('/testCases', '/temp')

outFile = currentworkingdirectory + "/testCaseOutput" + sys.argv[1]


#get values from inputfile and divide
x,y = testCaseExtractor(inFile)
try:
	output = div(int(x),int(y))
except:
	output = "ERROR"

#writeFile(outFile, output)
intToText(outFile,output)


