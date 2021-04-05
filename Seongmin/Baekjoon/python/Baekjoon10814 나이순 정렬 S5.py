#백준 10814 나이순 정렬 S5
#딕셔너리 활용 좀 더 연습 필요. 복습 필수

N = int(input())
dic = {}

for i in range(N):
    [age, name] = map(str, input().split()) #문자열 있으니 str형으로 map해주어 입력받음

    if int(age) not in dic.keys():  #dic에 값들 넣어줌.
        dic.update({int(age):[name]}) #없으면 추가
    else: #같은 나이 있으면
        dic[int(age)].append(name)

dic2 = sorted(dic.items()) # 정렬 진행 나이순 먼저, 이름순으로 정렬되게 age:name 구조로 만들었었음.

for item in dic2:
    for i in range(len(item[1])): #이름수, 즉 dic안의 개수 만큼 정렬된거에 맞게 출력
        print(item[0], item[1][i])
