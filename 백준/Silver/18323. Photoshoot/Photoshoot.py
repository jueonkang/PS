N = int(input())
num = list(map(int,input().split()))

for i in range(1,N+1):
  cow = [i]  # [1]   [4,6,7,6]
  for j in range(1,N) :  # 1 ~ 4 
    tmp = num[j-1] - cow[j-1] # 3
    if (tmp in cow) or (tmp <= 0) : 
      break 
    cow.append(tmp) 

  if len(cow)  == N:
    print(*cow)
    break 