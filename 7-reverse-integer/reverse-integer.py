class Solution:
    def reverse(self, x: int) -> int:
        i=len(str(x))-1
        a=ans=0
        neg=False
        if x<0:
            x=-x
            neg=True
            i-=1
        
        while x>0:
            a=int(x%10)
            x=(x-a)/10
            ans+=a*(10**i)
            i-=1
        if neg==True:
            ans=-ans
        if ans<-(2**31) or ans>((2**31)-1):
            return 0
        return ans