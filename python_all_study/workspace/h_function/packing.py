# packing과 unpacking
# 함수 선언 시 가변인자로 묶어서 받을 것인지(packing)
# 함수 사용 시 풀어서 전달할 것인지(unpacking)를 선택할 수 있다.

# packing
# 매개변수: *args(가변인자)
# 사용 시: a, b, c

# unpacking
# 매개변수: a, b, c
# 사용 시: (*datas)

def sub(*numbers):
    total = 0
    for number in numbers:
        total -= number

    return total


numbers = 1, 2, 3
sub(*numbers)


# n개 정수의 합
# 매개변수의 개수는 알 수 없다.
# 가변인자는 Tuple 타입이며, 전달할 때에는 ,로 여러 개의 값을 전달할 수 있다.
def get_total(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total


numbers = range(1, 11)
result = get_total(*numbers)
print(result)


# 국어, 영어, 수학 점수를 전달받은 뒤 총점을 출력하는 함수
# packing
def get_total_score(*scores):
    total = 0
    for score in scores:
        total += score

    print(total)


scores = [10, 50, 90]
# unpacking
get_total_score(*scores)


# 문자열에서 'A'가 몇 개 있는지 검사하는 함수
def find_A(*string):
    count = 0
    for i in string:
        if i == 'A':
            count += 1

    print(count)


string = "ABABABABDDDDACAXseoakcfmbid"
find_A(*string)











