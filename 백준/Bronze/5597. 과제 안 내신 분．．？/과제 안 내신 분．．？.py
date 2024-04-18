a = [i for i in range(1,31)]
for i in range(28):
  B = int(input())
  a.remove(B)
print(min(a))
print(max(a))
