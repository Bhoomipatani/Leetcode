class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        larr=[0]*len(nums)
        rarr=[0]*len(nums)
        n=len(nums)
        for i in range(1,len(nums)):
            larr[i]=larr[i-1]+nums[i-1]
            rarr[n-i-1]=rarr[n-i]+nums[n-i]
        for i in range(0,len(nums)):
            if larr[i]==rarr[i]:
                return i
        return -1