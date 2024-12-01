class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def perm(curr, counter):
            if len(curr)==len(nums):
                ans.append(list(curr))
                return
            for num in counter:
                if counter[num]>0:
                    curr.append(num)
                    counter[num]-=1
                    perm(curr,counter)
                    curr.pop()
                    counter[num]+=1
        ans=[]
        perm([],Counter(nums))
        return ans