# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = head
        l=[]
        while k:
            l.append(k.val)
            k=k.next
        l.reverse()

        dummy = temp = ListNode(0)
        for xx in l:
            new = ListNode(int(xx))
            temp.next = new
            temp = temp.next
        return dummy.next