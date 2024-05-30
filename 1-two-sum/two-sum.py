class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            nums2=target-nums[i]
            if nums2 in nums and nums.index(nums2)!=i:
                return [i, nums.index(nums2)]