class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans=0
        if len(nums)<3:
            return 0
        diff=[0]*(len(nums)-1)
        for i in range(1,len(nums)):
            diff[i-1]=nums[i]-nums[i-1]
        count=1
        print(diff)
        for i in range(len(diff)-1):
            print(count,ans)
            if diff[i]==diff[i+1]:
                count+=1
            elif diff[i]!=diff[i+1] and count>=2:
                i=2
                while i<=count:
                    ans+=count+1-i
                    i+=1
                count=1
        i=2
        while i<=count:
            ans+=count+1-i
            i+=1
        count=1
        return ans
