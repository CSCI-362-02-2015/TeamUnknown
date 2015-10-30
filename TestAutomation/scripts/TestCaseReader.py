def testCaseExtractor(filename):
    f=open((filename +".txt"), 'r')
    file_contents=f.read()
    file_contents=file_contents.split()
    contentLength=len(file_contents)
    if(contentLength==1):
        firstNum=file_contents[0]
        return {firstNum}
    else:
        firstNum=file_contents[0]
        secondNum=file_contents[1]
        return {firstNum, secondNum}
        
    
    
    
