class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        if len(s)<=k:
            return s[::-1]
        while i <len(s):
            # print(s,i)
            if i==0:
                s=s[i:i+k][::-1]+s[i+k::]
            elif i%(2*k)==0 and i!=0:
                # print(s[::i])
                # print(s[i:i+k])
                # print(s[i+k::])
                s=s[0:i]+s[i:i+k][::-1]+s[i+k::]
            i+=1
        return s