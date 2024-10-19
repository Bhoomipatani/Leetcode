class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def helper(openp,closep, s):
            if openp==n and closep==n:
                ans.append(s)
                return
            # if open==n next close
            # if open==close next open
            # if open>close and open<n next open or close
            if openp==n:
                s+=')'
                helper(openp, closep+1, s)
            if openp==closep:
                s+='('
                helper(openp+1, closep, s)
            if openp>closep and openp<n:
                s+='('
                helper(openp+1, closep, s)
                s=s[0:-1]+')'
                helper(openp, closep+1, s)
        res=helper(0,0,'')
        return ans
            
