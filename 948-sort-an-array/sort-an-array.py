class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,low,mid,high):
            l=low
            r=mid+1
            tarr=[]
            while l<=mid and r<=high:
                if arr[l]<=arr[r]:
                    tarr.append(arr[l])
                    l+=1
                else:
                    tarr.append(arr[r])
                    r+=1
            while l<=mid:
                tarr.append(arr[l])
                l+=1
            while r<=high:
                tarr.append(arr[r])
                r+=1
            for i in range(len(tarr)):
                arr[i+low]=tarr[i]
        def mergesort(arr,low,high):
            if low>=high:
                return
            mid=(low+high)//2
            mergesort(arr,low,mid)
            mergesort(arr,mid+1,high)
            merge(arr,low,mid,high)
        
        mergesort(nums,0,len(nums)-1)
        return nums