# 파이썬은 빠른 for문 밖에 없다.
# print(list(range(1, 10, 1)))

# for i in range(1, 10, 1):
#     print(i)

# default
# start = 0, step = 1
# for i in range(0, 10, 1):
# for i in range(0, 10):
# for i in range(10):
#     print(i, end=" ")

# 실습1. 100~1까지 출력
# for i in range(100):
#     print(100 - i)

# 실습2. 1~15까지 출력
# for i in range(15):
#     print(i + 1)

# 실습3. 30~1까지 출력
# for i in range(30):
#     print(30 - i)

# 실습4. 1~100까지 중 홀수만 출력
# for i in range(50):
#     print(i * 2 + 1)

# 실습5. 1~10까지 합 출력
# total = 0
# for i in range(10):
#     total += i + 1
#
# print(total)

# 실습6. 1~n까지 합 출력
# n = 100
# total = 0
#
# for i in range(n):
#     total += i + 1
#
# print(total)

# 실습7. 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(12):
#     print(i % 4 + 3, end=" ")
