import sys
input = sys.stdin.readline

a = [0] * 10001

b = int(input())
for i in range(b):
  c = int(input())
  a[c] += 1

for i in range(len(a)):
  if a[i] != 0:
    for j in range(a[i]):
      print(i)