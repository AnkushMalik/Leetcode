class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        pHash = self.makeHash(p)
        ans = []
        i=0
        wd = [0]*26
        while(i<len(s)):
            if i>=len(p):
                if wd==pHash:
                    ans.append(i-len(p))
                old = ord(s[i-len(p)])-ord('a')
                wd[old]-=1
                wd[ord(s[i])-ord('a')]+=1
            else:
                wd[ord(s[i])-ord('a')]+=1
            i+=1
        if wd==pHash:
            ans.append(i-len(p))
        return ans
    def makeHash(self, s):
        arr = [0]*26
        for i in s:
            arr[ord(i)-ord('a')]+=1
        return arr