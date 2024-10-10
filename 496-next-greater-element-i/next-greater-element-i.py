class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng=[]
        flag=0
        for i in range(len(nums1)):
            flag=0
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    flag = 1 
                if flag==1 and nums1[i]<nums2[j]:
                    ng.append(nums2[j])
                    flag=0
                    break
            if len(ng)<=i:
                ng.append(-1)
        return ng