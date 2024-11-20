class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        j=max(piles)
        i=1
        while i<j:
            hours=0
            k=(i+j)//2
            for n in range(len(piles)):
                hours+=ceil(piles[n]/k)   
            if hours>h:
                i=k+1
            else:
                j=k
           
        return i
                