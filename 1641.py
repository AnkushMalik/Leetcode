'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045

'''


#simple recursion:
class Solution:
    def countVowelStrings(self, n: int) -> int:
        def buildVowelGrid(n):
            if n==1: return ['1','2','3','4','5']
            else:
                lastGrid = buildVowelGrid(n-1)
                currGrid = []
                for i in lastGrid:
                    for j in range(int(i[-1]),6):
                        currGrid.append(i+str(j))
                return currGrid
        return len(buildVowelGrid(n))

#with memoisation:
class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.vowelGrid = {}
        def buildVowelGrid(n,vowels):
            if n==1: return vowels
            if vowels==1: return 1
            if (n,vowels) not in self.vowelGrid:
                self.vowelGrid[(n,vowels)] = buildVowelGrid(n-1,vowels)+buildVowelGrid(n,vowels-1)
            return self.vowelGrid[(n,vowels)]
        return buildVowelGrid(n,5)
