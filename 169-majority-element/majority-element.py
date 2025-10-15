class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        k=None
        for num in nums:
            if c==0:
                k=num
            if num==k:
                c+=1
            else:
                c-=1
        return k