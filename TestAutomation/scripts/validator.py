def validator( oracleVal, actualVal):


	testVal = actualVal


	tempVal = oracleVal.split(" ")
	finalOracleVal = int(tempVal[2])

	if (oracleVal == testVal):
		return True
	else:
		return False

