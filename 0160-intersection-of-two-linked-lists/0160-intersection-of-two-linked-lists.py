# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
       
        if not headA or not headB:
            return None
        ptrA,ptrB=headA,headB
        while ptrA!=ptrB:
            ptrA=ptrA.next if ptrA else headB
            ptrB=ptrB.next if ptrB else headA
        return ptrA