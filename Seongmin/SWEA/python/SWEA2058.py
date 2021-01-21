"""
Case 2 풀이 로직
1234 = 1 * 1000 + 2 * 100 + 3 * 10 + 4 * 1

1234/10 => 몫 123, 나머지 4(일의 자리)
123/10 -> 나머지 3(십의 자리)...
"""
number = int(input())


def sum_of_digit(number):
    total = 0

    while number / 10:  # 값이 있는동안 계속
        remainder = number % 10
        total += remainder
        number = number // 10
    return total


print(sum_of_digit(number))