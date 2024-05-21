a,b = map(int,input().split())
c = []

for i in range(1,b+1):
  for j in range(i):
    c.append(i)

answer = 0
for i in range(a-1,b):
  answer += c[i]
print(answer)