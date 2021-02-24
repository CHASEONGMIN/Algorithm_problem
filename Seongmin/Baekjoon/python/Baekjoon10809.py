#백준 10809 알파벳 찾기 브2
#중요 자주 쓰이는 것

#문자열 입력
str = list(map(str, input()))

#알파벳 리스트
str_a = list('abcdefghijklmnopqrstuvwxyz')

#알파벳 길이만큼 array에 -1
arr = [-1 for i in range(len(str_a))]

for i in range(len(str)):
    # 알파벳 리스트의 인덱스와 문자열 인덱스가 같으면 i
    if arr[str_a.index(str[i])] == -1:
        arr[str_a.index(str[i])] = i
for j in arr:
    print(j, end=" ")

#다른 풀이  내장함수 활용의 끝
# print(*map(input().find,map(chr,range(97,123))),sep=" ")