'''
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]

'''

class Solution:
    even = ["00","11","69","88","96"]
    odd = ["0","1","8"]
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n==1:
            return ["0","1","8"]
        if n==2:
            return ["11","69","88","96"]
        
        ans = []
        if n%2==0:
            bases = self.findStrobogrammatic(n-2)
            for i in bases:
                for j in self.even:
                    ans.append(i[:len(i)//2]+j+i[len(i)//2:])
        else:
            bases = self.findStrobogrammatic(n-1)
            for i in bases:
                for j in self.odd:
                    ans.append(i[:len(i)//2]+j+i[len(i)//2:])

        return ans
