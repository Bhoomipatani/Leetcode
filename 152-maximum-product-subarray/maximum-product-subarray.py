class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin=1,1
        res=max(nums)
        for n in nums:
            tmp=curMax
            curMax=max(n*curMax, n*curMin, n)
            curMin=min(tmp*n, n*curMin, n)
            res=max(curMax,res)
        return res