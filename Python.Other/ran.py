import os

class UniformBaseGenerate:
    def __init__(self,factor,incriment,module,primary):
        self.factor = factor
        self.incriment = incriment
        self.module = module
        self.previous = primary
    def getValue(self):
        self.previous = (self.factor * self.previous + self.incriment) % self.module
        return (self.previous + 1) / (self.module + 1)
        
if __name__ == '__main__':
    os.chdir(r'C:\git-progect\Python.Other')
    file = open('OutRand.txt','w')
    fileString = ''
    test = UniformBaseGenerate(1220703125,7,2**31 - 1,7)
    for index in range(0,200):
        item = test.getValue()
        fileString += str(item) + '\n'
    file.write(fileString)
    file.close()
    