n = int(input())
current = set()

for i in range(n):
  A, B = input().split()
  if B == "enter":
    current.add(A)
  elif B == "leave":
    current.remove(A)

current = sorted(list(current) , reverse = True)
for i in range(len(current)):
  print(current[i])