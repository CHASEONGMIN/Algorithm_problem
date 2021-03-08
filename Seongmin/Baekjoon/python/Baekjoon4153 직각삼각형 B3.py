#백준 4153 직각삼각형 B3
#리스트 활용

while True:
    arr = list(map(int, input().split()))
    m_arr = max(arr)
    if m_arr == 0:
        break #가장 큰수가 0이면 0 0 0

    arr.remove(m_arr)

    if arr[0] ** 2 + arr[1] ** 2 == m_arr ** 2:
        print('right')
    else:
        print('wrong')

