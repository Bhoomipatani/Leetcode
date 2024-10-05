class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)-1
        return max(nums[0]*nums[1]*nums[l],nums[l]*nums[l-1]*nums[l-2])