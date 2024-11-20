class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low=0
        high=m-1
        while low<=high:
            mid=low+(high-low)//2
            if matrix[mid][0]<=target and matrix[mid][-1] >= target:
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high=mid-1
        row=mid
        # print(row)
        l=0
        r=n-1
        while l<=r:
            # print(mid)
            mid=l+(r-l)//2
            if matrix[row][mid]==target:
                return True
            
            if matrix[row][mid]<target:
                # print("l")
                l = mid + 1
                # print(l)
            else:
                r=mid-1

        return False