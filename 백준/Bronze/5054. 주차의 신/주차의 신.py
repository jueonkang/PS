t = int(input())

for i in range(t):
  n = int(input())
  coordinate = list(map(int,input().split()))
  coordinate.sort()
  print(2*(coordinate[n-1]-coordinate[0]))
