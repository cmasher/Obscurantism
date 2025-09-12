print("Пожалуйста введите x, A, B в одной строке через пробел")
x, A, B = map(float, input().split())
# мне известно что нужно проверять не знак равенства в случае вещественных чисел, а на маленькую разницу:
delta = -0.00001
mike_can = A - x >= delta
Ivan_can = B - x >= delta
#считаем что числа A, B даны с точностью до сотых, (центов), поэтому разница в 0.001 цента должно хватить
if mike_can and Ivan_can:
    print(2)
elif mike_can:
    print("Mike")
elif Ivan_can:
    print("Ivan")
elif (A + B - x >= delta):
    print(1)
else:
    print(0)