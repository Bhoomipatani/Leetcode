class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s=list(s)
        i=0
        maxl=0
        ls=''
        while i<len(s):
            if s[i] not in ls:
                ls+=(s[i])
                maxl=max(maxl,len(ls))
                i+=1
            else:
                ls=ls[1:]
            # print(ls)
            
        return maxl