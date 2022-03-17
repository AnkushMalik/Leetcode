class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s)==0: return 1
        stk = []
        ptr = 0
        score = 0
        for i in range(len(s)):
            if s[i]=='(':
                stk.append(s[i])
            else:
                stk.pop()
            if not stk:
                if ptr+1==i:
                    score+=1
                else:
                    score+=2*self.scoreOfParentheses(s[ptr+1:i])
                ptr=i+1
        return score