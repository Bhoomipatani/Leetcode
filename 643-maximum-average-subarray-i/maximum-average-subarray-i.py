class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=0
        max_avg=-inf
        sums=0
        win=1
        for i in range(len(nums)):
            sums=sums+nums[i]
            if win>=k:
                avg=sums/k
                max_avg=max(max_avg,avg)
                sums=sums-nums[i-k+1]
                win-=1
                
            win+=1
        return max_avg