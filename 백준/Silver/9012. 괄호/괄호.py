import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
  stack = []
  b = input().rstrip() 
  for j in b:
    if j == "(":
      stack.append(j)
    elif j == ")":
      if len(stack) == 0 :
        stack.append(j)

      elif stack[-1] == ")":
        stack.append(j)
      elif stack[-1] == "(":
        stack.pop()
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")
      