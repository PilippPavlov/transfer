if __name__ == '__main__':
    dateStr = input('Введите число >')
    if len(dateStr) > 1:
        sum = 0
        composition = 1
        for num in dateStr:
            sum += int(num)
            composition *= int(num)
    else:
        sum = int(dateStr)
        composition = int(dateStr)
    print('Сумма = ',sum,' Произведение = ',composition)