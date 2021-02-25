#백준 2941 크로아티아 알파벳 실5
#발상을 역으로 alpha를 str1과 비교를하자
#중요.  입력받은 값의 특정 부분이 다른 문자열과 매칭이 되면 replace로 바꿔주어 해결

str1 = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    str1 = str1.replace(i, 'a')

print(len(str1))
