'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Bad answer; first approach
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        itr = head
        nodeInfo = []
        
        while itr:
            nodeInfo.append(itr)
            itr = itr.next
            nodeInfo[-1].next=None

        ans = nodeInfo.pop(0)
        if nodeInfo:
            ans.next = nodeInfo.pop()
        itr = ans.next
        
        while(len(nodeInfo)!=0):
            itr.next = nodeInfo.pop(0)
            itr = itr.next
            if(len(nodeInfo)!=0):
                itr.next = nodeInfo.pop()
                itr = itr.next
        return ans
