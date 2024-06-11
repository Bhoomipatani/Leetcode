class Solution:
    def minInsertions(self, s):
        @lru_cache(None)
        def dp(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            if i >= j: return 0
            return min(dp(i + 1, j), dp(i, j - 1)) + 1
        return dp(0, len(s) - 1)