# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        first = temp
        second = temp
        for i in range(n+1): second = second.next
        while second:
            second=second.next
            first=first.next
        first.next=first.next.next
        return temp.next
        