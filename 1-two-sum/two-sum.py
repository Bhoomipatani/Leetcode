class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(0,len(nums)):
            if target-nums[i] in hm:
                return [hm[target-nums[i]],i]
            else:
                hm[nums[i]]=i