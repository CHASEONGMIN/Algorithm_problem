#백준 1181 단어 정렬 실5
# set활용, 정렬을 위해 튜플형태가 만들어지는데 이를 리스트에 넣어주고 원하는 값만 꺼냄
# 익숙치 않은 문제

import sys

N = int(sys.stdin.readline())
arr = []
arr2 = []

for _ in range(N):
    arr.append(input())

arr_1 = list(set(arr)) # 중복 제거

for word in arr_1:  #튜플을 리스트에 추가
    arr2.append((len(word), word))

#정렬 진행
result = sorted(arr2)

for word_len, word in result:
    print(word)