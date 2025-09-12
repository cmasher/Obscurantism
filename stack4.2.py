# a_4, a_3, a_2, a_1, a_0 = map(int, input().split(''))
# жалко что так нельзя ^
a = int(input())
a_0 = a % 10
a //= 10
a_1 = a % 10
a //= 10
a_2 = a % 10
a //= 10
a_3 = a % 10
a //= 10
a_4 = a % 10
print(a_1 ** a_0 * a_2 / (a_4 - a_3))