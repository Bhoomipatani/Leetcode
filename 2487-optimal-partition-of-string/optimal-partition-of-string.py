class Solution:
    def partitionString(self, s: str) -> int:
        res=[]
        ss=''
        for i in range(len(s)):
            if s[i] not in ss:
                ss+=s[i]
            elif s[i] in ss:
                res.append(ss)
                ss=''
                ss+=s[i]
        return len(res)+1