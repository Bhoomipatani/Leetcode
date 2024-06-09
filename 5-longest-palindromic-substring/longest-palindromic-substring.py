class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palin(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l=l-1
                r=r+1
            return s[l+1:r]
        max_str=s[0]
        for i in range(len(s)-1):
            odd=palin(i,i)
            even=palin(i,i+1)
            if len(odd)>len(max_str):
                max_str=odd
            if len(even)>len(max_str):
                max_str=even
        return max_str