class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root is None:
            return ans
        else:
            pass

        l = collections.deque()
        l.append(root)
        while l:
            lb = []
            q = len(l)
            while q > 0:
                currN = l.popleft()
                lb.append(currN.val)
                q = q - 1
                if currN.left is not None:
                    l.append(currN.left)
                if currN.right is not None:
                    l.append(currN.right)
            ans.append(lb)
        return (ans)






