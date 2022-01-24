class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1: return True
        caps = range(ord('A'),ord('Z')+1)
        fC = ord(word[0]) in caps
        sC = ord(word[1]) in caps
        if sC==True and fC==False: return False
        for i in range(2,len(word)):
            temp = ord(word[i]) in caps
            if temp!=sC: return False
        return True
            