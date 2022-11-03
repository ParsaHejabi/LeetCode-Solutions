from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBSTRecursive(self, root: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if root.val <= min_val or root.val >= max_val:
            return False

        leftValid = False
        rightValid = False

        if root.left != None:
            leftValid = self.isValidBSTRecursive(root.left, min_val, root.val)
        else:
            leftValid = True

        if root.right != None:
            rightValid = self.isValidBSTRecursive(
                root.right, root.val, max_val)
        else:
            rightValid = True

        return leftValid and rightValid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return self.isValidBSTRecursive(root, -math.inf, math.inf)
