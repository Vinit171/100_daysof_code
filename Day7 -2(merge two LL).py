# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        q = list1

        l = []

        while q:
            l.append(q.val)
            q = q.next

        q2 = list2
        l2 = []
        while q2:
            l2.append(q2.val)
            q2 = q2.next

        l.extend(l2)
        l.sort()
        dummy = temp = ListNode(0)
        for v in l:
            new = ListNode(int(v))
            temp.next = new
            temp = temp.next

        return dummy.next