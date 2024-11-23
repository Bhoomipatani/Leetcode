class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm={}
        a=[]
        for i in range(len(arr)):
            if arr[i] in hm:
                hm[arr[i]]+=1
            else:
                hm[arr[i]]=1
        for i in hm:
            
            if hm[i] in a:
                return False
            else:
                a.append(hm[i])
        
        return True
