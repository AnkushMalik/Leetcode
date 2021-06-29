'''
Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.
 

Example 1:

Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
Example 2:

Input: v1 = [1], v2 = []
Output: [1]
Example 3:

Input: v1 = [], v2 = [1]
Output: [1]
'''


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1[::-1]
        self.v2 = v2[::-1]
        self.zz = 1 #bool val if true pop from v1 if false pop from v2

    def next(self) -> int:
        if(self.zz==1 and len(self.v1)!=0):
            self.zz=2
            return self.v1.pop()
        else:
            self.zz=1
            if(len(self.v2)!=0):
                return self.v2.pop()
            else:
                return self.v1.pop()
        

    def hasNext(self) -> bool:
        return True if (len(self.v1)+len(self.v2))!=0 else False
