class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)[2:]
        n=list(n)
        ans=0
        for i in n:
            ans+=int(i)
        return ans