'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''

#DP tabular:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0]*(len(text2)) for _ in range(len(text1))]
        def findLCS(a,b,i,j):
            if i>=len(a) or j>=len(b): return 0
            if memo[i][j]:
                return memo[i][j]
            same = 0
            if a[i]==b[j]: same = 1 + findLCS(a,b,i+1,j+1)
            diff1 = findLCS(a,b,i,j+1)
            diff2 = findLCS(a,b,i+1,j)
            memo[i][j] =  max(same,diff1,diff2)
            return memo[i][j]
        return findLCS(text1,text2,0,0)
