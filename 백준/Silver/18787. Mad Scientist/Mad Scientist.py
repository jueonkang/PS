N = int(input())
A = input()
B = input()

flip = 0
miss = False

for i in range(N):
  if A[i] != B[i]:
    if not miss:
      flip += 1
      miss = True
  else:
     miss = False

print(flip)
