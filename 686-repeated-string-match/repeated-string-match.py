class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        l = (m - 1) // n + 1
        for i in range(l, l + 3):
            ra = a * i
            if ra.find(b) >= 0:
                return i
        return -1