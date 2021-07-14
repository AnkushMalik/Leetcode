'''
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head and not head.next: return True
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        rev = None
 
        while slow:
            curr = slow
            slow = slow.next
            curr.next = rev
            rev = curr
        
        while rev:
            if rev.val!=head.val:
                return False
            rev = rev.next
            head = head.next
        return True
