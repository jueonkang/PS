N = int(input())
snow = list(map(int,input().split()))
snow.sort(reverse=True)


if max(snow) > 1440:
  print(-1)
else:
  ans = 0
  while sum(snow)>0:
    ans += 1 
    
    if len(snow) > 1:
      snow[0] -= 1
      snow[1] -= 1
    elif len(snow) == 1:
      snow[0] -= 1
    
    newsnow = []
    for i in snow:
      if i > 0: 
        newsnow.append(i)
    snow = newsnow
    snow.sort(reverse=True)

    if ans > 1440:
      print(-1)
      break

  else:
    print(ans)