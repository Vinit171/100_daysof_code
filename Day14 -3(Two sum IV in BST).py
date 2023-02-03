# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []

        def pre(root):
            if root is None:
                return
            pre(root.left)
            l.append(root.val)
            pre(root.right)

        pre(root)
        for n in range(len(l)):
            q = k - l[n]
            if n < len(l) - 1:
                t = l[:n] + l[n + 1:]
                # print(t,"dfgg")
            else:
                t = l[:len(l) - 1]
                # print(n,"fg")
                # print(t,"sdf")
            if q in t:
                return (True)

        return (False)