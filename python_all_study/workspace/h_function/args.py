def getTotal(*datas):
    print(type(datas))
    total = 0
    for i in datas:
        total += i
    return total


result = getTotal(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

