class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sHash = self.genHash(s)
        tHash = self.genHash(t)
        for i in range(26):
            if sHash[i]!=tHash[i]:
                return chr(i+97)
    def genHash(self,s):
        arr = [0]*26
        for i in s:
            arr[ord(i) - ord('a')]+=1
        return arr