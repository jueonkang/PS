import sys
input = sys.stdin.readline

stack = []
N = int(input())

for i in range(N):
  a = int(input())
  if a == 0:
    stack.pop()
  else:
    stack.append(a)

print(sum(stack))
 