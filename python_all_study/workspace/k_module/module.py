# import calc
#
# result = calc.add(1, 2)
# print(result)

# from calc import *
#
# result = add(1, 2)
# print(result)

# import calc as c
#
# result = c.add(3, 5)
# print(result)

# import calc as c
# calc = c.Calculator(3, 2)
# print(calc.subtract())

from calc import Calculator

calc = Calculator(10, 5)
result = calc.subtract()
print(result)



