#!/usr/bin/env python

import os, sys

currentworkingdirectory = os.getcwd()
currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
os.chdir(currentworkingdirectory)
currentworkingdirectory = (currentworkingdirectory + '/project/src')
os.chdir(currentworkingdirectory)
sys.path.insert(0, currentworkingdirectory)

from functions import add

currentworkingdirectory = currentworkingdirectory.replace('/project/src', '')
currentworkingdirectory = (currentworkingdirectory + '/scripts')

sys.path.insert(0, currentworkingdirectory)

#from htmlConverter import writeFile
#from filereader import reader

inFile = "testCaseInput" + sys.argv[1]
print(inFile)
outFile = "testCaseOutput" + sys.argv[1]
print(outFile)
#x,y = reader(inFile)
output = add(4,5)

#writeFile(outFile, output)

print(output)
