def introduce(**info):
    print(type(info))
    for key, value in info.items():
        print(f"{key} = {value}")


# introduce(name='정희준', age=27)
info = {"name": "정희준", "age": 27}
introduce(**info)

def print_info(*, name, email):
    print(name, email)

info = {"name": "정희준", "email": "test@test.com"}
print_info(**info)
# print_info(name='정희준', email='test@test.com')


# 국어, 영어, 수학 점수의 평균 구하기
def get_average(**scores):
    kor = scores.get('kor')
    eng = scores.get('eng')
    math = scores.get('math')

    total = kor + eng + math
    average = total / len(scores)
    return average


scores = {'kor': 100, 'eng': 90, 'math': 80}
average = get_average(**scores)
print(average)


# 회원의 주문 금액들(pays)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# def use_coupon(*pays, **kwargs):
#     # result = [pay for pay in pays]
#     result = list(pays)
#
#     if kwargs.get('count') >= len(pays):
#         for i in range(len(pays)):
#             result[i] *= 1 - (kwargs.get('coupon') * 0.01)
#     else:
#         for i in range(kwargs.get('count')):
#             result[i] *= 1 - (kwargs.get('coupon') * 0.01)
#
#     return result

def use_coupon(*pays, **kwargs):
    result = [int(pays[i] * (1 - (kwargs.get('coupon') * 0.01)))
            for i in range(len(pays) if kwargs.get('count') >= len(pays) else kwargs.get('count'))]
    rest = []
    start = len(pays) - len(result)
    if start > 0:
        for i in range(start):
            print(pays[i + len(result)])
            rest.append(pays[i + len(result)])
    return result + rest

pays = [1000, 2000, 3000, 4000]
coupon_dict = {"coupon": 40, "count": 1}
result = use_coupon(*pays, **coupon_dict)
print(result)

