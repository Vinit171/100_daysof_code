# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        if root.val > val and root.left != None:
            return self.searchBST(root.left, val)
        if root.val < val and root.right != None:
            return self.searchBST(root.right, val)




"""
I am grateful for the enlightening session by Anvi Sharma, organized by the placement team of VIT Bhopal. It was truly inspiring and will aid me in my personal growth as I prepare for the challenges ahead. I would like to thank Shriram R sir for organizing such valuable webinars that have the power to change our mindset and push us to work harder and be a proud representative of VIT Bhopal.
"""