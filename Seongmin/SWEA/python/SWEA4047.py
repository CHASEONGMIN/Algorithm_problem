#SWEA 4047 영준이의 카드 카운팅
#딕셔너리 활용한 풀이 연습
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    card = input() #카드값 입력 받음
    card_dic = {    #카드 딕셔너리 생성
        'S': [],
        'D': [],
        'H': [],
        'C': [],
    }
    print('#{}'.format(tc), end=' ')


    for i in range(0, len(card), 3):  # 3글자 단위
        a = card[i] #카드의 무늬 값 T  (key)
        num = card[i + 1:i + 3] #카드의 숫자 값  (value)

        if num not in card_dic[a]:  # 카드 없으면 추가
            card_dic[a].append(num)
        else:  # 카드 있으면 에러출력하고 끝냄
            print('ERROR', end='')
            break
    else: #추가한 카드의 value값을 보여주기 위해 value
        for key, value in card_dic.items():
            print(13 - len(value), end=' ')  #숫자 13과 len(value)의 차이를 통해 없는 카드의 수 출력

    print()  # 다음출력값은 아래줄에 와야 하므로






    #dictionary에서 print(13 - len(value), end=' ') 이 표현 좋았음
