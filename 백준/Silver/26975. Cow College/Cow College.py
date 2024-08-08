N = int(input())
lst = list(map(int,input().split()))
lst.sort()
# 1 4 6 6 
total, min_ = 0,0

for i in range(N):
  tmp = lst[i] * (N-i)
  if tmp > total : 
    total = tmp 
    min_ = lst[i] 

print(total,min_)


