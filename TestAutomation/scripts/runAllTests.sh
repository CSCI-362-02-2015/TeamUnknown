#!/bin/bash
cd ..
for i in 1 2 3 4 5;
do
	python ./testCasesExecutables/TestCaseSet1.py $i 
done
for i in 6 7 8 9 10;
do
	python ./testCasesExecutables/TestCaseSet2.py $i
done
for i in 11 12 13 14 15;
do
	python ./testCasesExecutables/TestCaseSet3.py $i
done
for i in 16 17 18 19 20;
do
	python ./testCasesExecutables/TestCaseSet4.py $i
done
for i in 21 22 23 24 25;
do
	python ./testCasesExecutables/TestCaseSet5.py $i
done

python ./scripts/finalReportCreator.py
