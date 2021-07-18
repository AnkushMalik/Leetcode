'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

'''

class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        while(s!=''):
            if s[0]==' ':
                s = s[1:]
            elif s[0].isdigit():
                num = ''
                while s and s[0].isdigit():
                    num+=s[0]
                    s=s[1:]
                stk.append(int(num))
            elif s[0] in ['+','-','(']:
                stk.append(s[0])
                s=s[1:]
            else:
                res = ''
                while stk and stk[-1]!='(':
                    res=str(stk.pop())+res
                stk.pop()
                subAns = self.calculate(res)
                stk.append(subAns)
                s = s[1:]
        is_add = True
        ans = 0
        i=0
        if len(stk)==1:
            return int(stk.pop())
        if not stk:
            return 0
        while(i<len(stk)):
            if isinstance(stk[i],int):
                ans = ans+stk[i] if is_add else ans-stk[i]
            else:
                if stk[i]=='-' and stk[i+1]=='-':
                    is_add = True
                    i+=2
                    continue
                else:
                    is_add = True if stk[i]=='+' else False
            i+=1
        return ans
        
#not really a good solution but this is what i came with. should use only one main iteration to calculate the solution
