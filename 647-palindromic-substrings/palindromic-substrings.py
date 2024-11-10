class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=[]
        def pallin(l,r):
            while l>=0 and r<=len(s)-1 and s[l]==s[r] :
                ans.append(s[l:r+1])
                l-=1
                r+=1

        for i in range(len(s)):
            odd=pallin(i,i)
            even=pallin(i,i+1)
        return len(ans)
            