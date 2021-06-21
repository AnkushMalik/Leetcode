'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while(n!=0):
            num = n%10
            n = (int)(n/10)
            s += num
            p*=num
        return p-s
