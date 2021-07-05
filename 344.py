'''
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.revString(s,0,len(s)-1)
    def revString(self,s,i,j):
        if(i>=j):
            return
        s[i],s[j]=s[j],s[i]
        self.revString(s,i+1,j-1)
        
