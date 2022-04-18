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
            for i in self.keypad[digits[0]]:
                newComb= comb+i
                self.findAllCombinations(digits[1:], newComb, ans, limiter)