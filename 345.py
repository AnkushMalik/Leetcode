'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        l = 0
        r = len(s)-1
        
        lc = rc = ''
        
        while(r>=l):            
            if(s[l] in vowels):
                lc = s[l]
                l-=1

            if(s[r] in vowels):
                rc = s[r]
                r+=1
                
            if( lc!='' and rc!='' ):
                l+=1
                r-=1
                s[l]=rc
                s[r]=lc

                lc= rc =''
            l+=1
            r-=1

        s = ''.join(s)
        return s
