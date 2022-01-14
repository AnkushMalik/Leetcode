class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        while nums1 and nums2:
            k = nums1.pop()
            for i in range(len(nums2)):
                if nums2[i]==k:
                    nums2.pop(i)
                    ans.append(k)
                    break;
        return ans