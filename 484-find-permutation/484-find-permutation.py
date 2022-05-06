class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stk, ans = [], []
        for i in range(len(s)):
            stk.append(i+1)
            if s[i]=='I':
                while stk: ans.append(stk.pop())
        stk.append(len(s)+1)
        while stk: ans.append(stk.pop())
        return ans