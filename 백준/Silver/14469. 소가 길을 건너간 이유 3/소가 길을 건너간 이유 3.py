
N = int(input())
total = 0
lst = []

for i in range(N):
  A, B = map(int,input().split())
  lst.append([A,B])

lst.sort()
time_calculate = 0

for i in range(N):
  if time_calculate <  lst[i][0] : 
    time_calculate = lst[i][0] + lst[i][1]
  else : 
     time_calculate += lst[i][1]


print(time_calculate)  


