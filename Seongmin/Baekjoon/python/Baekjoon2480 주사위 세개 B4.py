#백준 2480 주사위 세개 B4
# 간결한 풀이법이 중요
# 정렬을 진행해주고 SET으로 중복을 제거해주는 방법
# 같은 수가 두개일 때 = 중간 값이 두개 있는 거임을 이용.

num = sorted(list(map(int, input().split())))

if len(set(num)) == 1:
    print(10000 + num[0] * 1000)
elif len(set(num)) == 2:
    print(1000 + num[1] * 100)
else:
    print(num[2] * 100)