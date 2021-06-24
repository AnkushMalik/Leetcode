'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
'''

class Solution:
    def reverse(self, x: int):
        num=0
        temp= abs(x)
        while(temp!=0):
            dig= temp%10
            num=num*10+dig
            temp=temp//10
        if abs(num)<2**31:
            if x>0:
                return num
            else:
                return num*-1
        else:
            return 0