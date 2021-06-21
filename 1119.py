'''
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:

Input: s = "aeiou"
Output: ""
'''

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        ans = ''.join(s)
        c = 0
        for idx,char in enumerate(s):
            if(s[idx] in vowels):
                ans = ans[:idx-c]+ans[idx-c+1:]
                c+=1

        return ans