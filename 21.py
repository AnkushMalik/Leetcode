'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []

'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1==None or l2==None):
            return l1 if(l1) else l2
        if(l1.val<=l2.val):
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        ans=head
        while(l1 and l2):
            if(l1.val<=l2.val):
                ans.next=l1
                ans=ans.next
                l1=l1.next
            else:
                ans.next=l2
                ans=ans.next
                l2=l2.next

        ans.next=l1 if(l1) else l2
        return head

'''
with recursion:
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val<=l2.val:
            first,second = l1,l2
        else:
            first,second = l2,l1
        newfirst = first.next
        newSecond = second.next
        
        if first.next and second.val>=first.next.val:
            newSecond = second
            second = newfirst
            first.next = self.mergeTwoLists(newfirst,newSecond)
        else:
            first.next = second
            second.next = self.mergeTwoLists(newfirst,newSecond)
        return first
'''
