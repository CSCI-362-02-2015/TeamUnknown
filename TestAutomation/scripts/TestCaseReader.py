def testCaseExtractor(filename):
    f=open((filename +".txt"), 'r')
    file_contents=f.read()
    file_contents=file_contents.split()
    firstNum=int(file_contents[0])
    if(file_contents[1]!=null):
        secondNum=int(file_conents[1])
        return {firstNum, secondNum}
    else:
        return {firstNum}
    
