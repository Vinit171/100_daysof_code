# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ans = []
        if root is None:
            return (0)
        s = []
        s.append(root)
        while s:
            ll = len(s)
            qq = []
            while ll > 0:
                curr = s.pop(0)
                qq.append(curr.val)
                ll = ll - 1
                if curr.left is not None:
                    s.append(curr.left)
                if curr.right is not None:
                    s.append(curr.right)

            ans.append(qq)
        return (len(ans))
        # if root is None:
        #   return(0)

        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
