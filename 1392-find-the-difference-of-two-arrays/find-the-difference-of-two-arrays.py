class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr=[]
        nums2=list(set(nums2))
        nums1=list(set(nums1))
        for i in range(len(nums1)):
            if nums1[i] not in nums2 :
                arr.append(nums1[i])
            else:
                nums2.remove(nums1[i])
        return [arr,nums2]