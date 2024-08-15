class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        maxSum=-inf
        for i in range(0,len(nums)):
            a=nums[i]
            curr+=a
            if curr<a:
                curr=a
            if curr>maxSum:
                maxSum=curr
        return maxSum