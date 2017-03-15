import os
import matplotlib.pyplot as plt
import numpy as np
import random
def load(path,name):
    os.chdir(path)
    file = open(name,'r')
    dateStr = file.read()
    dateStr = dateStr.strip()
    dataList = dateStr.split('\n')
    return dataList

    
if __name__ == '__main__':
    dateList = load(r'C:\git-progect\Python.Other','OutRand.txt')
    countDict = {}
    actualList = []
    for item1 in dateList:
        itemCount = 0
        for item2 in dateList:
            if(item2 == item1):
                itemCount += 1
        countDict.setdefault(item1,itemCount)
    for item in dateList:
        actualList.append(float(item))
    test = [random.random() for i in range(2000)]
    plt.hist(actualList,25)
    plt.show()