class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(start_index, i):
            if i == start_index:
                return nums[start_index]
            if i == start_index + 1:
                return max(nums[start_index], nums[start_index + 1])

            if (start_index, i) in memo:
                return memo[(start_index, i)]

            memo[(start_index, i)] = max(nums[i] + dp(start_index, i-2), dp(start_index, i-1))
            return memo[(start_index, i)]

        return nums[0] if len(nums) == 1 else max(dp(0, len(nums) - 2), dp(1, len(nums) - 1))