class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreachable=0
        for i in range(len(nums)):
            maxreachable=max(maxreachable,nums[i]+i)
            if maxreachable>=len(nums)-1:
                return True
            if maxreachable<=i:
                return False
        return False
