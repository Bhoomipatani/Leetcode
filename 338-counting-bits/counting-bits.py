class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            cnt=0
            while i>1:
                if i%2==1:
                    cnt+=1
                i=i//2
            if i==1:
                cnt+=1
            ans.append(cnt)
        return ans