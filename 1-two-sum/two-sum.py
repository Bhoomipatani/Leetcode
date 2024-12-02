class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            if target-nums[i] in hm:
                j=hm[target-nums[i]]
                break
            else:
                hm[nums[i]]=i
        return [j,i]
                