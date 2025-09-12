a = int(input())
sign = ''
if (a > 0):
    sign = "положительное "
elif (a < 0):
    sign = "отрицательное "
else:
    sign = "нулевое "
parity = ''
if (a != 0):
    if (a % 2 == 0):
        parity = "четное "
    else:
        parity = "нечетное "
print(sign, parity, "число", sep = '')