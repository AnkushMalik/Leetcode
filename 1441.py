'''
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the answer is unique.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
'''

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stk = []
        c = 0
        for i in range(1,n+1):
            if(i>target[-1]):
                return stk
            if(i!=target[c]):
                stk.append('Push')
                stk.append('Pop')
            else:
                stk.append('Push')
                c+=1
        return stk
