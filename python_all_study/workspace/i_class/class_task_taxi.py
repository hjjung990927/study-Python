# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의

class Taxi:
    init_fare = 5800
    init_distance = 2
    fare_per_km = 1000

    def calc_cost(self, money, distance):
        cost = Taxi.init_fare
        if distance > Taxi.init_distance:
            cost += (distance - Taxi.init_distance) * Taxi.fare_per_km

        return cost, money - cost


taxi = Taxi()
# cost, rest = taxi.calc_cost(20000, 1)
cost, rest = taxi.calc_cost(20000, 10)
print(f"요금: {cost}, 잔돈: {rest}")









