'''
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

 

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
Example 2:

Input: n = 1
Output: [0,1]
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        #recursive function to get 8bit numbers with single bit change difference
        def bit8code(num):
            if(num==1):
                return ["0","1"]
            ans = []
            res = bit8code(num-1)
            
            '''
			tricky part is that we have to add 1 to reverse of n-1 solution;
			for eg: if n=3; [n-1:2 solution] =              [00,01,11,10]
			appending 0, infront of n-1 solution:           [000,001,011,010]
			but now appending 1 to reverse of n-1 solution: [110, 111,101,100]
			notice the merge of arrays in the previos 2lines:  all the 8bits  are just a bit different of previous 8bit number
			'''
            for i in res:
                ans.append("0"+i)
            for i in res[::-1]:
                ans.append("1"+i)
            return ans
        
        bit8arr = bit8code(n)
        # convert all 8bit numbers to decimal to return the list of integer in desired order.
        for i in range(len(bit8arr)):
            c8 = int(bit8arr[i])
            if(c8==0):
                bit8arr[i]=c8
            else:
                j = 0
                intn = 0
                while(c8!=0):
                    rem = c8%10
                    c8 = c8//10
                    intn+=rem*(2**j)
                    j+=1
                bit8arr[i]=intn
        return bit8arr
