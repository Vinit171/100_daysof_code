# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = head
        l = []
        while m:
            l.append(m.val)
            m = m.next

        n = set(l)
        m = list(n)
        m.sort()
        dummy = temp = ListNode(0)
        for s in m:
            new = ListNode(s)
            temp.next = new
            temp = temp.next

        return dummy.next
