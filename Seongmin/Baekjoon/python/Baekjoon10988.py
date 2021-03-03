#백준 10988 팰린드롬인지 확인하기 브1

str1 = input()
if str1 == str1[::-1]:
    print(1)
else:
    print(0)