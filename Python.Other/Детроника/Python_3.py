from sys import argv

if __name__ == '__main__':
    stringIn = input('Введем текс>')
    stringIn = stringIn.rstrip()
    sentence = [ item.strip() for item in stringIn.split('.') if item != '']
    wordsNum = 0
    for item in sentence:
        wordsNum += len(item.rstrip().split(' '))
    print('Число предложений = ',len(sentence),'; Число слов = ', wordsNum)
    
        