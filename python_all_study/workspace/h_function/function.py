# 실습1. 두 정수의 합
# def add(number1, number2):
#     return number1 + number2
#
# number1 = 10
# number2 = 20
# result = add(number1, number2)
# print(result)

# 실습2. 두 정수의 나눗셈 후 몫과 나머지 리턴
def oper1(number1, number2):
    return number1 // number2

def oper2(number1, number2):
    return number1 % number2

number1 = 5
number2 = 2
result1 = oper1(number1, number2)
result2 = oper2(number1, number2)
print(result1, result2)

# 실습2. 강사님 코드
def div(number1, number2):
    return number1 // number2, number1 % number2

number1, number2 = 10, 3

value, rest = div(number1, number2)
print(f'몫: {value}, 나머지: {rest}')
