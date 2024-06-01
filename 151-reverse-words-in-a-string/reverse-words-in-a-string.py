class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split()
        string=''
        for i in range(len(t)-1,-1, -1):
            string+=t[i]
            if i!=0:
                string+=' '

        return string