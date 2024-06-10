class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(1,len(strs)):
            j=0
            str2=strs[i]
            while j<len(prefix) and j<len(str2) and  prefix[j]==str2[j] :
                j+=1
            prefix=prefix[0:j]
        return prefix