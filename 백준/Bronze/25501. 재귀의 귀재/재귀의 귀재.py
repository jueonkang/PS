
def isPalindrome(s, l, r,cnt):
  if l >= r: return 1 , cnt
  elif s[l] != s[r]: return 0, cnt
  else: return isPalindrome(s, l+1, r-1,cnt+1)
  

a = int(input())
for i in range(a):
  b = input()
  c = list(isPalindrome(b,0,len(b)-1,1))
  print(c[0], c[1])

