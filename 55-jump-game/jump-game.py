class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreachable=0
        for i in range(len(nums)):
            if i>maxreachable:
                return False
            maxreachable=max(maxreachable, nums[i]+i)
            if maxreachable>=len(nums)-1:
                return True
        return False