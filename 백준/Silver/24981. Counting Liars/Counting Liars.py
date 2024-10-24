N = int(input())
lst = []
for _ in range(N):
  a, b = input().split()
  b = int(b)
  lst.append([a,b])

ans = float("inf")

for i in range(N):# lst[i] --> 진실을 말하는 소
  count = 0 # 가짜 
  for j in range(N):
    if lst[j][0] == "L" and lst[j][1] < lst[i][1]:
      count+=1
    elif lst[j][0] == "G" and lst[j][1] > lst[i][1]:
      count += 1
  if count < ans:
    ans = count

print(ans)