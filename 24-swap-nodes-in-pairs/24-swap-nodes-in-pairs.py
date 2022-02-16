class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        curr = head
        cnxt = head.next
        curr.next = cnxt.next
        cnxt.next = curr
        
        curr.next = self.swapPairs(curr.next)
        return cnxt