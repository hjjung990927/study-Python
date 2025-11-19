# # mutable: 변할 수 있는
# datas1 = [1, 2, 3, 4]
# datas2 = datas1
#
# print(datas1 is datas2)
#
# datas2.append(5)
# print(datas1)

 # immutable: 변할 수 없는
datas1 = 1, 2, 3, 4
datas2 = datas1

print(datas1 is datas2)
datas1 += (5, 6)
print(datas1)
print(datas2)
print(datas1 is datas2)