animals = ['dog', 'cat', 'rabbit', 'fish']
print(animals)

# 인덱스로 접근
print(animals[1])
print(animals[2])

print(animals[-1])
print(animals[-2])

print(len(animals))

print("-" * 50)
print("정희준" + str(3))

animals.append("hamster")
print(animals)

animals.append("dog")
print(animals)

del animals[0]
print(animals)

animals.remove('hamster')
print(animals)

index = animals.index('fish')
print(index)

print(animals * 2)