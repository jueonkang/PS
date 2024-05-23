
import sys
input = sys.stdin.readline

stack = []

N = int(input())
for i in range(N):
  a = input().split()
  if len(a) == 2:
    stack.append(a[1])
  else:
    a = int(a[0]) 
    if a == 2:
      if len(stack) == 0:
        print(-1)
      else:
        print(stack.pop())
    if a == 3:
      print(len(stack))
    if a == 4:
      if len(stack) == 0:
        print(1)
      else: 
        print(0)
    if a == 5:
      if len(stack) == 0:
        print(-1)
      else:
        print(stack[-1])