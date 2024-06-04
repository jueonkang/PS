lst = []

for i in range(9):
  a = int(input())
  lst.append(a)

b,c = -1,-1 

for i in range(8):
  for j in range(i+1, 9):
    if sum(lst)-lst[i]-lst[j] == 100:
      b,c = i,j
      break
      
lst.pop(b)
lst.pop(c-1)
for i in lst:
  print(i)
    
    