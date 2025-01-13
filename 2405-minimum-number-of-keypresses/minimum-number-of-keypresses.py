class Solution:
    def minimumKeypresses(self, s: str) -> int:
        n=len(s)
        hm={}
        for i in range(n):
            if s[i] not in hm:
                hm[s[i]]=0
            hm[s[i]]+=1
        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        press=0
        l=0
        for v in hm.values():
            if l<9:
                press+=v
            elif 9<=l<18:
                press+=2*v
            else:
                press+=3*v
            l+=1
        return press
