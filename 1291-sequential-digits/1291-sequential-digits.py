class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        i = low
        j = high
        ans = []
        digL = digH = 0
        while(i):
            digL+=1
            i//=10
        while(j):
            digH+=1
            j//=10
        while(digL<=digH):
            j = digL
            while(j<=len(s)):
                num = int(s[j-digL:j])
                if low<=num and num<=high: ans.append(num)
                j+=1
            digL+=1
        return ans