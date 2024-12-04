from itertools import combinations

skills = [int(input())for _ in range(12)]

skills.sort()
min_ = float("inf")

for t1 in combinations(range(12), 3):
  remain1 = set(range(12)) - set(t1)
  t1sum = sum(skills[i] for i in t1)

  for t2 in combinations(remain1, 3):
    remain2 = set(remain1) - set(t2)
    t2sum = sum(skills[i] for i in t2)

    for t3 in combinations(remain2, 3):
      t3sum = sum(skills[i] for i in t3)
      t4sum = sum(skills[i] for i in remain2 - set(t3))

      maxskill = max(t1sum,t2sum,t3sum,t4sum)
      minskill = min(t1sum,t2sum,t3sum,t4sum)
      min_ = min(min_, maxskill-minskill)

print(min_)
