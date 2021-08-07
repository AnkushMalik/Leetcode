'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=end=0
        for i in range(len(s)):
            maxL = max(self.expandFromMiddle(s,i,i),self.expandFromMiddle(s,i,i+1))
            if maxL>end-start:
                start = i-(maxL-1)//2
                end = i+(maxL)//2
        return s[start:end+1]

    def expandFromMiddle(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            r+=1
            l-=1
        return r-l-1
