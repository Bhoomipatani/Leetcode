class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n=len(security)
        canrob=[]
       
        inc=[0]*len(security)
        dec=[0]*len(security)
        for i in range(1,len(security)):
            if security[i]<=security[i-1]:
                inc[i]=inc[i-1]+1
        for i in range(len(security)-2,-1,-1):
            if security[i]<=security[i+1]:
                dec[i]=dec[i+1]+1
        for i in range(time,n-time):
            if inc[i]>=time and dec[i]>=time:
                canrob.append(i)
        
        return canrob