from os import chdir




if __name__ == '__main__':
    chdir(r'C:\input_output_data')
    inputFile = open('inputFile_2.txt','r')
    number = int(inputFile.read())
    sumNum = sum([x for x in range(0,number + 1)])
    outputFile = open('outputFile_2.txt','w')
    outputFile.write(str(sumNum))
    outputFile.close()