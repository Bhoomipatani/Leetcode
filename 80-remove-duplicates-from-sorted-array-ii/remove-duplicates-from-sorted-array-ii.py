class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=nums[0]
        k=0
        i=0
        while i<len(nums):
            if num==nums[i]:
                k+=1
            if num==nums[i] and k>2:
                nums.pop(i)
            elif num!=nums[i]:
                num=nums[i]
                k=1
                i+=1
            else:
                i+=1
        return len(nums)