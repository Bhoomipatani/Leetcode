class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h={}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]]=1
            else:
                h[nums[i]]+=1
        for key,value in h.items(): 
            if value>2:
                while value>2:
                    nums.remove(key)
                    value-=1
        return len(nums)