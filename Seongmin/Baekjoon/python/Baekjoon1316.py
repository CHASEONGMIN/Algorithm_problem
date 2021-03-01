#백준 1316 그룹 단어 체커 실5
#입력된 문자열을 검사하는데 특정 문자 다음에 다른 문자가 나올 경우
# 문자열에서 그 글자 다음부터 끝까지 검사하여 똑같은 문자가 있는지 검사 후 카운트
# 범위만 잘 지정해주면 끝

N = int(input())

res = 0

for i in range(N):
    str1 = input()
    for j in range(len(str1)):
        #인덱스를 0부터 해주기 위해 이렇게 한다.
        if j != len(str1)-1:
            if str1[j] == str1[j + 1]:
                pass
            elif str1[j] in str1[j + 1:]:
                break
        else:
            res += 1
print(res)