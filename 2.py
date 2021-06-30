'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lg=sm=None
        h1 = l1
        h2 = l2
        
        while(l1 and l2):
            l1 = l1.next
            l2 = l2.next
        if(l2==None):
            lg=h1
            sm=h2
        else:
            lg=h2
            sm=h1

        ansh = lg

        while lg or sm:
            if sm:
                lg.val+=sm.val
                carr = lg.val//10
                lg.val%=10
                if lg.next:
                    lg.next.val +=carr
                sm = sm.next
            else:
                carr = lg.val//10
                if carr==0:
                    return ansh
                else:
                    lg.val%=10
                    if lg.next:
                        lg.next.val +=carr
                    else:
                        nN = ListNode(carr)
                        lg.next=nN
                        return ansh
            if(not sm and not lg.next and carr!=0):
                nN = ListNode(carr)
                lg.next=nN
                return ansh
            lg = lg.next
                
            

        return ansh
