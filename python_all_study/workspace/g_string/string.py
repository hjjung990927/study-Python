print(list("ABC"))

for i in "ABC":
    print(i)

print("Apple123!@#".upper())
print("Apple123!@#".lower())

data = "사과, 바나나, 파인애플, 포도, 복숭아"
print(data.split(", ", maxsplit=2))

print("A B C D E F".split())
print("A            B".split())
print("A     B".split(" "))

print(",".join(["a", "b", "c"]))

# replace('기존 값', '새로운 값')
print("A b C d".replace(" ", ""))
print("     AbCd     ".replace(" ", ""))
print("     AbCd     ".strip())

# find()
# print("ABC".index("Z"))
print("ABC".find("Z"))

# count('검색할 값')
print("fmdiosfnoeq2ionf0hdsnonv0c9xvclkmvp;wa-90jf9-13jpf".count("f"))

# 실습1. 아래 문자열을 189000 출력
s = "189,000 원"
print(s.replace(",","").strip().replace("원",""))

s = "189,000 원"
result = "".join(i for i in s if '0' <= i <= '9')
print(result)

