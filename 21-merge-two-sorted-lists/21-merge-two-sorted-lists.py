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