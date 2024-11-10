class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
            
        def rob_helper(houses):
            dp = [0] * len(houses)
            for i in range(len(houses)):
                dp[i] = max(houses[i]+dp[i-2], dp[i-1])

            return dp[-1]

        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))