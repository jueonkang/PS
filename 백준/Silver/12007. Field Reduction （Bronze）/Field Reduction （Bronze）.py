  
N = int(input())

cows = []
for _ in range(N):
  x,y = map(int,input().split())
  cows.append([x,y])
  
cowsx = sorted(cows)
cowsy = sorted(cows, key=lambda cow : cow[1])

minx = cowsx[0][0]
secminx = cowsx[1][0]
maxx  = cowsx[-1][0]
secmaxx = cowsx[-2][0]

miny = cowsy[0][1]
secminy = cowsy[1][1]
maxy  = cowsy[-1][1]
secmaxy = cowsy[-2][1]

ans = (maxx-minx) * (maxy-miny)

for i in range(N):
  x,y = cows[i]

  if minx == x : 
    newminx = secminx
  else:
    newminx = minx

  if maxx == x : 
    newmaxx = secmaxx
  else:
    newmaxx = maxx

  if miny == y : 
    newminy = secminy
  else:
    newminy = miny

  if maxy == y : 
    newmaxy = secmaxy
  else:
    newmaxy = maxy

  area = (newmaxx-newminx) *(newmaxy-newminy)
  if area < ans:
    ans = area

print(ans)
