'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        while(head.next and head.val==head.next.val):
            head=head.next
        itr = head
        while(itr and itr.next):
            while(itr.next and itr.val==itr.next.val):
                itr.next=itr.next.next
            itr = itr.next
        return head
