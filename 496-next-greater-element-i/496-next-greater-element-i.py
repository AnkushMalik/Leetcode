class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = []
        for i in nums1:
            k = nums2.index(i)
            greaterElem = -1
            for j in range(k+1,len(nums2)):
                if nums2[j]>i:
                    greaterElem = nums2[j]
                    break
            nge.append(greaterElem)
        return nge
                    