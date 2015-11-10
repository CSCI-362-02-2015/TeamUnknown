def validator( oracleVal, actualVal):


	testVal = actualVal


	tempVal = oracleVal.split(" ")
	finalOracleVal = tempVal[2]
	if (finalOracleVal == testVal):
		return True
	else:
		return False

