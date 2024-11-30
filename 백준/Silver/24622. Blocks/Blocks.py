n = int(input())
blocks = [input() for _ in range(4)]
words = [input() for _ in range(n)]

def spell(word) : 
  for a in range(4) : 
    for b in range(4) : 
      for c in range(4) : 
        for d in range(4) : 
          if (a != b != c!= d ) and ( b != d != a != c) : 
            idx = 0 
            choose = [ a,b,c,d ]
            for w in range(len(word)) :
              if  word[w]  in blocks[choose[w]]: 
                idx += 1 
            if idx == len(word) : return True
  
  return False
            
for i in words: 
  if spell(i) : 
    print("YES")
  else : 
    print("NO")