class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None): return head
        nxt = head.next
        ptr = head
        while(nxt):
            if nxt.val==ptr.val:
                ptr.next = nxt.next
                # nxt = nxt.next
            else:
                ptr = ptr.next
            nxt = nxt.next
        return head