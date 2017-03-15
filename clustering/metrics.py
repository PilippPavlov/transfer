from math import pow,sqrt

def pearson(expressionOne,expressionTwo):
    semple = {}
    for item in expressionOne:
        if item in expressionTwo:
            semple.defult(item)
            semple[item] = 1
    
    lenSemple = len(semple)
    
    sumOne = sum([expressionOne[item] for item in expressionOne if item in expressionTwo])
    sumTwo = sum([expressionTwo[item] for item in expressionTwo if item in expressionOne])
    
    sumSqurOne = sum([pow(expressionOne[item],2) for item in expressionOne if item in expressionTwo])
    sumSqurTwo = sum([pow(expressionTwo[item],2) for item in expressionTwo if item in expressionOne])
    
    sumComposition = sum([expressionOne[item]*expressionTwo[item] for item in semple])
    
    numerator = sumComposition - (sumOne * sumTwo / lenSemple)
    denominator = sqrt((sumSqurOne - pow(sumOne,2) / lenSemple)*(sumSqurTwo - pow(sumTwo,2) / lenSemple))
    
    if denominator == 0:
        return 0
    else:
        return round(numerator / denominator, 4)