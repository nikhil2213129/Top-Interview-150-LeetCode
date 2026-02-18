# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        tail = head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next
        def reverse(cur,end):
            prev = None
            while cur != end:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        new_head = reverse(head,tail)
        head.next = self.reverseKGroup(tail,k)
        return new_head
        
