class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                a+=s[i]
        l=0
        r=len(a)-1
        # print(a,l,r)
        while l<=r:
            if a[l]==a[r]:
                l+=1
                r-=1
            else:
                return False
        return True
