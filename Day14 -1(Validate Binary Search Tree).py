# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ax=[]
        def pre(root):
            if root is None:
                return

            pre(root.left)
            ax.append(root.val)
            pre(root.right)

        arr = pre(root)
        if len(ax)!=set(ax):
            return(False)
        q = ax.copy()
        if q.sort()==ax:
            return(True)
        else:
            return(False)

