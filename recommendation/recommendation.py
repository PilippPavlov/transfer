from criticism import critcs
from math import pow,sqrt
def similarity(dictcritics,person1,person2):
    simty = {}
    for item in dictcritics[person1]:
        if item in dictcritics[person2]:
            simty[item] = 1
    if len(simty) == 0:
        return 0
    distance = sum([pow(dictcritics[person1][item] - dictcritics[person2][item],2) for item in dictcritics[person1] if item in dictcritics[person2]])
    return round(1/ (1 + sqrt(distance)),2)

def PearsonCorrelation(dictcritics,person1,person2):  
    identical = {}
    for item in dictcritics[person1]:
        if item in dictcritics[person2]:
            identical[item] = 1
    if len(identical) == 0:
        return 0
    TNoR = len(identical) # total number of records 
    sum_composition = sum([dictcritics[person1][item]*dictcritics[person2][item] for item in dictcritics[person1] if item in identical])
    sum_componet1 = sum([dictcritics[person1][item] for item in dictcritics[person1] if item in identical])
    sum_componet2 = sum([dictcritics[person2][item] for item in dictcritics[person2] if item in identical])
    sum_componet1_pow = sum([pow(dictcritics[person1][item],2) for item in dictcritics[person1] if item in identical])
    sum_componet2_pow = sum([pow(dictcritics[person2][item],2) for item in dictcritics[person2] if item in identical])
    numerator = sum_composition - sum_componet1*sum_componet2 / TNoR
    denominator = sqrt((sum_componet1_pow - pow(sum_componet1,2) / TNoR )*(sum_componet2_pow - pow(sum_componet2,2) / TNoR))
    if denominator == 0:
        return 0
    return round(numerator / denominator,2)

def CityBlock(dictcritics,person1,person2):
    identical = {}
    for item in dictcritics[person1]:
        if item in dictcritics[person2]:
            identical[item] = 1
    if len(identical) == 0:
        return 0
    cityblock = sum([abs(dictcritics[person1][item] - dictcritics[person2][item]) for item in dictcritics[person1] if item in identical])
    return round(1 / (1 + cityblock),2)

def Jacquard(dictcritics,person1,person2):
    identical = {}
    for item in dictcritics[person1]:
        if item in dictcritics[person2]:
            identical[item] = 1
    denominator = len(dictcritics[person1]) + len(dictcritics[person2]) - len(identical)
    if denominator == 0:
        return 0
    return round(len(identical) / denominator, 2)
    
def recommend(dictcritics,logic=similarity):
    listperson = list(dictcritics.keys()).copy()
    vapor = {}
    vaporlist = []
    for person1 in dictcritics:
        listperson.remove(person1)
        vaporperson = []
        vaporsimilarty = []
        for person2 in listperson:
            vaporperson.append(person1 + ' and ' + person2)
            vaporsimilarty.append(logic(dictcritics,person1,person2))
        vapordict = {k:v  for (k,v) in zip(vaporperson,vaporsimilarty)}
        vaporlist.append(vapordict)
        if vapordict == {}:
            break 
        maxkey, maxsimilarity= None, 0
        for persons in vapordict:
            if vapordict[persons] > maxsimilarity and persons != maxkey:
                maxkey, maxsimilarity = persons, vapordict[persons]
        vapor[maxkey] = maxsimilarity
    return vapor,vaporlist

def Ranging(dictcritics,person,limit=5,logic=similarity):
    rang = [(logic(dictcritics,person,other),other) for other in dictcritics if other != person]
    rang.sort()
    rang.reverse()
    return rang[0:limit]

def getRecommendation(dictcritics,person,logic=PearsonCorrelation):
    totals = {}
    simSums = {}
    for other in dictcritics:
        if other == person:
            continue
        sim = logic(dictcritics,person,other)
        if sim <= 0:
            continue
        for item in dictcritics[other]:
            if item not in dictcritics[person] or dictcritics[person][item] == 0:
                totals.setdefault(item,0)
                totals[item] += dictcritics[other][item] * sim
                simSums.setdefault(item,0)
                simSums[item] += sim
    ranking = [(round(total/simSums[item],2),item) for item,total in totals.items()]
    ranking.sort()
    ranking.reverse()
    return ranking

def transformData(dictcritics):
    transform = {}
    for person in dictcritics:
        for item in dictcritics[person]:
            transform.setdefault(item,{})
            transform[item][person] = dictcritics[person][item]
    return transform
if __name__ == '__main__':
    #print(Ranging(critcs,'Toby'))
    #print(getRecommendation(critcs,'Toby'))
    data = transformData(critcs)
    print(Ranging(data,'The Night Listener'))
    #a1 = similarity(critcs,'Lusa Rose','Mick Lasalle')
    #b1 = similarity(critcs,'Jack Matthews','Toby')
    #print(a1,b1)
    #c1,d1 = recommend(critcs)    
    #c2,d2 = recommend(critcs,PearsonCorrelation)
    #c3,d3 = recommend(critcs,CityBlock)
    #c4,d4 = recommend(critcs,Jacquard)
    #for i in range(len(d1)):
    #    for item in d1[i]:
    #        line = 'Vapor: %s,Sim=%.2f,Pea=%.2f,City=%.2f,Jac=%.2f' %(item,d1[i][item],d2[i][item],d3[i][item],d4[i][item])
    #        print(line)
    