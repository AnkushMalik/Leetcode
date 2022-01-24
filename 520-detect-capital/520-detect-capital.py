class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1: return True
        fC = word[0].isupper()
        sC = word[1].isupper()
        if sC==True and fC==False: return False
        for i in range(2,len(word)):
            temp = word[i].isupper()
            if temp!=sC: return False
        return True
            