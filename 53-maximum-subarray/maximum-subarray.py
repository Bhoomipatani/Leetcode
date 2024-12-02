class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=1
        maxsum=nums[0]
        currsum=nums[0]
        while i<len(nums):
            # print(currsum)
            if currsum+nums[i]<nums[i]:
                currsum=nums[i]
            else:
                currsum+=nums[i]
            maxsum=max(currsum,maxsum)
            i+=1
        return maxsum