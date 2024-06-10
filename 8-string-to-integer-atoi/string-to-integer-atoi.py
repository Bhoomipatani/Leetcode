class Solution:
    def myAtoi(self, s: str) -> int:
        ans=''
        num='0123456789'
        for i in s:
            if (i=='-' or i=='+') and ans=='':
                ans+=i
            elif i in num:
                ans+=i
            elif i==' ' and len(ans)==0:
                continue
            else:
                break

        if ans=='' or ans in '-+':
            return 0
        else:
            if int(ans)<-(2**31):
                return -(2**31)
            elif int(ans)>(2**31-1):
                return (2**31-1)
            else:
                return int(ans)