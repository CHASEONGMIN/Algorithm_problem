x = int(input()) #(−1000 ≤ x ≤ 1000; x ≠ 0)
y = int(input()) #(−1000 ≤ y ≤ 1000; y ≠ 0)

if(x < 0 and y < 0):
    print(3)
elif(x < 0 and y > 0):
    print(2)
elif (x > 0 and y < 0):
    print(4)
elif (x > 0 and y > 0):
    print(1)
else:
    print('try again')
