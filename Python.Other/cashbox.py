import os
class Date:
    def __init__(self,beginH,beginM,endH,endM):
        self.begin = beginH + beginM / 60
        self.end = endH + endM / 60
        self.workingHours = self.end - self.begin

        
def loadData(path='C:\git-progect\Python.Other',fileName='input.txt'):
    os.chdir('C:\git-progect\Python.Other')
    loads = []
    duration = []
    fileDesc = open(fileName,'r')
    for record in fileDesc.readlines():
        loads.append(record)
    number = int(loads[0])
    del loads[0]
    for item in loads:
        listH = item.split(' ')
        duration.append(Date(int(listH[0]),int(listH[1]),int(listH[2]),int(listH[3])))
    maxBegin = 0
    minEnd = 1000000
    for item in duration:
        if item.begin > maxBegin:
            maxBegin = item.begin
        if item.end < minEnd:
            minEnd = item.end
        if minEnd < maxBegin:
            result = 0
        else:
            result = ( minEnd - maxBegin)*60
    open('output.txt','w').write(str(result))
    
    
    
    
    
if __name__ == '__main__':

    loadData()
