class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm={}
        ans=0
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]]=1
            else:
                hm[s[i]]+=1
        print(hm)
        odd=False
        for val in hm.values():
            if val%2==0:
                ans+=val
            else:
                ans+=val-1
                odd=True
        if odd==True:  

            return ans+1
        else:
            return ans
            