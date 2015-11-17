#!/usr/bin/env python

import os, sys

from validator import validator

def createReport(numberTestCases):
	
	lineheaders = ["TestId: ", "Requirement: ", "Component: ", "Method: ", "Input: ", "Expected Outcome: ", "Actual Outcome: ", "Test Results: "]
	
	currentWorkingDirectory = os.getcwd()
	currentWorkingDirectory = currentWorkingDirectory.replace('/scripts', '')
	currentWorkingDirectory = currentWorkingDirectory + "/reports"
	sys.path.insert(0, currentWorkingDirectory)
	print(currentWorkingDirectory)
	fileURL = currentWorkingDirectory + "/finalReport.html"
	report = open((fileURL), 'w+')
	report.write('<html> \n <table border="1" style="width:100%"> \n')
	
	report.write("<tr> \n")
	for h in range(0, 8):
		report.write("<td>" + lineheaders[h] + "</td> \n")
	report.write("</tr> \n")

	currentWorkingDirectory = currentWorkingDirectory.replace('/reports', '')

	for i in range(1, (numberTestCases+1)):
		report.write("<tr> \n")
	
		currentWorkingDirectory = currentWorkingDirectory.replace('/temp', '')
		currentWorkingDirectory = currentWorkingDirectory + '/testCases'
		currentTestCase = currentWorkingDirectory + '/testCase' + str(i)

		testCaseProper = open((currentTestCase + '.txt'), 'r')
		testCaseContents = testCaseProper.read()
		testCaseContents = testCaseContents.split('\n')
		
		for j in range(0, 6):
			report.write('<td>' + testCaseContents[j].replace(lineheaders[j], '') + '</td> \n')

		currentWorkingDirectory = currentWorkingDirectory.replace('/testCases', '/temp')
		
		testOutputProper = open((currentWorkingDirectory + '/testCaseOutput' + str(i) + '.txt'), 'r')
		testOutputContents = testOutputProper.read()
		report.write('<td>' + testOutputContents + '</td> \n')
		isCorrect = validator(testCaseContents[5], testOutputContents)
		if(isCorrect):
			report.write('<td>Passed</td> \n')
		else:
			report.write('<td>Failed</td> \n')
		report.write('</tr> \n')
	report.write("</table> \n </html>")
	report.close
	return (fileURL)
