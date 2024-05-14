def isPalindrome(s, l, r):
  global cnt
  cnt += 1 
  if l >= r: return 1 
  elif s[l] != s[r]: return 0
  else: return isPalindrome(s, l+1, r-1)
  

a = int(input())

for i in range(a):
  b = input()
  cnt = 0
  c = isPalindrome(b,0,len(b)-1)
  print(c, cnt)