#!/usr/bin/env python

import os, sys

from validator import validator

def createReport(numberTestCases):
	currentWorkingDirectory = os.getcwd()
	currentWorkingDirectory = currentWorkingDirectory.replace('/scripts', '')
	currentWorkingDirectory = currentWorkingDirectory + "/reports"
	sys.path.insert(0, currentWorkingDirectory)
	print(currentWorkingDirectory)
	report = open((currentWorkingDirectory + "/finalReport.html"), 'w+')
	report.write("<html> \n <body> \n")

	currentWorkingDirectory = currentWorkingDirectory.replace('/reports', '')

	for i in range(1, (numberTestCases+1)):
		report.write("<div> \n")
	
		currentWorkingDirectory = currentWorkingDirectory.replace('/temp', '')
		currentWorkingDirectory = currentWorkingDirectory + '/testCases'
		currentTestCase = currentWorkingDirectory + '/testCase' + str(i)

		testCaseProper = open((currentTestCase + '.txt'), 'r')
		testCaseContents = testCaseProper.read()
		testCaseContents = testCaseContents.replace('\n','<br>')
		report.write(testCaseContents)
	
		testCaseContents = testCaseContents.split('<br>')
		currentWorkingDirectory = currentWorkingDirectory.replace('/testCases', '/temp')
		
		testOutputProper = open((currentWorkingDirectory + '/testCaseOutput' + str(i) + '.txt'), 'r')
		testOutputContents = testOutputProper.read()
		report.write('Actual Outcome: ' + testOutputContents)
		isCorrect = validator(testCaseContents[5], testOutputContents)
		if(isCorrect):
			report.write('<br> Test Results: Passed')
		else:
			report.write('<br> Test Results: Failed')
		report.write('</div>')
	report.write("</body> \n </html>")
	report.close
