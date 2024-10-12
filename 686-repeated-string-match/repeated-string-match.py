class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        l = m//n
        copya=""
        for i in range(l+2):
            copya+=a
            if b in copya:
                return i+1
        return -1