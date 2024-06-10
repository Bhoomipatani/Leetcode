class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a=strs[0]
        b=strs[-1]
        ans=''
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if a[i]!=b[i]:
                return ans
            ans+=a[i]
        return ans