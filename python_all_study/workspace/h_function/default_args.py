# 두 정수 혹은 세 정수의 합
# def add(number1, number2, number3=0):
#     return number1 + number2 + number3
#
#
# result = add(10, 20, 30)
# print(result)
#
# result = add(10, 20)
# print(result)

from functools import singledispatch


@singledispatch
def printData(value):
    print(f"기본 출력: {value}")


@printData.register(int)
def _(value):
    print(f"정수 출력: {value}")


@printData.register(str)
def _(value):
    print(f"문자열 출력: {value}")


printData("안녕!")
printData(10)


def logger(func):
    def proxy(*args, **kwargs):
        print(f"함수 실행")
        print(f"매개변수: {args}")
        result = func(*args, **kwargs)
        print(f"함수 종료")
        return result
    return proxy


@logger
def add(number1, number2):
    return number1 + number2


result = add(10, 20)
print(result)











