T = int(input())

for _ in range(T):
  mod, want = input().split()
  
  mod_apos = []
  want_apos = []

  for i in range(len(mod)):
    if mod[i] == "a":
      mod_apos.append(i)

  for i in range(len(want)):
    if want[i] == "a":
      want_apos.append(i)
  
  ans = 0
  for i in range(len(mod_apos)):
    ans+= abs(mod_apos[i]-want_apos[i])

  print(ans)
