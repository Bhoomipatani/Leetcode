class Solution:
    def countAndSay(self, n: int) -> str:
        rle='1'
        for j in range(n-1):
            ans=''
            a=rle[0]
            count=1
            for i in range(1,len(rle)):
                check=rle[i]
                if check==a:
                    count+=1
                else:
                    ans+=str(count)+str(a)
                    a=check
                    count=1
            ans+=str(count)+str(a)
            rle=ans
        return rle
        