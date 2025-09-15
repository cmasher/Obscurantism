l = list(map(float, input().split()))
s = set()
for el in l:
    if el in s:
        print('YES')
    else:
        s.add(el)
        print('NO')