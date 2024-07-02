date = int(input())

nums = list(map(int,input().split()))
answer = 0
for i in range(5):
  if nums[i] == date:
    answer+=1

print(answer)
