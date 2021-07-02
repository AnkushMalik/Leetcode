'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist_hsh = {}
        for i in range(len(arr)):
            dist_hsh[i]=abs(arr[i]-x)
        sorted_dists = sorted(dist_hsh.items(),key=lambda p:p[1])
        ans = []
        for i in range(k):
            idx,dist = sorted_dists[i]
            ans.append(arr[idx])
        return sorted(ans)
