class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=list(s) 
        tl=list(t)
        if len(sl) == len(tl):
            sl.sort()
            tl.sort()
            
            return sl==tl
        else:
            return False