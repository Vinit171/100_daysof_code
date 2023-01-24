class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = head
        while m:
            if m.val == None:
                return (True)
            m.val = None
            m = m.next

        return (False)
