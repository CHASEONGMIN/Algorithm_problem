#SWEA 1216 회문2
import sys
sys.stdin = open('input.txt', 'r')

#오늘자 실습 4861 회문에서 가로와 세로가 같은 구성을 가진 것을 확인하였기에 회문 검사는 함수를 통하여 진행하게 짠다.
# 실습에서 슬라이싱을 활용하였으므로 다른 방법으로 시도(팰린드롬)
# point : 함수를 사용하기 위해 str2를 이용하여 세로를 가로 형태로만들어 주고 해결 함.

def palindrome(str): #회문 확인
    l = len(str)
    for i in range(l // 2):
        if str[i] != str[l - i - 1]:
            return False
    return True

T = 10
for tc in range(1, T + 1):
    input() #테스트 케이스의 번호
    length = 100
    str = [] #문자열들 리스트로 넣어주기 위해
    str2 = [] #세로를 가로로 만들기 위한 리스트
    N = 100

    for i in range(N): #str에 문자열들 리스트로 넣어줌
        str.append(input())
    for i in range(N): #세로를 str처럼 가로형태로 만들어서 str2에 저장
        str_temp = ''
        for k in range(N):
            str_temp += str[k][i]
        str2.append(str_temp)

    res = 0 #결과를 보여주기 위한  res
    for l in range(length, 0, -1): #길이와 비교
        if res >= l:
            break
        for i in range(N):
            if res == l:
                break
            for j in range(N - l + 1): #N - M + 1형태는 연습이 더 필요한듯.
                if palindrome(str[i][j:j + l]) or palindrome(str2[i][j:j + l]):
                    res = l
                    break

    print("#{} {}".format(tc, res))


    #아직 숙련도가 부족하여 참고를 하였음. 복습하며 체화 필요.