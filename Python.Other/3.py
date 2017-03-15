from os import chdir
from math import pow
if __name__ == '__main__':
    chdir(r'C:\input_output_data')
    num = int(open('inputFile_3.txt','r').read())
    numPow = pow(num,2)
    file = open('outputFile_3.txt','w').write(str(numPow))
    #реши на си