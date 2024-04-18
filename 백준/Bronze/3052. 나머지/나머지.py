c = []
for i in range(1,11):
  a = int(input())
  b = a%42
  if b in c:
    continue
  else:
    c.append(b)
print(len(c))