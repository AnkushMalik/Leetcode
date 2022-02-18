class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num): return '0'
        stk = []
        for dig in num:
            while k and stk and stk[-1]>dig:
                stk.pop()
                k-=1
            stk.append(dig)
        if k: stk =stk[:-k]
        return "".join(stk).lstrip('0') or "0"