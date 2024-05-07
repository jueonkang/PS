a = int(input())
b= []
c = 0
max = 0
for i in range(a):
  b.append(int(input()))
for i in range(a-1,-1,-1):
  if b[i] > max:
    max=b[i]
    c +=1

print(c)