class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k <len(nums):
            nums[:]=nums[n-k:]+nums[0:n-k]
        else:
            for i in range(k):
                nums[:]=nums[-1:]+nums[:-1]
        return nums