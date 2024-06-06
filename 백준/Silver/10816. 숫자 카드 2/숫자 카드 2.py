n = int(input())
card = list(map(int,input().split()))
m =int(input())
count = map(int,input().split())

a = {}

for x in card: 
  if x in a:
    a[x] += 1
  else:
    a[x] = 1

for x in count:
  if x in a:
    print(a[x], end= " ")
  else:
    print("0", end = " ")

