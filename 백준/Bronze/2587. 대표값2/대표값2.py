b = 0
c = []
for i in range(5):
  a = int(input())
  c.append(a)
  b += a
print(b//5)
c.sort()
print(c[2])