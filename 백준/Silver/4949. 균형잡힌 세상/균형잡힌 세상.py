while(1):
    st = input()
    if st =='.':
        break
        
    stack = []
    result = True
    
    for i in st:
        if i == '(' or i =='[':
            stack.append(i)
        elif i==')':
            if len(stack)==0 or stack[-1]=='[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i==']':
            if len(stack)==0 or stack[-1]=='(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if len(stack)==0 and result==True:
        print('yes')
    else:
        print('no')