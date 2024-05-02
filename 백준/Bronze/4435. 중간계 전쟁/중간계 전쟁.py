tc = int(input())

for i in range(1, tc + 1) :
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  gan_score = a[0] + a[1]*2 + a[2]*3 + a[3]*3 + a[4]*4 + a[5]*10
  sau_score = b[0] + b[1]*2 + b[2]*2 + b[3]*2 + b[4]*3 + b[5]*5 + b[6]*10

  if gan_score > sau_score :
    print(f"Battle {i}: Good triumphs over Evil")
  elif gan_score < sau_score :
    print(f"Battle {i}: Evil eradicates all trace of Good")
  else :
    print(f"Battle {i}: No victor on this battle field")