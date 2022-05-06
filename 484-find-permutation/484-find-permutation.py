class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stk, ans = [], []
        for i in range(len(s)):
            stk.append(i+1)
            if s[i]=='I':
                ans += stk[::-1]
                stk = []
        stk.append(len(s)+1)
        ans += stk[::-1]
        return ans