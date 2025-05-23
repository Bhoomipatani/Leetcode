class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=-inf
        while l<=r:
            a=min(height[l],height[r]) *(r-l)
            ans=max(ans,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return ans