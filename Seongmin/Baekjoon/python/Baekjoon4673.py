# 셀프 넘버 브1
# 셀프 넘버 처리를 하는 함수를 만들고
# 주어진 범위 (~ 10001)안에서 함수를 돌린다.

# Key : 함수에서 리스트를 활용한 것은 이후에 출력할 때 for문으로 arr을 돌릴 때 문자열이라면 int와의 비교가 힘들어서 그럼

def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x)
    return int(n) + a

arr = []
for i in range(1,10001):
    k = d(i)
    arr.append(k)

for b in range(1, 10001):
    if b in arr:
        pass
    else:
        print(b)
