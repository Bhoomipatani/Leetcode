class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreachable=0
        
        for i in range(len(nums)):
            if maxreachable+1>=len(nums):
                return True
            if maxreachable==i and nums[i]==0:
                return False
            maxreachable=max(maxreachable,nums[i]+i)
            # print(i,maxreachable)

        return False
