m = float(input())
n = int(input())
weight = sorted([float(input()) for i in range(n)])
# класический жадный алгоритм стремящийся сначала перевезти самых тяжелый рыбаков
count = 0 #кол во лодок
while len(weight) > 0:
    count += 1
    w1 = weight[-1]
    weight.pop()
    x = m - w1
    # двоичный поиск самого тяжелого рыбака которого мы сможем перевезти:
    # границы l, r (l всегда сможем перевезти, r не можем)
    if len(weight) == 0:
        break
    w2 = weight[0]
    if (w2 > x):
        continue
    w2 = weight[-1]
    if w2 <= x:
        weight.pop()
        continue
    r = len(weight) - 1
    l = 0
    while r - l > 1:
        mid = (r + l) // 2
        if weight[mid] > x:
            r = mid
        else:
            l = mid
    weight.pop(l)
print(count)