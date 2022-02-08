class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while(len(s)>1):
            tmp = 0
            for i in s:
                tmp+=int(i)
            s = str(tmp)
        return int(s)