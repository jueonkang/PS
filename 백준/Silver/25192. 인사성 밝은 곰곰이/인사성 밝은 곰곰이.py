N = int(input())
gom = set()
count = 0

for i in range(N):
  a = input()
  if a == "ENTER":
    count += len(gom)
    gom = set()
  else:
    gom.add(a)

count += len(gom)
print(count)


