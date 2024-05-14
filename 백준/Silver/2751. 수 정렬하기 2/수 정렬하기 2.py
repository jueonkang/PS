import sys

input = sys.stdin.readline

a = int(input())
c= []

for i in range(a):
  b = int(input())
  c.append(b)
  
c.sort()

for i in range(a):
  print(c[i])
