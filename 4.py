'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findMedian(arr):
            arr_len = len(arr)
            if(arr_len%2!=0):
                return arr[(int)(arr_len/2)]
            else:
                j = (int)(arr_len/2)
                i = j-1
                return (arr[i]+arr[j])/2
        comb_arr = []
        while(len(nums1)!=0 or len(nums2)!=0):
            small = -1
            if(len(nums1)==0 or len(nums2)==0):
                comb_arr = comb_arr+nums1+nums2
                break;
            if (nums1[0]<=nums2[0]):
                small = nums1[0]
                nums1 = nums1[1:]
            else:
                small = nums2[0]
                nums2 = nums2[1:]
            comb_arr.append(small)
        return findMedian(comb_arr)

# not a good solution but i am learning, so i guess its okay.
