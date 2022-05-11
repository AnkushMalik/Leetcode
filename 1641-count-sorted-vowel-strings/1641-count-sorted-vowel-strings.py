class Solution:
    def countVowelStrings(self, n: int) -> int:
        def findCombs(vowel, n):
            if n==1: return vowel
            k = 0
            for i in range(vowel):
                k+= findCombs(vowel-i, n-1)
            return k
        return findCombs(5, n)
                
                
            