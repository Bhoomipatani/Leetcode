class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hms={}
        hmt={}
        
        for i in range(len(s)):
            if s[i] not in hms and t[i] not in hmt:
                hms[s[i]]=t[i]
                hmt[t[i]]=s[i]
            
            elif hms.get(s[i])!=t[i] or hmt.get(t[i])!=s[i]:
                return False
        return True
