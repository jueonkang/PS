def count(word) : 
  a = [0] * 26 
  for w in word: 
    a[ord(w)-ord("a")] += 1 
  return a

N = int(input())
alphabet = [0] * 26 

for i in range(N):
  a,b = input().split()
  cnt_a,cnt_b = count(a),count(b)
  
  for j in range(26) : 
    alphabet[j] += max(cnt_a[j],cnt_b[j])

print(*alphabet,sep = "\n")

  