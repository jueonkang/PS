N, M = map(int,input().split()) 
cowheight = list(map(int,input().split()))
caneheight = list(map(int,input().split()))

for i in range(M):
  max_, min_ = caneheight[i], 0
  for j in range(N):
    if cowheight[j] > min_ :
      original = min(max_,cowheight[j])
      cowheight[j] += original - min_
      min_ = original
    if max_ <= min_:
      break 
      

for i in range(N):
  print(cowheight[i])