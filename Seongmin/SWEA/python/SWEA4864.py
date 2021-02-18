#SWEA 4864 문자열 비교
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print("#%d %d" %(tc,1))
    else :
        print("#%d %d" %(tc,0))



