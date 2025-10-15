class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1] and k<2:
                k+=1
                i+=1
            elif nums[i]==nums[i-1] and k>=2:
                nums.remove(nums[i])
            else:
                i+=1
                k=1
        return len(nums)
            