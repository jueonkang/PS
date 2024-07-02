N = int(input())
lst = list(map(int,input().split())) # 1,1,2,3
answer = 0
for i in range(N):
  total = 0
  p = set()
  for j in range(i,N): 
    total += lst[j]
    p.add(lst[j])
    if total / (j-i+1)  in p : 
      answer+=1


print(answer) 