# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a = head
        l = []
        while a:
            l.append(a.val)
            a = a.next

        l2 = []
        for x in l:
            if x == val:
                pass
            else:
                l2.append(x)

        dummy = temp = ListNode(0)
        for xx in l2:
            new = ListNode(int(xx))
            temp.next = new
            temp = temp.next
        return dummy.next