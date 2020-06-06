# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = l = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            tmp = 0
            if l1: tmp += l1.val
            if l2: tmp += l2.val
            l.next = ListNode((tmp + carry)%10)
            if tmp + carry >= 10:
                carry = 1
            else:
                carry = 0
            l = l.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return l3.next
        
