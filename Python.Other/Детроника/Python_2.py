from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        strIn = str().join(argv[1:])
    else:
        strIn = input('Введите строку> ')
    result = ''
    interResult = strIn.lower()
    for i in range(1,len(interResult)+1):
        result += interResult[-i]  
    result = result.upper()
    print('В итоге получили',result)