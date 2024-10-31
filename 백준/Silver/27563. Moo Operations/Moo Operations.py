Q = int(input())
results = []

for _ in range(Q):
  s = input()
  n = len(s)

  if s== "MOO":
    results.append(0)
    continue

  if n < 3:
    results.append(-1)
    continue

  elif "MOO" in s:
    minoperation = n-3
    results.append(minoperation)

  elif "MOM" in s:
    minoperation = n-2
    results.append(minoperation)

  elif "OOO" in s:
    minoperation = n-2
    results.append(minoperation)

  elif "OOM" in s:
    minoperation = n-1
    results.append(minoperation)

  else:
    results.append(-1)

for i in results:
  print(i)