#백준 5622 다이얼 브2
#시험 전 복습 할 것.    .index의 활용

str1 = input()
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

res = 0 #총 걸린 시간
for i in range(len(str1)):  #len으로 처리해주어야 함
    for j in alpha:
        if(str1[i] in j):
            res += alpha.index(j) + 3
print(res)
