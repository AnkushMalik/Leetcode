'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []

'''

class Solution:
    keypad = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="": return []
        ans=[]
        self.findAllCombinations(digits,'',ans,len(digits))
        return ans

    def findAllCombinations(self,digits, comb, ans, limiter):
        if(len(comb)==limiter):
            ans.append(comb)
            return
        else:
            if len(digits)==0:
                return
            for i in self.keypad[digits[0]]:
                newComb= comb+i
                self.findAllCombinations(digits[1:], newComb, ans, limiter)
