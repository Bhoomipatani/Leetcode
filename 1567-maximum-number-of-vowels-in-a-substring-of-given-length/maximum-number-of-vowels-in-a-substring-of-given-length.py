class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a', 'e', 'i', 'o', 'u']
        # ss=s[:k]
        c=0
        ss=''
        v=0
        ans=-inf
        i=0
        while i<len(s):
            if c<k:
                ss+=s[i]
                if s[i] in vowels:
                    v+=1
                c+=1
                i+=1
            elif c==k:
                ss+=s[i]
                if s[i] in vowels:
                    v+=1
                if s[i-k] in vowels:
                    v-=1
                ss=ss[-k:]
                i+=1
            
            ans=max(ans,v)
            # print(ss,v,c,ans)
        return ans