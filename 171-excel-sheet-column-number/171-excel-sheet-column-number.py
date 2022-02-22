class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        for i in columnTitle:
            idx = ord(i)-ord('A')+1
            count*=26
            count+=idx
        return count