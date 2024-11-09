class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)
        def helper(i):
            if i<0:
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]= max(helper(i-2)+nums[i], helper(i-1))
            return memo[i]
        return helper( len(nums)-1)
            