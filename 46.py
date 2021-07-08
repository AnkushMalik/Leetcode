'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.findAllPerms(nums,[],ans,len(nums))
        return ans
    
    def findAllPerms(self,arr,comb,ans,limiter):
        if(len(comb)==limiter):
            ans.append(comb[:])
            return True
        else:
            for i in arr:
                comb.append(i)
                newarr = [x for x in arr if x!=i]
                self.findAllPerms(newarr,comb,ans,limiter)
                comb.pop()
