# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급(pay_of_hour)
# - 직원수(total_of_part_timers)

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(total_wage): 초기값은 0으로 고정

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

class PartTimer:
    pay_of_hour = 10000
    total_of_part_timers = 0

    def __init__(self, nickname, location='청담동'):
        self.nickname = nickname
        self.location = location
        self.total_wage = 0

    def calculate_wage(self, hour, bonus=0):
        self.total_wage += PartTimer.pay_of_hour * hour + bonus


ryan = PartTimer("라이언")
neo = PartTimer("네오", "제주도")

ryan.calculate_wage(3)
print(ryan.total_wage)

neo.calculate_wage(5, 30000)
print(neo.total_wage)
