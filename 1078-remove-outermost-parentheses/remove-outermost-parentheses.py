class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        i=0
        ans=''
        while i <len(s):
            if s[i]=='(':
                if stack!=[]:
                    ans+=s[i]  
                stack.append(s[i]) 
            elif s[i]==')':
                stack.pop()
                if stack!=[]:
                    ans+=s[i]     
            # print(i,ans)
            i+=1
        return ans               