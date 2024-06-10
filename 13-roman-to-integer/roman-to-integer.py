class Solution:
    def romanToInt(self, s: str) -> int:
        sys_val={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i=len(s)-2
        ans=0
        while i>=0:
            if sys_val[s[i]]<sys_val[s[i+1]]:
                ans-=sys_val[s[i]]
            else:
                ans+=sys_val[s[i]]
            
            i-=1
        return ans+sys_val[s[-1]]