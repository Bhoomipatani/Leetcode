class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        l = m//n
        repeatstr=""
        for i in range(l+2):
            repeatstr+=a
            if b in repeatstr:
                return i+1
        return -1