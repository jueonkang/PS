n,m = map(int,input().split())
spotty_gene = [input() for _ in range(n)]
plain_gene = [input() for _ in range(n)]

position = 0

for i in range(m):
  spotty = set(spotty_gene[j][i] for j in range(n))
  plain = set(plain_gene[j][i] for j in range(n))

  if not (spotty&plain):
    position += 1

print(position)
