class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        if len(s)<=k:
            return s[::-1]
        while i <len(s):
            if i%(2*k)==0 :
                s=s[:i]+s[i:i+k][::-1]+s[i+k:]
                i+=k
            else:
                i+=1
        return s