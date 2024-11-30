class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        delete=0
        ans1=ans2=True
        r=len(s)-1
        while l<=r:
            # print(l,r,s[l],s[r])
            if s[l]==s[r]:
                l+=1
                r-=1
            elif l+1<=r and s[l+1]==s[r]:
                l+=1
                delete+=1
                if delete>1:
                    ans1= False
                    break
            else:
                ans1= False
                break
        l=0
        delete=0
        r=len(s)-1
        while l<=r:
            print(l,r,s[l],s[r])
            if s[l]==s[r]:
                l+=1
                r-=1
            elif r-1>=l and s[r-1]==s[l]:
                r-=1
                delete+=1
                if delete>1:
                    ans2= False
                    break
            else:
                ans2= False
                break
        if ans1 or ans2:    
            return True
        return False
