class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        candidates.sort()
        def fun(ind,target):
            if target==0:
                ans.append(ds[:])
            for i in range(ind, len(candidates)):
                if i!=ind and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                fun(i+1,target-candidates[i])
                ds.pop()

        fun(0,target)
        return ans