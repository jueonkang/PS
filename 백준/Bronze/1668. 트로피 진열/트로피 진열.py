N = int(input())
answer = 0
lst = []

for i in range(N):
  a = int(input())
  lst.append(a)

left_max = 0
left_answer = 0
right_max = 0
right_answer = 0

for i in range(N):
  if lst[i] > left_max:
    left_max = lst[i]
    left_answer += 1 

  if lst[N-(i+1)] > right_max :
    right_max = lst[N-(i+1)]
    right_answer += 1 

print(left_answer)
print(right_answer)