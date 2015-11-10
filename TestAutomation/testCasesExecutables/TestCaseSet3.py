#!/usr/bin/env python

import os, sys

#get Directory for functions
currentworkingdirectory = os.getcwd()
currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
os.chdir(currentworkingdirectory)
currentworkingdirectory = (currentworkingdirectory + '/project/src')
os.chdir(currentworkingdirectory)
sys.path.insert(0, currentworkingdirectory)

from functions import sub

#get Directory for driver scripts
currentworkingdirectory = currentworkingdirectory.replace('/project/src', '')
currentworkingdirectory = (currentworkingdirectory + '/scripts')

sys.path.insert(0, currentworkingdirectory)

#from htmlConverter import writeFile
from TestCaseReader import testCaseExtractor

#get file directory
currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
currentworkingdirectory = (currentworkingdirectory + '/testCases')

#create file pointers
inFile = currentworkingdirectory + "/" + "testCase" + sys.argv[1]
print(inFile)
outFile = "testCaseOutput" + sys.argv[1]
print(outFile)

#get values from inputfile and add
x,y = testCaseExtractor(inFile)
output = sub(int(x),int(y))

#writeFile(outFile, output)

print(output)
