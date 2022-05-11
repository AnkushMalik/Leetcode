class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        count = 0
        def findCombs(vowel, n):
            if n==1: return len(vowel)
            k = 0
            for i in range(len(vowel)):
                k+= findCombs(vowel[i:], n-1)
            return k
        return findCombs(vowel, n)
                
                
            