class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        for i in range(0,len(s)):
            if s[i] in dict1:
                dict1[s[i]]+=1
            else:
                dict1[s[i]]=1
        for i in range(0,len(t)):
            if t[i] in dict1:
                dict1[t[i]]-=1
            if t[i] not in dict1:
                return False
        for val in dict1:
            if dict1[val] !=0:
                return False
        return True