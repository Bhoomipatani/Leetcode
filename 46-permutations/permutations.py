class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def perms(ind):
            if ind>=len(nums):
                ans.append(nums[:])
                return
            for i in range(ind,len(nums)):
                print(i)
                nums[ind],nums[i]=nums[i],nums[ind]
                perms(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
        perms(0)
        return ans

