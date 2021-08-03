'''
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1

'''

#BACKTRACKING:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.relevantStrings = []
        self.findAllRelevantString(2*n, "(")
        return self.relevantStrings
    
    def findAllRelevantString(self, n, s):
        if len(s)==n:
            if self.isValid(s):
                self.relevantStrings.append(s)
        else:
            for char in ["(",")"]:
                s+=char
                self.findAllRelevantString(n,s)
                s=s[:-1]

    def isValid(self, s):
        stk = []
        for i in s:
            if i==')' and not stk: return False
            if i=='(':
                stk.append(i)
            elif stk:
                stk.pop()
        return False if stk else True
