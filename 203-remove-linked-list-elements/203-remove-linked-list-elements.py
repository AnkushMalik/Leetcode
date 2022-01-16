class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if(head==None):
            return head
        
        #head correction
        while(head and head.val==val):
            head=head.next
        if(head==None):
            return head
        
        
        i = head
        nxt = head.next
        
        while(i and i.next):
            while(nxt and nxt.val == val):
                nxt =nxt.next
            i.next = nxt
            i = nxt
            if(i):
                nxt = i.next
        return head