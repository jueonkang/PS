import sys
input = sys.stdin.readline

a = input()
b = sorted(a,reverse = True)

for i in range(len(b)):
  print(b[i], end="")
  