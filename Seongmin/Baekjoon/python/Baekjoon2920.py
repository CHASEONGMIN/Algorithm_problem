#백준 2920 음계 브2
#그냥 input으로 받으면 str형이네

str1 = input()
str2 = '1 2 3 4 5 6 7 8'

if str1 == str2:
    print('ascending')
elif str1 == str2[::-1]:
    print('descending')
else:
    print('mixed')






