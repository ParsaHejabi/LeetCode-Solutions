# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        visited = {}
        traversal = []
        stack = []
        stack.append(root)

        while len(stack) > 0:
            if stack[-1].left != None and stack[-1].left not in visited.keys():
                stack.append(stack[-1].left)
            else:
                front = stack.pop()
                traversal.append(front.val)
                visited[front] = True
                if front.right != None:
                    stack.append(front.right)

        return traversal
