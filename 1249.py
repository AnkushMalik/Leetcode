'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pt_idx = []
        stk = []
        i = 0
        while(i<len(s)):
            if(s[i]=='('):
                stk.append(s[i])
                pt_idx.append(i)
            elif(s[i]==')'):
                if(len(stk)!=0 and stk[-1]=='('):
                    stk.pop()
                    pt_idx.pop()
                else:
                    s = s[:i]+s[i+1:]
                    i-=1
            i+=1
        for i in pt_idx[::-1]:
            s = s[:i]+s[i+1:]
        return s
