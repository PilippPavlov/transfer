from metrics import CoefficientPearson
from generatefeedparser import LoadData
from metrics import pearson

class Nodal:
    def __init__(self,CounterWords,LeftNeighbor,RightNeighbor=None,id=None,Distance=0.0):
        self.CounterWords = CounterWords    #словарь, счктчик вхождения слов
        self.LeftNeighbor = LeftNeighbor    #левый сосед
        self.RightNeighbor = RightNeighbor  #правый сосед
        #self.Linck = Linck                 #ссылка
        self.id = id                        #идентификатор записи
        self.Distance = Distance            #Расстояние между соседями

def clustering():
    savedDistance = {}
    Data = LoadData()
    clusters = [Nodal(CounterWords=Data[item],LeftNeighbor=item, id = i) for item in Data for i in range(len(Data))] 
    while len(clusters) > 1:
        lowestpair = (0,1)
        closest = person(clusters[0].CounterWords,clusters[1].CounterWords)
        for i in range(len(clusters)):
            for j in range(i + 1,len(clusters)):
                if (clusters[i].id,clusters[j]) not in savedDistance:
                    savedDistance[(clusters[i].id,clusters[j])] = person(clusters[i].CounterWords,clusters[j].CounterWords)
        
            distans = savedDistance[(clusters[i].id,clusters[j])]
        if distans < closest:
            lowestpair = (clusters[i].id,clusters[j])
            closest = distans
            
            
                    
        