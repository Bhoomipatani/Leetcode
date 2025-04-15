class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        swaps=0
        minnum=min(nums)
        maxnum=max(nums)
        minindex,maxindex=float('inf'), float('-inf')
        for i in range(n):
            if nums[i]==minnum:
                minindex=min(minindex,i)
            if nums[i]==maxnum:
                maxindex=max(maxindex,i)
        if minindex>maxindex:
            swap=minindex+n-maxindex-2
        else:
            swap=minindex+n-maxindex-1
        return swap