class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums=['1','2','3','4','5','6','7','8','9']
        n=len(str(low))
        m=len(str(high))
        print(n,m)
        arr=set()
        for i in range(n,m+1):
            for j in range(len(nums)):
                num=int(''.join(nums[j:j+i]))
                if num>=low and num<=high:
                    arr.add(num)    
        arr=list(arr)
        arr.sort()
        
        return arr
