class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count=sub=0
        for i in range(len(nums)):
            if nums[i]!=0:
                sub=nums[i]
                count+=1
                for j in range(len(nums)):
                    nums[j]-=sub

        return count