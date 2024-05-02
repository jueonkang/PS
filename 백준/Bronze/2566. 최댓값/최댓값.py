m= 0
r = 0
c = 0

for i in range(9):
  a = list(map(int,input().split()))
  for j in range(9):
    if m<a[j]:
      m=a[j]
      r = i
      c = j
      

print(m)
print(r+1,c+1)

