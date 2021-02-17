res = []

for _ in range(10):
    n = int(input())
    r = n % 42
    res.append(r)

s = set(res)
print(len(s))

#set을 활용하여 중복 제거를 쉽게 해줌.