class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums=0
        winstart=0
        max_ans=float('inf')
        ans=0
        for i in range(len(nums)):
            sums+=nums[i]
            while sums>=target:
                max_ans=min(max_ans,i-winstart+1)
                sums-=nums[winstart]
                winstart+=1
        if max_ans==inf:
            return 0   
        return max_ans