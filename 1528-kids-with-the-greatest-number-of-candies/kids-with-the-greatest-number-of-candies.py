class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_arr=max(candies)
        arr=[]
        for i in range(len(candies)):
            if max_arr<=extraCandies+candies[i]:
                arr.append(True)
            else:
                arr.append(False)
        return arr