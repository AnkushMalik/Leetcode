'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        hsh = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        if(len(s)%2!=0):
            return False
        stck = [s[0]]
        s = s[1:]
        while(len(s)!=0):
            c = s[0]
            if(len(stck)==0 or c not in hsh.keys()):
                stck.append(c)
            elif(c in hsh.keys() and stck[-1]==hsh[c]):
                stck.pop()
            else:
                return False
            s = s[1:]
        return False if len(stck) else True
            
                
