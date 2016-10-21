from metrics import CoefficientPearson
from generatefeedparser import LoadData

class Nodal:
    def __init__(self,CounterWords,LeftNeighbor,RightNeighbor=None,id=None,Distance=0.0):
        self.CounterWords = CounterWords    #словарь, счктчик вхождения слов
        self.LeftNeighbor = LeftNeighbor    #левый сосед
        self.RightNeighbor = RightNeighbor  #правый сосед
        #self.Linck = Linck                 #ссылка
        self.id = id                        #идентификатор записи
        self.Distance = Distance            #Расстояние между соседями

def clustering():
    Data = LoadData()
    clusters = [Nodal(CounterWords=Data[item],LeftNeighbor=item, id = i) for item in Data for i in range(len(Data))] 
    while len(clusters) > 1:
        