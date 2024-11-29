class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        i=0
        count=0
        while i<(len(s)):
            if s[i]=='(':
                count+=1
                stack.append(s[i])
            elif s[i]==')' and count>0:
                stack.append(s[i])
                count-=1
            elif s[i]!=')':
                stack.append(s[i])
            i+=1
        ans=[]
        for i in range(len(stack)-1,-1,-1):
            
            if  stack[i]=='(' and count>0:
                count-=1
            else:
                ans.append(stack[i])

        return ''.join(reversed(ans))
