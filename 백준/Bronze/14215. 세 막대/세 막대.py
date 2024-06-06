a = list(map(int,input().split()))
a.sort()
answer = a[0] + a[1] + min(a[2], a[0]+a[1]-1)
print(answer)