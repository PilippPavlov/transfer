from os import chdir

if __name__ == '__main__':
    chdir(r'C:\input_output_data')
    numOne = open('inputFile_4.txt','r').read()
    numThre = 9 - int(numOne)
    numWhole = numOne + '9' + str(numThre)
    open('outputFile_4.txt','w').write(numWhole)