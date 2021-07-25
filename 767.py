'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        hsh = {}
        for i in s:
            if i in hsh: 
                hsh[i]+=1
            else: hsh[i]=1
                
        charSet = list(hsh.items())
        stk = []
        midCheck = len(s)//2 if len(s)%2==0 else len(s)//2+1
        for i in charSet:
            if i[1]>midCheck: return ""
            stk.append(i)
        ans = ""
        
        while stk:
            stk.sort(key=lambda k:k[1], reverse=True)
            char = stk.pop(0)
            if ans and char[0]==ans[-1]:
                stk.append(char)
                char = stk.pop(0)
            ans+=char[0]
            if char[1]>1: stk.insert(1,(char[0],char[1]-1))
        return ans
