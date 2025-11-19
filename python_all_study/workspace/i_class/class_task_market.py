# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(f"name: {self.name}, price: {self.price}")


# 손님
# 이름, 나이, 할인율, 잔액
class Customer:
    def __init__(self, name, age, discount, money):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money


# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
class Market:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    def sell(self, customer):
        discount_price = self.product.price - (self.product.price * customer.discount * 0.01)
        customer.money -= discount_price
        self.stock -= 1


potato = Product('potato', 2000)
market = Market(potato, 50)
han = Customer('정희준', 27, 50, 40000)

market.sell(han)
print(han.money)
print(market.stock)



















