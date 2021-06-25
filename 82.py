'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
'''

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        j=head
        k=None
        while j and j.next:
            if j.val==j.next.val:
                while j and j.next and j.val==j.next.val:
                    j=j.next
                j=j.next
                if(k==None):
                    head=j
                else:
                    k.next=j
            else:
                k=j
                j=j.next
        return head

