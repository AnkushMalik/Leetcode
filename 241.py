'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''


class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        ans = []
        for i in range(len(exp)):
            if not exp[i].isdigit():
                lans = self.diffWaysToCompute(exp[:i])
                rans = self.diffWaysToCompute(exp[i+1:])
                for j in lans:
                    for k in rans:
                        ans.append(eval(str(j)+exp[i]+str(k)))
        if not ans:
            ans.append(int(exp))
        return ans
        
        
