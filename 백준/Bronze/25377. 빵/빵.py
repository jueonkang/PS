n = int(input())  
a = []
b = []
for i in range(n):
    c, d = map(int, input().split())  
    a.append(c)
    b.append(d)

time = []
for i in range(n):
    if b[i] >= a[i]:  
        time.append(b[i])

if time:
    print(min(time))  
else:
	print(-1)