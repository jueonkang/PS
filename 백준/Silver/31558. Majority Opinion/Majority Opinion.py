T = int(input())
for i in range(T):
  N = int(input())
  a = list(map(int,input().split()))

  hay = set()
  for j in range(N-2):
    lst = [a[j],a[j+1],a[j+2]]
    lst.sort()
    if lst[0] == lst[1] or lst[2] == lst[1]:
      hay.add(lst[1])
  if len(a) == 2 and a[0] == a[1]:
      hay.add(a[0])

  hay = list(hay)
  if len(hay) == 0:
      hay.append(-1)
  hay.sort()
      
      
    
  print(*hay)
      
  