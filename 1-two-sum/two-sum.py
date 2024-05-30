class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for i in range(0, len(nums)):
            nums2=target-nums[i]
            if nums2 in hmap:
                return [hmap[nums2],i]
            hmap[nums[i]]=i
        