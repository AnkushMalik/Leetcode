class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        ptr = ans
        while(l1 and l2):
            if l1.val<l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        remaining = l1 if l1 else l2
        ptr.next = remaining
        return ans.next
                