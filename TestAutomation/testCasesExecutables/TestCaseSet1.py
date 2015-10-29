#!/usr/bin/env python

import os, sys

currentworkingdirectory = os.getcwd()
currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
os.chdir(currentworkingdirectory)
currentworkingdirectory = (currentworkingdirectory + '/project/src')
os.chdir(currentworkingdirectory)

from functions import add

output = add(int(sys.argv[1]),int(sys.argv[2]))

print(output)
