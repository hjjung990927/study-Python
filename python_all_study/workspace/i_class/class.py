class A:
    # static
    name = "A"

    def __init__(self, data=0):
        print(self)
        self.data = data

    def print_data(self):
        print(self.data)

object1 = A()
object2 = A(100)

print(object1)
print(object2)

print(A.name)

print(object1.data)
print(object2.data)

object1.print_data()
object2.print_data()





