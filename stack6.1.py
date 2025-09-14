N = int(input())
cnt = 0
for i in range(N):
    a = int(input())
    cnt += (a == 0)
print(cnt)