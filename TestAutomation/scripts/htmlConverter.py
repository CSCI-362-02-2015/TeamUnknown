import os, sys
from random import *

currentworkingdirectory = os.getcwd()
currentworkingdirectory = currentworkingdirectory.replace('\\scripts', '')
currentworkingdirectory = currentworkingdirectory + "\\testReports"
os.chdir(currentworkingdirectory)
print(os.getcwd())
def writeFile(testFileName, num):
    
    
    htmlFileName = testFileName + ".html"
    f = open("foo.txt", 'a') 
    f.write("fuckerooni")      
        


    htmlFileName.close()

def main():
    writeFile("testfoo", 6)
#    

