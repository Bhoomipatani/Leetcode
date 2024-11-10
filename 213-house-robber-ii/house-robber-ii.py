class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i, robbedFirst):
            if (i >= n or (i == n - 1 and robbedFirst)):
                return 0            
            return max(dfs(i + 1, robbedFirst), nums[i] + dfs(i + 2, robbedFirst))
        return max(dfs(1, False), nums[0] + dfs(2, True))