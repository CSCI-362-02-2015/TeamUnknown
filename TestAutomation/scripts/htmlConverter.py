#!/usr/bin/env python


import os, sys
from random import *
import webbrowser, os.path


currentworkingdirectory = os.getcwd()
currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
currentworkingdirectory = currentworkingdirectory + "/testReports"
os.chdir(currentworkingdirectory)
print(os.getcwd())
def writeFile(testFileName, num):
    
    
    htmlFileName = testFileName + ".html"
    f = open("foo.txt", 'w') 
    f.write("does this work")      
        


    htmlFileName.close()

def main():
    writeFile("testfoo", 6)
print ''' content type: text/html
<html>
<body>
<head>
<title> This is the title </title>
</head>
this is a body
</body>
</html>
'''

#    

