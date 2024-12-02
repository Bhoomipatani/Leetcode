class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0]==target:
                return True
            elif matrix[i][0]<target:
                low=0
                high=len(matrix[0])-1
                while low<=high:
                    mid=low+(high-low)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                        high=mid-1
                    else:
                        low=mid+1
            else:
                return False
        return False
