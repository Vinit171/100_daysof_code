# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root

        q = collections.deque()
        q.appendleft(root)
        while (len(q) > 0):
            top = q.pop()
            if top.val > val:
                if top.left:
                    q.appendleft(top.left)
                else:
                    top.left = TreeNode(val)
            if top.val < val:
                if top.right:
                    q.appendleft(top.right)
                else:
                    top.right = TreeNode(val)
        return root