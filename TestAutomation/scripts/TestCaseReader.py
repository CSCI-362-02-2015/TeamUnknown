def testCaseExtractor(filename):
    f=open((filename +".txt"), 'r')
    file_contents=f.read()
    file_contents=file_contents.split("\n")
    userNumbers=file_contents[4].split(" ")
    contentLength=len(userNumbers)

    if(contentLength==2):
        firstNum=file_contents[1]
        return firstNum
    else:
        firstNum=file_contents[1]
        secondNum=file_contents[2]
        return firstNum, secondNum
        
    
    
    
